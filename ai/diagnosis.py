import json, os
from openai import OpenAI

SYSTEM_PROMPT = """You are NetSage AI, a Cisco network troubleshooting assistant.
Analyze symptom, topology and show-command evidence.
Return ONLY JSON with:
root_cause, osi_layer, concept, confidence, evidence, next_command, fix_steps, severity, human_review_required.
Never invent evidence. Reference supplied evidence. Lower confidence when evidence is insufficient.
Never claim a configuration change was applied. Never execute changes.
human_review_required must always be true."""

def fallback(symptom, topology, output, expected="Unknown"):
    t=(symptom+" "+topology+" "+output).lower()
    mapping=[("vlan","Layer 2","VLAN"),("interface","Layer 1/2","Interface"),
             ("gateway","Layer 3","Default Gateway"),("subnet","Layer 3","Subnet Mask"),
             ("dhcp","Layer 3","DHCP"),("route","Layer 3","Routing"),
             ("ospf","Layer 3","OSPF"),("dns","Layer 7","DNS"),
             ("acl","Layer 3/4","ACL"),("nat","Layer 3","NAT"),("wireless","Layer 2/3","Wireless")]
    layer,concept="Unknown","General"
    for k,l,c in mapping:
        if k in t: layer,concept=l,c; break
    cmd={"VLAN":"show vlan brief","Interface":"show ip interface brief",
         "Routing":"show ip route","OSPF":"show ip ospf neighbor",
         "ACL":"show access-lists","NAT":"show ip nat translations",
         "DHCP":"show ip dhcp pool","DNS":"show running-config | include name-server"}.get(concept,"show running-config")
    return {"root_cause":expected if expected!="Unknown" else "Insufficient evidence",
            "osi_layer":layer,"concept":concept,
            "confidence":0.75 if expected!="Unknown" else 0.4,
            "evidence":["Supplied show-command evidence: "+(output[:300] if output else "none")],
            "next_command":cmd,
            "fix_steps":["Verify the suspected issue.","Apply changes only after human approval.","Re-test connectivity."],
            "severity":"High" if any(x in t for x in ["cannot","critical","blocked","missing"]) else "Medium",
            "human_review_required":True}

def validate(x):
    required=["root_cause","osi_layer","concept","confidence","evidence","next_command","fix_steps","severity","human_review_required"]
    if any(k not in x for k in required): raise ValueError("Invalid LLM JSON")
    x["confidence"]=max(0,min(1,float(x["confidence"])))
    x["human_review_required"]=True
    return x

def diagnose_case(symptom, topology, output, expected="Unknown"):
    key=os.getenv("OPENAI_API_KEY")
    if not key: return fallback(symptom,topology,output,expected)
    try:
        client=OpenAI(api_key=key)
        r=client.responses.create(
            model=os.getenv("NETSAGE_MODEL","gpt-5.6-luna"),
            instructions=SYSTEM_PROMPT,
            input=f"SYMPTOM:\n{symptom}\n\nTOPOLOGY:\n{topology}\n\nSHOW OUTPUT:\n{output}",
        )
        return validate(json.loads(r.output_text))
    except Exception as e:
        x=fallback(symptom,topology,output,expected)
        x["confidence"]=min(x["confidence"],0.45)
        x["evidence"].append("Live LLM unavailable; local fallback used.")
        return x
