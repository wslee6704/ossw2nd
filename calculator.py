import re  # 한글 감지를 위한 모듈

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

# 숫자 입력 함수 (한글 입력 방지)
def get_number(prompt):
    while True:
        value = input(prompt)
        if re.search("[가-힣]", value):  # 한글이 포함되었는지 검사
            print("❌ 숫자만 입력하세요!")
            continue
        try:
            return float(value)  # 숫자로 변환
        except ValueError:
            print("❌ 유효한 숫자를 입력하세요!")

if __name__ == "__main__":
    # 사용자 입력
    input1 = get_number("\n첫 번째 숫자를 입력하세요: ")

    while True:
        act = input("\n원하는 사칙연산 기호를 선택하세요 (+, -, *, /): ")
        if act in ["+", "-", "*", "/"]:
            break
        print("❌ 잘못된 연산자입니다. 다시 입력하세요!")

    input2 = get_number("\n두 번째 숫자를 입력하세요: ")

    # 연산 수행
    if act == "+":
        result = plus(input1, input2)
    elif act == "-":
        result = minus(input1, input2)
    elif act == "*":
        result = mul(input1, input2)
    elif act == "/":
        result = divide(input1, input2)

    print(f"\n✅ 결과: {result}")
