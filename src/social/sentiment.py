from typing import List
def analyze_sample(texts: List[str]):
    # trivial sentiment scoring: positive if 'love' in text else negative if 'terrible'
    out = []
    for t in texts:
        score = 0.0
        if 'love' in t.lower(): score = 0.9
        if 'terrible' in t.lower(): score = -0.8
        out.append({'text':t,'score':score})
    return out
