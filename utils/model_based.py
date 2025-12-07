"""
model_based.py — fakespot-ai 모델 기반 AI 탐지기
"""

from transformers import pipeline
import torch

MODEL_NAME = "openai-community/roberta-base-openai-detector"
DEVICE = 0 if torch.cuda.is_available() else -1

# 모델 로드
try:
    ai_detector = pipeline(
        "text-classification",
        model=MODEL_NAME,
        device=DEVICE,
        #truncation=True
    )
    print(f"✅ Loaded model: {MODEL_NAME} (device={DEVICE})")
except Exception as e:
    print(f"⚠️ 모델 로드 실패: {e}")
    ai_detector = None

def model_ai_score(text: str) -> float:
    global ai_detector

    if ai_detector is None:
        return 0.5
    print("MODEL_DEBUG:", ai_detector("테스트")[0])

    try:
        snippet = text.strip()
        if len(snippet) > 1024:
            snippet = snippet[:1024]

        result = ai_detector(snippet)[0]
        label = result["label"]
        score = float(result["score"])

        # fakespot-ai 모델 라벨:
        #   AI-GENERATED     → AI 확률 score
        #   HUMAN-WRITTEN    → 사람이 쓴 글 → 1 - score
        if label == "Fake":
            ai_score = score
        elif label == "Real":
            ai_score = 1.0 - score
        else:
            ai_score = 0.5

        return max(0.0, min(1.0, ai_score))

    except Exception as e:
        print("⚠️ 모델 예측 오류:", e)
        return 0.5
