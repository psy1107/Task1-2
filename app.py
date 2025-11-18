import streamlit as st
import pandas as pd

# --- 제목 ---
st.title("🧊 Penguins 데이터 분석 앱")

# --- Task 1: 기본 UI 컴포넌트 ---
st.header("1️⃣ 기본 UI 컴포넌트")

name = st.text_input("이름을 입력하세요")
age = st.slider("나이를 선택하세요", 1, 100, 20)
gender = st.selectbox("성별을 선택하세요", ["남성", "여성", "기타"])
hobby = st.checkbox("나는 펭귄 데이터를 좋아한다")

if st.button("제출하기"):
    st.write("### 입력한 정보")
    st.write(f"- 이름: {name}")
    st.write(f"- 나이: {age}")
    st.write(f"- 성별: {gender}")
    st.write(f"- 펭귄 데이터 좋아함: {hobby}")

# --- Task 2: 데이터 표시하기 ---
st.header("2️⃣ 데이터 표시하기 (DataFrame & 통계 정보)")

# CSV 파일 읽기
df = pd.read_csv("penguins.csv")

st.subheader("📄 데이터프레임 미리보기")
st.dataframe(df)

st.subheader("📊 기본 통계 정보")
st.write(df.describe())
