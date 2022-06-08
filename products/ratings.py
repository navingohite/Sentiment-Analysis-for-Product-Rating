import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def rating_analysis(input_txt: str):
    s = SentimentIntensityAnalyzer()
    score = s.polarity_scores(input_txt)

    print(input_txt)
    print(score)

    if score["neg"] < .1 and score["pos"] > .7:
        return 5, 0
    elif score["neg"] < .2 and score["pos"] > .6:
        return 4, 1
    elif score["neg"] < .3 and score["pos"] > .5:
        return 4, 0
    elif score["neg"] < .3 or score["pos"] > .4:
        return 3, 1
    elif score["neg"] < .4 or score["pos"] > .3:
        return 3, 0
    elif score["neg"] < .6 or score["pos"] > .2:
        return 2, 0
    else:
        return 1, 0