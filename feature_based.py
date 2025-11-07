import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt', quiet=True)

def feature_ai_score(text: str) -> float:
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    
    if not words or not sentences:
        return 50.0

    avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)
    lexical_diversity = len(set(words)) / len(words)

    # 문체 점수 계산 (단순 모델)
    score = (1 - lexical_diversity) * 50 + max(avg_sentence_length - 15, 0) * 2
    return min(max(score, 0), 100)