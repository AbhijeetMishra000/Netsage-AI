# System Architecture

## Flow
1. User selects a case.
2. Symptom, topology and show output are collected.
3. LLM produces structured diagnosis.
4. Response is validated.
5. Python rule checker runs.
6. Results are shown together.
7. Human selects Accept/Edit/Reject.
8. Review is saved.
9. Dashboard aggregates results.
10. Engineer fixes and verifies the Packet Tracer network.

## Safety Boundary
NetSage never directly executes configuration changes. It recommends; a human decides and applies.
