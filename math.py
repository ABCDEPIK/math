import streamlit as st

# Streamlit 앱의 제목 설정
st.title('분수와 박자를 이용한 간단한 작곡 프로그램')

# 사용자로부터 분수를 입력받는 입력 필드 추가
st.write("음표를 생성할 분수를 입력해주세요.")
numerator_input = st.number_input('분자를 입력하세요', step=1)
denominator_input = st.number_input('분모를 입력하세요', step=1)

# 분수를 박자로 변환하는 함수
def fraction_to_duration(numerator, denominator):
    duration = 4 * numerator / denominator  # 4분음표 기준으로 계산
    return duration

# 입력된 분수를 박자로 변환하여 음표 생성
if st.button('음표 생성'):
    note_duration = fraction_to_duration(numerator_input, denominator_input)
    st.write(f"생성된 음표의 박자: {note_duration}분음표")

    # 여기에 음표 생성 및 재생하는 코드 추가 가능
    # 예를 들어, MIDI 파일 생성 또는 음악 라이브러리를 이용하여 소리 출력 등을 구현할 수 있습니다.
