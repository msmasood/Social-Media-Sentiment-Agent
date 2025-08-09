from social.sentiment import analyze_sample
def test_sentiment():
    r = analyze_sample(['I love this','I hate this'])
    assert isinstance(r, list) and len(r)==2
