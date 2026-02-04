from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction

def bleu_score(actual, predicted):
    smooth = SmoothingFunction().method4
    return corpus_bleu(actual, predicted, smoothing_function=smooth)
