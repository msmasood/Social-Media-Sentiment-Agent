# Social Media Sentiment & Trend Analysis Agent (Demo)

Demo pipeline for ingesting small social media samples and running sentiment + topic detection.

Quickstart:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/social/sentiment_demo.py
uvicorn src.api.app:app --reload --port 8500
```
