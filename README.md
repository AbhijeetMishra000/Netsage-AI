# NetSage AI

Human-in-the-loop AI network troubleshooting assistant.

## Run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Set `OPENAI_API_KEY` before using the real LLM. If unavailable, the application can use the deterministic fallback.

## Folders
- `data/` — dataset and review log
- `ai/` — LLM integration
- `checker/` — deterministic checks
- `dashboard/` — dashboard module
- `prompts/` — AI prompts
- `docs/` — report, architecture, testing, demo and responsible-AI documentation
