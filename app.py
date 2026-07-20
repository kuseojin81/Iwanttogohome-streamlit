import streamlit as st

st.markdown("# 앱 UI 만들기")
user_id = st.text_input("이름", placeholder="이름")
ai_model = st.radio("나이", ["1", "2", "3"], horizontal=True)
age = st.number_input("반", min_value=1, max_value=100, value=1)
ai_speed = st.select_slider("난이도",options=["매우 쉬움", "쉬움", "보통", "어려움", "매우 어려움"],value="보통")
creativity = st.slider("점수", 0, 100, 50)
question = st.text_area("소감", placeholder="소감입니다.")

       
 
