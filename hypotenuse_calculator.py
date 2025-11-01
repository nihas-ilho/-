import math

def hypotenuse(a, b):
    """직각삼각형의 두변 a, b를 받아 빗변 길이를 반환."""
    return math.hypot(a, b) 

if __name__ == "__main__":
    # 사용자 입력 받기

    a = float(input("가로 길이를 입력하세요 (m): "))
    b = float(input("세로 길이를 입력하세요 (m): "))

    c = hypotenuse(a, b)
    print(f"빗변의 길이는 {c:.2f} m 입니다.")   
    