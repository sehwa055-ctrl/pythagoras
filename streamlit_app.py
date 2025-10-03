
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import font_manager, rc
import os

# NanumGothic 폰트 경로 지정
font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'NanumGothic-Regular.ttf')
if os.path.exists(font_path):
    font_manager.fontManager.addfont(font_path)
    rc('font', family='NanumGothic')

# 삼각형의 변 입력
st.title("삼각형 판별기 (피타고라스의 정리)")

st.write("각 변의 길이 a, b, c를 입력하세요. (자연수)")

a = st.number_input("변 a", min_value=1, step=1)
b = st.number_input("변 b", min_value=1, step=1)
c = st.number_input("변 c", min_value=1, step=1)

# 삼각형이 만들어지는지 확인
sides = sorted([a, b, c])  # sides[2]가 가장 긴 변
is_triangle = sides[0] + sides[1] > sides[2]

if st.button("삼각형 판별하기"):
    if not is_triangle:
        st.error("입력한 값으로는 삼각형을 만들 수 없습니다.")
    else:
        # 피타고라스의 정리로 삼각형 종류 판별
        a2, b2, c2 = sides[0]**2, sides[1]**2, sides[2]**2
        if a2 + b2 == c2:
            st.success("직각삼각형입니다. (a² + b² = c²)")
        elif a2 + b2 > c2:
            st.info("예각삼각형입니다. (a² + b² > c²)")
        else:
            st.warning("둔각삼각형입니다. (a² + b² < c²)")

        # 삼각형 그래프 그리기
        # 변의 길이: sides[0]=a, sides[1]=b, sides[2]=c (c가 가장 긴 변)
        # 삼각형의 한 꼭짓점을 (0,0), 두 번째 꼭짓점을 (a,0), 세 번째 꼭짓점의 좌표를 계산
        a, b, c = sides[0], sides[1], sides[2]
        # 두 꼭짓점: (0,0), (a,0)
        # 세 번째 꼭짓점: (x, y)
        # x = (a^2 + c^2 - b^2) / (2a)
        # y = sqrt(c^2 - x^2)
        try:
            x = (a**2 + c**2 - b**2) / (2*a)
            y = np.sqrt(max(c**2 - x**2, 0))
            pts = np.array([[0,0], [a,0], [x,y], [0,0]])
            fig, ax = plt.subplots()
            ax.plot(pts[:,0], pts[:,1], 'bo-')
            ax.set_aspect('equal')
            ax.set_title('입력값으로 만들어진 삼각형')
            ax.grid(True)
            st.pyplot(fig)
        except Exception as e:
            st.error(f"그래프를 그릴 수 없습니다: {e}")
