from itertools import product

def countMoney(users, emoticons, sales): #세일에 따른 구독자와 판매액 계산을 해주는 함수
    cnt_people = 0 #구독자 수
    cnt_money = 0 #판매액
    for buy, maximun_money in users:
        cnt = 0 #구매할 예정의 총액
        for i in range(len(emoticons)):
            if sales[i] >= buy:
                cnt += (100-sales[i]) * (emoticons[i] // 100)
        if cnt >= maximun_money: #최대 비용이 초과라면 구독
            cnt_people += 1
        else: #최대 비용보다 작다면 바로 사버리기~
            cnt_money += cnt
    
    return cnt_people, cnt_money
        
def solution(users, emoticons):
    max_people = 0 #최대 구독자 수
    max_money = 0 #최대 구독자 수일 때 최대 판매액
    
    #최대 구독자와 최대 반매자를 알러 탐색 시작~
    for sales in product([10, 20, 30, 40], repeat = len(emoticons)):
        now_people, now_money = countMoney(users, emoticons, sales)
        #조건 1. 구독자 수가 저장한 구독자 수보다 더 클 경우
        if max_people < now_people:
            max_people = now_people
            max_money = now_money
        #조건 2. 구독자 수는 같지만 판매액이 더 클 경우
        elif max_people == now_people and max_money < now_money:
            max_money = now_money
        
    return [max_people, max_money]

#아래는 테스트 케이스를 실행하기 위한 코드이다.
#크게 특별한것은 없다.
test_case1_user = [[40, 10000], [25, 10000]]
test_case1_emoticons = [7000, 9000]
test_case1_answer = [1, 5400]

test_case2_user = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
test_case2_emoticons = [1300, 1500, 1600, 4900]
test_case2_answer = [4, 13860]

print('test1 : ',solution(test_case1_user, test_case1_emoticons) == test_case1_answer)
print('test2 : ',solution(test_case2_user, test_case2_emoticons) == test_case2_answer)
