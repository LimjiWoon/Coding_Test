#입력값
test_one = "1 2"
#원하는 출력은 3

#python용 코드
a, b = map(int, test_one.split(" "))

#baek-joon용 코드
#a, b = map(int, input().split(" "))

print(a+b)