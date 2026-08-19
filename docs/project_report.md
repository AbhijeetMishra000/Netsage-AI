# NetSage AI — Project Report

## Abstract
NetSage AI is a human-in-the-loop AI troubleshooting assistant for Cisco-style laboratory networks. It accepts symptoms, topology notes and `show` command output, then recommends a likely root cause, OSI layer, evidence, next diagnostic command and remediation steps.

## Objectives
- Build at least 30 troubleshooting cases.
- Cover VLAN, IP addressing, DHCP, DNS, routing, ACL, NAT and wireless.
- Use evidence-backed AI responses.
- Add deterministic checks.
- Require human review.
- Record AI corrections.
- Provide a dashboard and demonstration.

## Architecture
```text
User → Streamlit → LLM + Rule Checker → Structured Diagnosis → Human Review → Packet Tracer Fix → Verification
```

## Technology
Python, Streamlit, Pandas, OpenAI Responses API, CSV, Cisco Packet Tracer and Matplotlib.

## Dataset
`data/cases.csv` contains 30 structured troubleshooting cases with symptom, topology note, show output, expected fault, OSI layer, concept and severity.

## AI
The LLM returns structured JSON. The application validates the response and forces `human_review_required=true`.

## Rule Checker
Python checks common faults such as interface down, missing VLAN, missing route, gateway mismatch and duplicate IP.

## Human Oversight
Every diagnosis is Accepted, Edited or Rejected by a human. Reviews are stored in `data/reviews.csv`.

## Responsible AI
The system does not automatically change Cisco configuration. AI evidence must come from supplied input, and uncertain cases should have lower confidence.

## Evaluation
Measure AI-human agreement, rule-check accuracy, evidence usage and case coverage.

## Limitations
LLMs can be wrong; Packet Tracer output may differ from production Cisco devices; the checker covers only common configuration errors.

## Future Scope
Topology graph input, RAG networking knowledge base, larger dataset, multi-device reasoning and richer validators.

## Conclusion
NetSage AI demonstrates a safer AI-assisted network troubleshooting workflow by combining LLM reasoning, deterministic validation and mandatory human review.
