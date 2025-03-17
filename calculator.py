# 사칙연산 함수 정의
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

if __name__ == "__main__":
    # 사용자 입력
    print("\n첫 번째 숫자를 입력하세요.")
    input1 = float(input("입력: "))  # 숫자로 변환

    print("\n원하는 사칙연산 기호 중 하나를 선택하세요. (+, -, *, /)")
    act = input("기호: ")

    print("\n두 번째 숫자를 입력하세요.")
    input2 = float(input("입력: "))  # 숫자로 변환

    # 연산 수행
    if act == "+":
        result = plus(input1, input2)
    elif act == "-":
        result = minus(input1, input2)
    elif act == "*":
        result = mul(input1, input2)
    elif act == "/":
        result = divide(input1, input2)
    else:
        result = "잘못된 연산자 입력입니다."

    print(f"\n사칙연산 결과는 {result}입니다.")
