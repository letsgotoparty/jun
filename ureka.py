import streamlit as st
import pandas as pd

# 맥주 추천 로직
def recommend_beer(beer_data, bitterness, sweetness, alcohol):
    # 각 맥주와 사용자 입력 값 사이의 거리를 계산\
    return 1

# 사용자로부터 입력을 받는 스트림릿 애플리케이션을 생성
st.title('맥주 추천 앱')
st.header('맛 프로필 입력')

bitterness = st.slider('쓴맛 (Bitterness)', 0, 10, 5)
sweetness = st.slider('단맛 (Sweetness)', 0, 10, 5)
alcohol = st.slider('알콜 함량 (Alcohol Content)', 3, 10, 5)

# 사용자 입력을 기반으로 맥주 추천
if st.button('맥주 추천'):
    beer_data = 1
    recommended_beer = recommend_beer(beer_data, bitterness, sweetness, alcohol)
    st.subheader('추천 맥주')
    st.write(recommended_beer)