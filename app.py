import streamlit as st
from utils.feature_based import feature_ai_score
from utils.model_based import model_ai_score

st.set_page_config(page_title="AI Text Detector", page_icon="🤖")

st.title("🧠 AI Text Detector")
st.markdown("**입력한 글이 AI가 작성한 것인지 예측하는 웹 도구입니다.**")

text_input = st.text_area("✍️ 텍스트를 입력하세요:", height=250, placeholder="여기에 글을 입력하세요...")

if st.button("분석하기 🚀"):

    if not text_input.strip():
        st.warning("텍스트를 입력해주세요.")
    else:
        with st.spinner("AI가 분석 중입니다..."):
            feature_score = feature_ai_score(text_input)
            model_score = model_ai_score(text_input) * 100
            final_score = (feature_score + model_score) / 2

        st.subheader("📊 분석 결과")
        st.metric("AI 작성 확률", f"{final_score:.2f}%")

        if final_score > 60:
            st.error("⚠️ AI가 작성했을 가능성이 높습니다.")
        elif final_score > 40:
            st.warning("🤔 애매합니다. 일부 문장은 AI 느낌이 납니다.")
        else:
            st.success("✅ 사람이 작성했을 가능성이 높습니다.")

        st.markdown("---")
        st.caption(f"통계 기반 점수: {feature_score:.2f} | 모델 기반 점수: {model_score:.2f}")