import streamlit as st
import openai
import random

# OpenAI API 키 설정
openai.api_key = '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'

def recommend_beer(selected_intensity, selected_calories, selected_flavor, selected_origin):
    # 맥주 목록 가져오기
    beers = get_beer_list()

    # 사용자가 선택한 조건에 맞게 맥주 추천
    filtered_beers = [beer for beer in beers
                      if beer["도수"] == selected_intensity
                      and beer["칼로리"] == selected_calories
                      and beer["맛"] == selected_flavor
                      and beer["생산지"] == selected_origin]

    # 조건에 맞는 맥주가 없을 때 OpenAI로 추천 생성
    if not filtered_beers:
        prompt = f"맥주 추천: 도수 {selected_intensity}, 칼로리 {selected_calories}, 맛 {selected_flavor}, 생산지 {selected_origin}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,  # 토큰 수를 조정할 수 있습니다.
            temperature=0.7
        )

        # OpenAI에서 생성된 텍스트 추천 반환
        recommended_text = response.choices[0].text.strip()

        # 임의의 맥주를 선택하여 결과를 생성
        random_beer = random.choice(beers)
        recommended_beer = f"{random_beer['name']}를 추천합니다!"

        return recommended_beer

    else:
        # 조건에 맞는 맥주가 있을 때는 무작위로 선택하여 "~~맥주를 추천합니다"로 반환
        recommended_beer = random.choice(filtered_beers)
        return f"{recommended_beer['name']}를 추천합니다!"
    
def get_beer_list():
    # 맥주 목록
    beers = [
        {"name": "카스", "도수": "보통", "칼로리": "높음", "맛": "쓴맛", "생산지": "한국"},
        {"name": "테라", "도수": "보통", "칼로리": "보통", "맛": "달콤한맛", "생산지": "한국"},
        {"name": "블랑", "도수": "높음", "칼로리": "높음", "맛": "고소한맛", "생산지": "독일"},
        {"name": "켈리", "도수": "낮음", "칼로리": "보통", "맛": "쓴맛", "생산지": "한국"},
        {"name": "맥스", "도수": "낮음", "칼로리": "보통", "맛": "달콤한맛", "생산지": "한국"},
        {"name": "한맥", "도수": "낮음", "칼로리": "낮음", "맛": "쓴맛", "생산지": "한국"},
        {"name": "버드와이저", "도수": "보통", "칼로리": "낮음", "맛": "쓴맛", "생산지": "한국"},
        {"name": "곰표", "도수": "보통", "칼로리": "낮음", "맛": "쓴맛", "생산지": "한국"},
        {"name": "클라우드", "도수": "낮음", "칼로리": "높음", "맛": "쓴맛", "생산지": "한국"},
        {"name": "하이네킨", "도수": "낮음", "칼로리": "낮음", "맛": "달콤한맛", "생산지": "독일"},
        {"name": "카스라이트", "도수": "낮음", "칼로리": "낮음", "맛": "고소한맛", "생산지": "한국"},
        {"name": "스텔라", "도수": "높음", "칼로리": "보통", "맛": "쓴맛", "생산지": "일본"},
        {"name": "오비라거", "도수": "보통", "칼로리": "보통", "맛": "쓴맛", "생산지": "한국"},
        {"name": "칭따오", "도수": "보통", "칼로리": "높음", "맛": "고소한맛", "생산지": "중국"},
        {"name": "타이거", "도수": "낮음", "칼로리": "보통", "맛": "달콤한맛", "생산지": "일본"},
        {"name": "구스아일랜드", "도수": "보통", "칼로리": "보통", "맛": "쓴맛", "생산지": "독일"},
        {"name": "필굿", "도수": "낮음","칼로리": "보통", "맛": "쓴맛", "생산지": "한국"},
        {"name": "버터맥주", "도수": "낮음", "칼로리": "낮음", "맛": "고소한맛", "생산지": "독일"},
        {"name": "밀러", "도수": "보통", "칼로리": "높음", "맛": "쓴맛", "생산지": "일본"},
        {"name": "코젤", "도수": "높음", "칼로리": "높음", "맛": "고소한맛", "생산지": "독일"},
        {"name": "순하리", "도수": "낮음", "칼로리": "낮음", "맛": "달콤한맛", "생산지": "한국"}
    ]
    return beers

def main():
    st.title("맥주 추천 앱")

    # 사용자 입력값 받기
    도수 = st.selectbox("도수", ["낮음", "보통", "높음"])
    칼로리 = st.selectbox("칼로리", ["낮음", "보통", "높음"])
    맛 = st.selectbox("맛", ["쓴맛", "달콤한맛", "고소한맛"])
    생산지 = st.selectbox("생산지", ["한국" , "독일", "일본"])

    if st.button('시작'):
        recommendbeer = recommend_beer(도수, 칼로리, 맛, 생산지)
        st.subheader('추천 맥주')
        st.write(recommendbeer)

if __name__ == "__main__":
    main()
