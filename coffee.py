print("코드덤 커피 자판기\n 1: 아메리카노  1,800원\n 2: 카페라떼  2,700원\n 3:핫초코  2,300원")

print(f" 커피 종류를 선택하세요. 번호 입력 >>>> ")
a = int(input())

print(f"몇 잔을 드릴까요? >>>> ")
b = int(input())


c = 0
if int(a) == 1:
    c = 1800*b
elif int(a) == 2:
    c = 2700*b
else:
    c = 2300*b


print(f"총 금액 {c}입니다. 돈을 투입해주세요. >>>> ")
d = int(input())

e = d-c
print(f" {d}을 받았습다. 거스름돈은 {e}입니다.")
