import streamlit as st

# Streamlit 앱의 제목 설정
st.title('음악에서 찾는 분수')

# 분자와 분모에 대한 선택 옵션 설정
numerator_options = [1, 2, 3]
denominator_options = [2, 4, 8, 16]

# Streamlit 사이드바에 탭 추가
selected_tab = st.sidebar.selectbox("탭을 선택하세요", ["음표와 분수의 관계 이해", "분수를 입력하여 해당 음표의 길이를 확인해보세요", "Google Song Maker로 이동하기"])

# 선택된 탭에 따라 내용 표시
if selected_tab == "음표와 분수의 관계 이해":
    st.title('음표와 분수의 관계 이해')
    st.write("음악에서 음표는 시간의 길이를 나타냅니다.")
    st.write("예를 들어, 4분음표는 1박을 나타내고, 2분음표는 1/2 박을 나타냅니다.")
    st.write("이런 식으로 다른 분수들은 다른 박자를 나타냅니다.")
elif selected_tab == "분수를 입력하여 해당 음표의 길이를 확인해보세요":
    st.title('분수를 입력하여 해당 음표의 길이를 확인해보세요')

    # 분자와 분모 선택
    numerator_input = st.selectbox('분자를 선택하세요', numerator_options)
    denominator_input = st.selectbox('분모를 선택하세요', denominator_options)

    # 분수를 박자로 변환하는 함수
    def fraction_to_duration(numerator, denominator):
        duration = 4 / denominator * numerator  # 4분음표 기준으로 계산
        return duration

    # 입력된 분수를 박자로 변환하여 음표 생성
    if st.button('음표 길이 확인'):
        note_duration = fraction_to_duration(numerator_input, denominator_input)
        st.write(f"선택한 {numerator_input}/{denominator_input} 분수는 {note_duration}분음표에 해당됩니다.")
elif selected_tab == "Google Song Maker로 이동하기":
    st.title('Google Song Maker로 이동하기')
    st.write("Google Song Maker로 이동하려면 아래 링크를 클릭하세요:")
    google_songmaker_link = "https://musiclab.chromeexperiments.com/Song-Maker/"
    st.markdown(f"[Google Song Maker 바로가기]({google_songmaker_link})")
