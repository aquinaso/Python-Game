# 들여쓰기 수정했습니당
import random

num1 = int(input("하나를 선택하세요 : 가위(0), 바위(1), 보(2) :"))
num2 = random.randrange(0, 3)
if num2 == 0:
    print("컴퓨터는 가위를 냈습니다.")
elif num2 == 1:
    print("컴퓨터는 바위를 냈습니다.")
else:
    print("컴퓨터는 보를 냈습니다.")

# Hello Hamster 🐹
if num1 == 0:
    if num2 == 1:
        print("컴퓨터가 이겼습니다")
    elif num2 == 2:
        print("당신이 이겼습니다.")
    else:
        print("비겼습니다.")
elif num1 == 1:
    if num2 == 0:
        print("당신이 이겼습니다.")
    elif num2 == 2:
        print("컴퓨터가 이겼습니다.")
    else:
        print("비겼습니다.")
elif num1 == 2:
    if num2 == 0:
        print("컴퓨터가 이겼습니다.")
    elif num2 == 1:
        print("당신이 이겼습니다.")
    else:
        print("비겼습니다.")
