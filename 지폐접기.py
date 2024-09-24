def solution(wallet, bill):
    '''
    규칙
    1. 지폐의 긴 쪽을 반으로 접습니다.
    2. 접기 전 길이가 **홀수**이면, 소수점 이하는 버립니다. 즉, `floor(길이 / 2)`를 적용합니다.
    3. 지폐를 접어서 지갑에 들어갈 수 있는 크기(가로, 세로)보다 작아질 때까지 접습니다.
    4. 접힌 상태에서 90도 회전하여 지갑에 넣을 수도 있습니다.
    wallet = [가로,세로]
    bill = [가로, 세로]

    해결 방법
    1. wallet 보다 bill이 크다면
    2. 배열 내용중 긴 쪽을 반으로 접는다.
    3. 1,2를 반복 하며 길지 않다면 리턴
    ※ 방법 1. 가로 세로 바꿔서도 진행 횟수 적은걸 리턴
      방법 2. wallet보다 bill이 큰걸 체크 할 때 가로 세로 바꿔서도 확인
    '''
    # 방법 2
    # 조건 지갑의 가로가 지폐의 가로보다 작거나 지갑의 세로가 지폐의 세로보다 작으면 (지폐의 가로 세로가 바뀌어도 된다.)
    def check_count(bill_):
        count = 0
        while wallet[0] < bill_[0] or wallet[1] < bill_[1]:
            if(bill_[0]>bill_[1]):
                bill_[0] //= 2
            elif(bill_[1]>bill_[0]):
                bill_[1] //= 2
            count+=1
        return count

    no_rotate=check_count(bill[:])
    rotate = check_count(bill[::-1])
    return min(no_rotate, rotate)



