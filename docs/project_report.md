# NetSage AI — AI-Assisted Network Troubleshooting System

## 1. Abstract

NetSage AI is a human-in-the-loop artificial intelligence system designed to assist with troubleshooting Cisco-style laboratory networks. The system accepts network symptoms, topology information, and diagnostic command output such as `show` commands. It analyzes the supplied evidence and generates a structured diagnosis containing the likely root cause, affected OSI layer, supporting evidence, recommended diagnostic commands, and remediation steps.

The system combines Large Language Model (LLM) reasoning with deterministic rule-based validation. This hybrid approach reduces dependence on AI-only reasoning and provides an additional layer of verification for common networking faults. Human review is mandatory, allowing a reviewer to accept, edit, or reject an AI-generated diagnosis.

NetSage AI uses a dataset of 30 structured networking troubleshooting cases covering areas such as VLANs, IP addressing, DHCP, DNS, routing, ACLs, NAT, and wireless networking. The system also provides a dashboard for reviewing cases and AI outputs.

The application is implemented in Python and Streamlit and uses the OpenAI API for AI-assisted diagnosis. It has been deployed through Streamlit Cloud, making the system accessible through a web-based interface.

---

## 2. Introduction

Computer networks are composed of multiple interconnected devices and protocols. A small configuration error, such as an incorrect IP address, missing VLAN assignment, wrong default gateway, unavailable route, or incorrectly configured ACL, can cause communication failures.

Traditional troubleshooting requires a network administrator or student to inspect the topology, identify symptoms, execute diagnostic commands, interpret the output, determine the root cause, and apply an appropriate correction.

This process can be difficult for students and beginners because the same symptom may have several possible causes.

NetSage AI was developed to assist with this process. Instead of allowing an AI model to directly modify network configurations, the system uses a safer human-in-the-loop workflow. The AI analyzes evidence supplied by the user and proposes a diagnosis, while deterministic checks and human review provide additional safeguards.

---

## 3. Problem Statement

Students and laboratory users often encounter networking problems in environments such as Cisco Packet Tracer but may not know how to systematically identify the root cause.

Common problems include:

- Incorrect IP addressing
- Incorrect subnet masks
- Incorrect default gateways
- VLAN configuration errors
- Trunk configuration problems
- DHCP failures
- DNS configuration problems
- Missing or incorrect routes
- ACL-related connectivity problems
- NAT configuration issues
- Wireless connectivity problems
- Interfaces being administratively down

The objective is to develop an AI-assisted troubleshooting system that can interpret networking evidence and provide useful, explainable diagnostic guidance while keeping the final decision under human control.

---

## 4. Objectives

The major objectives of NetSage AI are:

1. Build a structured dataset containing at least 30 networking troubleshooting cases.
2. Cover common networking concepts including VLAN, IP addressing, DHCP, DNS, routing, ACL, NAT, and wireless networking.
3. Accept symptoms, topology information, and diagnostic command output as evidence.
4. Use an LLM to generate structured troubleshooting diagnoses.
5. Provide supporting evidence for each diagnosis.
6. Recommend appropriate next diagnostic commands.
7. Provide remediation steps.
8. Add deterministic rule-based checks for common networking errors.
9. Require human review of AI-generated diagnoses.
10. Store human feedback for later evaluation.
11. Provide a dashboard for interacting with troubleshooting cases.
12. Demonstrate the cases using Cisco Packet Tracer.
13. Deploy the application as a publicly accessible web application.

---

## 5. Proposed System

NetSage AI follows a human-in-the-loop troubleshooting workflow:

```text
User
  ↓
Network Symptoms + Topology + Diagnostic Evidence
  ↓
Streamlit Application
  ↓
LLM Diagnosis
  ↓
Structured JSON Response
  ↓
Deterministic Rule Checker
  ↓
Human Review
  ↓
Accepted / Edited / Rejected
  ↓
Recommended Packet Tracer Fix
  ↓
Verification
```

The system intentionally does not automatically modify Cisco configurations.

---

## 6. System Architecture

The major components of the system are:

### 6.1 Streamlit Application

Streamlit provides the web-based user interface. It allows the user to interact with the troubleshooting system and view the generated diagnosis and supporting information.

### 6.2 AI Diagnosis Module

The AI diagnosis module communicates with the OpenAI API and generates a structured diagnosis from the supplied networking evidence.

The diagnosis can contain:

- Likely root cause
- OSI layer
- Evidence
- Confidence
- Next diagnostic command
- Recommended remediation

### 6.3 Rule Checker

The deterministic checker validates common networking conditions using predefined rules.

Examples include:

- Interface down
- Missing VLAN
- Missing route
- Gateway mismatch
- Duplicate IP address

The rule checker provides an additional validation mechanism independent of the LLM.

### 6.4 Dataset

The project uses structured CSV files to store troubleshooting cases and review information.

Important files include:

```text
data/cases.csv
data/reviews.csv
```

### 6.5 Human Review

AI output is not treated as an automatically correct answer. A human reviewer can:

- Accept the diagnosis
- Edit the diagnosis
- Reject the diagnosis

The review information is stored for evaluation.

---

## 7. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application and troubleshooting logic |
| Streamlit | Web interface and deployment |
| OpenAI API | AI-assisted diagnosis |
| Pandas | CSV/data processing |
| Matplotlib | Dashboard visualization |
| CSV | Case and review storage |
| Cisco Packet Tracer | Network topology simulation |
| Git/GitHub | Version control and project hosting |
| Streamlit Cloud | Application deployment |

---

## 8. Dataset

The project contains 30 structured troubleshooting cases in:

```text
data/cases.csv
```

Each case contains information required to reproduce and evaluate a networking troubleshooting scenario.

The dataset includes fields representing information such as:

- Case identifier
- Network symptom
- Topology description
- Diagnostic or `show` command output
- Expected fault
- OSI layer
- Networking concept
- Severity

The cases are designed to represent realistic laboratory troubleshooting situations rather than relying only on theoretical questions.

---

## 9. Networking Areas Covered

The troubleshooting cases cover several important networking concepts.

### VLAN

Examples include incorrect VLAN assignments and missing VLAN configuration.

### IP Addressing

Cases include incorrect IP addresses, subnet configuration problems, and addressing inconsistencies.

### DHCP

Cases represent situations where hosts fail to obtain appropriate network configuration.

### DNS

Cases represent name-resolution failures and DNS-related configuration problems.

### Routing

Routing cases include missing routes and incorrect routing information.

### ACL

ACL cases demonstrate situations where traffic is unexpectedly permitted or denied.

### NAT

NAT-related cases demonstrate connectivity problems caused by incorrect translation configuration.

### Wireless

Wireless cases represent common connectivity and configuration problems in simulated environments.

---

## 10. AI Diagnosis Process

The AI diagnosis process follows these steps:

### Step 1 — Collect Evidence

The user provides information such as:

- Observed symptoms
- Network topology
- Relevant command output
- Additional observations

### Step 2 — Analyze Evidence

The application sends the relevant information to the AI diagnosis module.

### Step 3 — Generate Structured Diagnosis

The LLM produces a structured response rather than an unrestricted paragraph.

The response can contain:

```text
Root Cause
OSI Layer
Evidence
Confidence
Next Diagnostic Command
Remediation
```

### Step 4 — Validate

The application validates the AI response and applies deterministic checks where applicable.

### Step 5 — Human Review

The reviewer evaluates the diagnosis and can accept, edit, or reject it.

---

## 11. Deterministic Rule Checker

An important design feature of NetSage AI is that it does not rely entirely on LLM reasoning.

The Python-based rule checker identifies common conditions that can be detected deterministically.

Examples include:

```text
Interface Down
Missing VLAN
Missing Route
Gateway Mismatch
Duplicate IP
```

This hybrid architecture provides two complementary mechanisms:

```text
LLM reasoning
      +
Deterministic validation
      +
Human review
```

The purpose is not to guarantee that every diagnosis is correct, but to reduce the risk of blindly accepting an AI-generated answer.

---

## 12. Human-in-the-Loop Design

Human oversight is a central part of NetSage AI.

The system requires the human reviewer to make the final decision.

The workflow is:

```text
AI Diagnosis
     ↓
Human Review
     ↓
 ┌─────────┬────────┬─────────┐
 │ Accept  │  Edit  │ Reject  │
 └─────────┴────────┴─────────┘
```

Human review information is stored in:

```text
data/reviews.csv
```

This creates a feedback mechanism that can later be used to evaluate model performance and improve the troubleshooting dataset.

---

## 13. Dashboard

NetSage AI includes a dashboard component for presenting troubleshooting information and evaluation-related information.

The dashboard can be used to inspect the collected cases and review information.

Visualization is provided using Python-based data processing and Matplotlib.

The dashboard is intended to provide a simple overview of the troubleshooting system rather than replacing the underlying diagnostic workflow.

---

## 14. Cisco Packet Tracer Integration

Cisco Packet Tracer is used to reproduce networking scenarios corresponding to the troubleshooting cases.

A Packet Tracer case contains:

1. Network topology
2. Device configuration
3. Intentional fault
4. Observable symptom
5. Diagnostic evidence
6. Correct configuration/fix
7. Verification procedure

The Packet Tracer files provide reproducible evidence for the cases in the dataset.

The general workflow is:

```text
Create Topology
      ↓
Introduce Configuration Fault
      ↓
Observe Network Symptom
      ↓
Run Diagnostic Commands
      ↓
Record Evidence
      ↓
Create Dataset Case
      ↓
Test NetSage AI
      ↓
Apply Fix
      ↓
Verify Connectivity
```

---

## 15. Testing and Evaluation

The system is evaluated using the 30 troubleshooting cases.

Important evaluation dimensions include:

### Case Coverage

Whether the system can process cases across the targeted networking concepts.

### AI-Human Agreement

Whether the AI diagnosis agrees with the human-reviewed expected diagnosis.

### Evidence Usage

Whether the generated diagnosis is supported by evidence supplied in the case.

### Rule Checker Accuracy

Whether deterministic rules correctly identify supported configuration problems.

### Human Review

Whether reviewers accept, edit, or reject AI-generated diagnoses.

Actual numerical evaluation results should be reported only after running the final evaluation and should not be fabricated.

---

## 16. Responsible AI

NetSage AI follows several responsible-AI principles.

### Human Oversight

The system requires human review before a diagnosis is treated as the final troubleshooting decision.

### Evidence-Based Reasoning

The AI is expected to base its diagnosis on the supplied network evidence.

### No Automatic Configuration Changes

The system does not automatically modify Cisco device configurations.

### Uncertainty

AI-generated confidence should not be interpreted as a guarantee of correctness. Uncertain diagnoses should be verified by the user.

### Auditability

Human review information is stored in:

```text
data/reviews.csv
```

This allows the project to track how AI-generated diagnoses were evaluated.

---

## 17. Deployment

The NetSage AI application has been deployed as a web application.

The deployment architecture is:

```text
GitHub Repository
       ↓
Streamlit Cloud
       ↓
NetSage AI Web Application
       ↓
OpenAI API
```

The source code is maintained in GitHub.

The application is deployed using Streamlit Cloud.

The OpenAI API key is stored as a deployment secret rather than being included in the GitHub repository.

This prevents the API credential from being exposed through source control.

---

## 18. Project Structure

The main project structure is:

```text
NetSage-AI/
│
├── ai/
├── checker/
├── dashboard/
├── data/
├── docs/
├── prompts/
│
├── .env.example
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

Important components include:

```text
app.py
```

Main Streamlit application.

```text
ai/
```

AI diagnosis functionality.

```text
checker/
```

Deterministic networking validation.

```text
dashboard/
```

Dashboard and visualization components.

```text
data/
```

Troubleshooting cases and human-review data.

```text
docs/
```

Project documentation.

```text
prompts/
```

AI diagnosis prompt documentation.

---

## 19. Advantages

NetSage AI provides several advantages:

1. Assists students in understanding networking faults.
2. Provides structured troubleshooting guidance.
3. Uses actual networking evidence.
4. Combines AI reasoning with deterministic validation.
5. Maintains human control over the final diagnosis.
6. Supports reproducible Packet Tracer cases.
7. Stores review information for evaluation.
8. Provides a web-based interface.
9. Can be expanded with additional troubleshooting cases.
10. Can be deployed without requiring users to configure the complete development environment locally.

---

## 20. Limitations

The system has several limitations:

- LLM-generated diagnoses can be incorrect.
- The rule checker only covers supported fault patterns.
- Packet Tracer behavior may differ from physical Cisco equipment.
- The current dataset contains only 30 cases.
- CSV-based storage is not intended for large-scale production workloads.
- Network troubleshooting requiring information not supplied to the system may result in an uncertain diagnosis.
- AI confidence should not be interpreted as guaranteed probability of correctness.

---

## 21. Future Scope

Possible future improvements include:

### Larger Dataset

Expand the troubleshooting dataset from 30 cases to hundreds or thousands of cases.

### Retrieval-Augmented Generation

Integrate a networking knowledge base containing Cisco documentation, networking concepts, and verified troubleshooting procedures.

### Topology Graph Analysis

Allow the system to directly analyze network topology graphs rather than relying only on textual topology descriptions.

### Multi-Device Reasoning

Support simultaneous analysis of multiple routers, switches, servers, and hosts.

### Advanced Validators

Expand deterministic checks to include more routing protocols, VLAN/trunk conditions, ACL rules, NAT behavior, DHCP configuration, and interface statistics.

### Database Integration

Replace CSV-based storage with a database for larger deployments.

### Automated Evidence Collection

Future versions could collect supported diagnostic information automatically from network devices in controlled environments while still requiring human approval before configuration changes.

---

## 22. Conclusion

NetSage AI demonstrates a human-in-the-loop approach to AI-assisted network troubleshooting.

The project combines:

```text
Networking Evidence
       +
LLM Reasoning
       +
Deterministic Validation
       +
Human Review
       +
Packet Tracer Verification
```

The system supports 30 structured networking troubleshooting cases and covers important networking concepts including VLAN, IP addressing, DHCP, DNS, routing, ACL, NAT, and wireless networking.

Rather than allowing AI to make autonomous network changes, NetSage AI keeps the human reviewer responsible for the final decision. This design makes the system more suitable for educational networking laboratories and controlled troubleshooting environments.

The completed application is deployed through Streamlit Cloud and can be accessed through a web browser, while its source code and documentation are maintained in GitHub.

NetSage AI therefore provides a practical demonstration of how AI can assist network troubleshooting while maintaining evidence-based reasoning, deterministic checks, reproducibility, and human oversight.

---

## 23. References

1. Cisco Networking Academy — Networking Fundamentals and Cisco Packet Tracer.
2. OpenAI API Documentation.
3. Streamlit Documentation.
4. Python Documentation.
5. Pandas Documentation.
6. Matplotlib Documentation.
7. Standard networking concepts related to TCP/IP, VLAN, DHCP, DNS, routing, ACL, NAT, and wireless networking.

---

## 24. Project Deliverables

The final NetSage AI submission consists of:

- Live NetSage AI web application
- GitHub source-code repository
- Project report
- 30 troubleshooting cases
- Dashboard
- Responsible AI documentation
- Human-review records
- Cisco Packet Tracer `.pkt` files
- Demonstration video
- Project documentation
