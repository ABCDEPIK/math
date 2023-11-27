import streamlit as st

# Streamlit 앱의 제목 설정
st.title('음표와 분수 관계 이해하기')

# 음표와 분수 관계 설명
st.write("음표와 분수의 관계를 이해해봅시다.")
st.write("음악에서 음표는 시간의 길이를 나타냅니다.")
st.write("예를 들어, 4분음표는 1박을 나타내고, 2분음표는 1/2 박을 나타냅니다.")
st.write("이런식으로...")
st.write("- 1박은 4분음표")
st.write("- 1/2 박은 2분음표")
st.write("- 1/4 박은 1분음표")
st.write("- 1/8 박은 1/2분음표")
st.write("- 1/16 박은 1/4분음표")
st.write("와 같이 계산됩니다.")

# 사용자로부터 분수를 입력받는 입력 필드 추가
st.write("\n이제 분수를 입력하여 해당 음표의 길이를 확인해보세요.")
numerator_input = st.number_input('분자를 입력하세요', step=1)
denominator_input = st.number_input('분모를 입력하세요', step=1)

# 분수를 박자로 변환하는 함수
def fraction_to_duration(numerator, denominator):
    duration = 4 * numerator / denominator  # 4분음표 기준으로 계산
    return duration

# 입력된 분수를 박자로 변환하여 음표 생성
if st.button('음표 길이 확인'):
    note_duration = fraction_to_duration(numerator_input, denominator_input)
    st.write(f"입력한 {numerator_input}/{denominator_input} 분수는 {note_duration}분음표에 해당됩니다.")
