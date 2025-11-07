import argparse
from utils.feature_based import feature_ai_score
from utils.model_based import model_ai_score

def main():
    parser = argparse.ArgumentParser(description="AI Text Detector")
    parser.add_argument("--file", type=str, help="분석할 텍스트 파일 경로")
    parser.add_argument("--text", type=str, help="직접 입력할 문장")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        print("텍스트 입력이 필요합니다 (--file 또는 --text)")
        return

    # 1️⃣ 통계 기반 점수
    feature_score = feature_ai_score(text)
    # 2️⃣ AI 모델 기반 점수
    model_score = model_ai_score(text)
    # 3️⃣ 통합 결과
    final_score = (feature_score + model_score * 100) / 2

    print(f"\nAI 작성 가능성: {final_score:.2f}%")
    if final_score > 60:
        print("→ ⚠️ AI가 작성했을 확률이 높습니다.")
    elif final_score > 40:
        print("→ 🤔 중간 정도로 애매합니다.")
    else:
        print("→ ✅ 사람이 작성했을 가능성이 높습니다.")

if __name__ == "__main__":
    main()