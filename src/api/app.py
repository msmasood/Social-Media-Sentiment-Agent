from fastapi import FastAPI
from social.sentiment import analyze_sample
app = FastAPI(title='Social Media Sentiment Demo API')
@app.post('/analyze')
def analyze(texts: list):
    return {'status':'ok','results': analyze_sample(texts)}
