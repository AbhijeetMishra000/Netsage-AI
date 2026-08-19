def run_checks(symptom, topology, output):
    t=(symptom+" "+topology+" "+output).lower()
    return {
      "interface_status":"FAIL" if "line protocol is down" in t or "administratively down" in t else "PASS",
      "missing_vlan":"FAIL" if "vlan" in t and "absent" in t else "PASS",
      "missing_route":"FAIL" if "no route to" in t else "PASS",
      "gateway_mismatch":"FAIL" if "outside the" in t and "subnet" in t else "PASS",
      "duplicate_ip":"FAIL" if "duplicate ip" in t or "two mac addresses" in t else "PASS"
    }
