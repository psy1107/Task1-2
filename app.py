import streamlit as st
import pandas as pd
import numpy as np

st.title("Team Project Streamlit Dashboard")

st.write("이곳에 Task 3: 차트 그리기 기능을 구현합니다.")

st.header("Line Chart")
df = pd.DataFrame(np.random.randn(20, 3), columns=['a','b','c'])
st.line_chart(df)

st.header("Bar Chart")
st.bar_chart(df)

st.header("Area Chart")
st.area_chart(df)

st.header("Task 4: 인터랙티브 필터")
st.write("데이터를 조건에 따라 필터링해보는 예제입니다.")

# 예시 데이터 (상품/카테고리/매출)
data = {
    "상품": ["A", "B", "C", "D", "E", "F"],
    "카테고리": ["식품", "식품", "의류", "의류", "전자", "전자"],
    "매출": [10, 25, 30, 15, 40, 22]
}
df = pd.DataFrame(data)

st.subheader("원본 데이터")
st.dataframe(df)

# --- 사이드바 필터 ---
st.sidebar.header("필터 설정")

# 카테고리 선택 필터
selected_category = st.sidebar.multiselect(
    "카테고리 선택",
    options=df["카테고리"].unique(),
    default=list(df["카테고리"].unique())
)

# 매출 최소값 슬라이더
min_sales = st.sidebar.slider(
    "최소 매출 선택",
    min_value=int(df["매출"].min()),
    max_value=int(df["매출"].max()),
    value=int(df["매출"].min())
)

# --- 필터 적용 ---
filtered_df = df[
    (df["카테고리"].isin(selected_category)) &
    (df["매출"] >= min_sales)
]

st.subheader("필터링된 결과")
st.dataframe(filtered_df)

st.subheader("필터링된 결과 막대 그래프")
if not filtered_df.empty:
    chart_df = filtered_df.set_index("상품")["매출"]
    st.bar_chart(chart_df)
else:
    st.info("조건에 맞는 데이터가 없습니다. 필터를 조정해 보세요.")
