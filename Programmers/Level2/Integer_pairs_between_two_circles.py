#프로그래머스 코딩테스트 연습 - 두 원 사이의 정수의 쌍 구하기 문제다
#문제 출처: https://school.programmers.co.kr/learn/courses/30/lessons/181187

#대각선의 길이를 구하는 방법
#피타고라스의 정리 a^2 + b^2 = c^2 을 변형해서 이용하자
#4분면 중 하나에서 x축 값을 기준으로 y의 길이는 위 식을 변형하면 이렇다
#b^2 = c^2 - a^2 이를 이용하자

def solution(r1, r2):
    cnt = 0
    for x in range(1, r2+1):
        r2_y = (r2**2 - x**2)**0.5 # 변하는 값 x마다 계산할 y의 높이
        r1_y = (r1**2 - x**2)**0.5 # 위와 동일, 기준이 r1임
        if x >= r1: #지정한 x좌표가 r1의 반지름보다 커질 경우 -> 그냥 바로 계산
            cnt += int(r2_y) + 1 # +1은 x축 자체도 포함시킴
        elif int(r2_y) == r2_y or int(r1_y) == r1_y: #원 위에 점이 있을 경우
            #해당 점을 기준으로 거리를 구해 점의 갯수를 세면 된다.
            cnt += int(r2_y - r1_y) + 1
        elif r2_y - r1_y > 1: #y축의 차이가 1보다 켜야 점이 존재가능
            cnt += int(r2_y) - int(r1_y)
            
    return cnt*4

#위의 조건에서 r1은 r2보다 무조건 작아야하고 r1,r2는 무조건 정수라는 조건이 존재한다.
print(solution(2,3))
