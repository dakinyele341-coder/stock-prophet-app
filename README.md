# Stock Prophet App

Simple Streamlit app that performs sentiment analysis on input text. The app will try to use a Hugging Face `sentiment-analysis` pipeline if `transformers` and `torch` are installed; otherwise it falls back to a small rule-based classifier.

Quick start

1. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Run locally:

```bash
streamlit run app.py
```

Deployment

- For Streamlit Community Cloud: push this repository to GitHub and connect the repo in Streamlit Cloud. Use the `requirements.txt` file for dependencies. Note: the Hugging Face model download may be large — consider using a smaller model or the HF Inference API for production.
- For Render / Cloud Run / Docker-based deploys: consider adding a `Dockerfile` or use the platform's build settings.

If you want, I can create the GitHub repository and push this code for you (requires `gh` CLI auth). 
# stock-prophet-app