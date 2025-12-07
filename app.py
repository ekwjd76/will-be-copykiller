import streamlit as st
from utils.model_based import model_ai_score

st.set_page_config(page_title="AIlian", page_icon="👾" )

st.title("AIlian 👾")
st.markdown("**‼️AI가 쓴 글인지 확인하기‼️**")

text_input = st.text_area("텍스트를 입력하세요", height=250, placeholder="여기에 문장을 입력하세요...")

if st.button("분석하기"):
    if not text_input.strip():
        st.warning("텍스트를 입력해주세요.")
    else:
        with st.spinner("분석 중..."):
            model_score = model_ai_score(text_input)          # 0~1
            final_score = model_score * 100                   # 퍼센트 변환

        st.subheader("📊 분석 결과")
        st.metric("AI 작성 확률", f"{final_score:.2f}%")

        if final_score > 70:
            st.error("❌ AI가 쓴 글입니다.")
        else:
            st.success("✅ 사람이 쓴 글입니다.")

        st.markdown("---")
        st.caption(f"모델 기반 점수: {model_score:.2f}")
