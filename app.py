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
