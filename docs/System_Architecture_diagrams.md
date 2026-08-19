# NetSage AI — System Architecture Diagrams

This document contains the major architecture diagrams of the NetSage AI system. The diagrams use Mermaid syntax and can be viewed directly on GitHub or in Markdown editors that support Mermaid.

---

## 1. High-Level System Architecture

```mermaid
flowchart TD
    U[User<br/>Network Problem / Symptoms] --> UI[Streamlit UI<br/>Symptoms, Topology, Show Output]

    UI --> CORE[NetSage AI Core]

    subgraph CORE[NetSage AI Core]
        LLM[LLM Diagnosis<br/>AI analyzes evidence]
        RC[Rule Checker<br/>Deterministic validation]
        LLM <--> RC
    end

    CORE --> SD[Structured Diagnosis<br/>Root Cause<br/>OSI Layer<br/>Evidence<br/>Next Command<br/>Remediation<br/>Confidence]

    SD --> HR[Human Review<br/>Accept / Edit / Reject]

    HR --> PT[Cisco Packet Tracer<br/>Apply / Reproduce Fix]

    PT --> V[Verification<br/>Connectivity / Resolution]
```

---

## 2. AI Diagnosis Pipeline

```mermaid
flowchart TD
    S[1. Symptoms<br/>Observed Network Problem] --> T[2. Topology Information<br/>Devices, Links, IPs, VLANs]
    T --> SO[3. Show Command Output<br/>show ip int brief<br/>show vlan<br/>show ip route<br/>etc.]
    SO --> EP[4. Evidence Preparation<br/>Collect and structure evidence]
    EP --> DP[5. Diagnosis Prompt<br/>Evidence + Instructions]
    DP --> API[6. OpenAI API<br/>LLM Processing]
    API --> JSON[7. Structured JSON Response]

    JSON --> F1[Root Cause]
    JSON --> F2[OSI Layer]
    JSON --> F3[Evidence]
    JSON --> F4[Confidence]
    JSON --> F5[Next Diagnostic Command]
    JSON --> F6[Remediation Steps]
    JSON --> F7[Human Review Required]
```

---

## 3. Hybrid AI + Rule Checker Architecture

```mermaid
flowchart TD
    E[Network Evidence<br/>Symptoms + Topology + Show Output] --> LLM[LLM Reasoning<br/>AI proposes diagnosis]
    E --> RULE[Rule Checker<br/>Deterministic checks]

    LLM --> VAL[Diagnosis Validation]
    RULE --> VAL

    VAL --> HR[Human Reviewer<br/>Final decision and feedback]

    subgraph RULES[Examples of Deterministic Checks]
        R1[Interface Down]
        R2[Missing VLAN]
        R3[Missing Route]
        R4[Gateway Mismatch]
        R5[Duplicate IP]
    end

    RULE -.-> RULES
```

---

## 4. Human-in-the-Loop Architecture

```mermaid
flowchart TD
    AI[AI Diagnosis<br/>Structured diagnosis] --> HUMAN[Human Reviewer<br/>Review AI output]

    HUMAN --> ACCEPT[Accept<br/>Diagnosis is correct]
    HUMAN --> EDIT[Edit<br/>Modify / Improve diagnosis]
    HUMAN --> REJECT[Reject<br/>Diagnosis is incorrect]

    ACCEPT --> STORE[Review Stored]
    EDIT --> STORE
    REJECT --> STORE

    STORE --> CSV[data/reviews.csv<br/>Evaluation and feedback]
```

---

## 5. Deployment Architecture

```mermaid
flowchart LR
    DEV[Developer<br/>Develop and Test Locally] -->|git push| GH[GitHub Repository<br/>Source Code + Documentation]

    GH -->|Deploy| SC[Streamlit Cloud<br/>NetSage AI Web Application]

    SC -->|API Request| OA[OpenAI API<br/>LLM Diagnosis]

    SEC[Streamlit Secrets<br/>OPENAI_API_KEY] -.->|Secure credential| SC
    SEC -.->|Authentication| OA

    GH -.->|Does NOT contain API key| SEC
```

---

## 6. Complete End-to-End Architecture

```mermaid
flowchart TD
    USER[User] --> INPUT[Symptoms<br/>Topology<br/>Diagnostic Output]

    INPUT --> STREAM[Streamlit Application]

    STREAM --> AI[AI Diagnosis Module]
    STREAM --> CHECK[Deterministic Rule Checker]

    AI --> OPENAI[OpenAI API]
    OPENAI --> AI

    AI --> DIAG[Structured Diagnosis]
    CHECK --> DIAG

    DIAG --> REVIEW[Human Review]

    REVIEW -->|Accept / Edit / Reject| FEEDBACK[data/reviews.csv]

    REVIEW --> PT[Cisco Packet Tracer]
    PT --> FIX[Apply Corrective Configuration]
    FIX --> VERIFY[Verify Connectivity]

    VERIFY --> RESULT[Confirmed / Resolved Case]

    CASES[data/cases.csv<br/>30 Troubleshooting Cases] --> STREAM
    PROMPT[prompts/diagnose_prompt.md] --> AI
```

---

## 7. Architecture Components

| Component | Responsibility |
|---|---|
| Streamlit UI | User interaction and presentation |
| AI Diagnosis Module | Sends evidence to the LLM and processes the response |
| OpenAI API | Provides LLM-based reasoning |
| Rule Checker | Performs deterministic checks for common faults |
| Structured Diagnosis | Standardizes AI output |
| Human Review | Accepts, edits, or rejects the diagnosis |
| `cases.csv` | Stores the 30 troubleshooting cases |
| `reviews.csv` | Stores human review information |
| Packet Tracer | Reproduces and verifies network faults |
| GitHub | Source-code version control |
| Streamlit Cloud | Hosts the deployed application |
| Streamlit Secrets | Securely stores the OpenAI API key |

---

## 8. Overall Design Principle

NetSage AI follows the principle:

```text
Evidence
   ↓
AI Reasoning
   +
Deterministic Validation
   ↓
Structured Diagnosis
   ↓
Human Review
   ↓
Packet Tracer Verification
   ↓
Final Troubleshooting Decision
```

The system does **not** allow the AI to automatically modify network configurations. Human oversight remains part of the final troubleshooting workflow.
