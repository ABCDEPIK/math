import streamlit as st

# 사이드바에 텍스트와 설명 추가
st.sidebar.title('음표와 분수의 관계 이해')
st.sidebar.write("음악에서 음표는 시간의 길이를 나타냅니다.")
st.sidebar.write("예를 들어, 4분음표는 1박을 나타내고, 2분음표는 1/2 박을 나타냅니다.")
st.sidebar.write("이런 식으로 다른 분수들은 다른 박자를 나타냅니다.")

# 메인 화면에 제목 설정
st.title('분수를 입력하여 해당 음표의 길이를 확인해보세요')

# 사용자로부터 분수를 입력받는 입력 필드 추가
st.write("오른쪽 패널에서 분수를 입력하고, 해당 음표의 길이를 확인해보세요.")
numerator_input = st.sidebar.number_input('분자를 입력하세요', step=1)
denominator_input = st.sidebar.number_input('분모를 입력하세요', step=1)

# 분수를 박자로 변환하는 함수
def fraction_to_duration(numerator, denominator):
    duration = 4 / denominator * numerator  # 4분음표 기준으로 계산
    return duration

# 입력된 분수를 박자로 변환하여 음표 생성
if st.button('음표 길이 확인'):
    note_duration = fraction_to_duration(numerator_input, denominator_input)
    st.write(f"입력한 {numerator_input}/{denominator_input} 분수는 {note_duration}분음표에 해당됩니다.")
