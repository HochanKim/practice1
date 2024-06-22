import random   # 랜덤 기능 가져오기
# 블랙잭 게임 구현
cardShape = ["하트", "스페이드", "다이아", "크로바"]
cardNumber = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = []   # 초기화
for i in range(52) :    # 0부터 51까지 범위 설정
    deck.append(i)
print(deck)

# 34 모양 // 13
print(34 // 13) # 모양  2 > 다이아
print(34 % 13)  # 숫자  8 > 9개
print(cardShape [34 // 13], cardNumber [34 % 13]) # 34에 대한 카드정보 출력

# deck에 들어있는 모든 카드를 출력
for card in deck :
    print(card, "번 카드 : ", cardShape[card // 13], cardNumber[card % 13])
print()

# 카드 섞기
for i in range(9999) :
    popValue = deck.pop(random.randint(0, 51))
    deck.insert(0, popValue)

for card in deck :
    print(card, "번 카드 : ", cardShape[card // 13], cardNumber[card % 13])
print()

# count로 확인
# for i in range(52) :
#     print(deck.count(i))

play1_deck = []
play2_deck = []

# 각 플레이어가 카드 1장씩 받음
# deck 하나씩 가져와서 play1_deck과 play2_deck에 넣는다.
play1_deck.append(deck.pop())
play2_deck.append(deck.pop())

print("남은 카드 개수 : " + str(len(deck)))
print()

print(play1_deck)
print(play2_deck)
print()

is_play1_flag = True;   # True면 p1은 게임을 계속함
is_play2_flag = True;   # True면 p2은 게임을 계속함


while is_play1_flag or is_play2_flag :   # 카드 받는 작업을 반복적으로 실행
    if is_play1_flag : # 카드 받는 작업이 True일 경우
        p1_input = input("play1님 카드를 받으시겠습니까? 1.Yes 2.No : ")
        if p1_input == '1' :
            play1_deck.append(deck.pop())        # p1 카드 받는 작업
        else :
            is_play1_flag = False
    
    if is_play2_flag : # 카드 받는 작업이 True일 경우
        p2_input = input("play2님 카드를 받으시겠습니까? 1.Yes 2.No : ")
        if p2_input == '1' :
            play2_deck.append(deck.pop())        # p2 카드 받는 작업
        else :
            is_play2_flag = False
print()

play1_sum = 0   # 카드 합계 초기화
play2_sum = 0

# 카드 계산
# play1_sum
for i in play1_deck :   
    i = 0
    if i % 13 == 0 :    # A 카드
        i = 11   # A 카드를 11로 처리
    elif i % 13 <= 9 :
        i = i % 13 + 1
    else :
        i = 10
    play1_sum = play1_sum + i
# A 처리 11 or 1이 된다. 21이 넘어가면 A는 1로 처리, 안넘어가면 11로 처리
for i in play1_deck :
    # 21이 안넘으면
    if play1_sum <= 21 :
        break
    else :  # 21이 넘으면
        if i % 13 == 0 :    # A이면
            play1_sum -= 10
print()

# play2_sum 
for i in play2_deck :
    i = 0
    if i % 13 == 0 :    # A 카드
        i = 11   # A 카드를 11로 처리
    elif i % 13 <= 9 :
        i = i % 13 + 1
    else :
        i = 10
    play2_sum = play2_sum + i
# A 처리 11 or 1이 된다. 21이 넘어가면 A는 1로 처리, 안넘어가면 11로 처리
for i in play2_deck :
    # 21이 안넘으면
    if play2_sum <= 21 :
        break
    else :  # 21이 넘으면
        if i % 13 == 0 :    # A이면
            play2_sum -= 10
print()

print(play1_deck)
print("play1 카드")
for i in play1_deck :
    print(cardShape[i // 13], cardNumber[i % 13], end=" ")
print("총합 :",play1_sum)
print()
print()
print(play2_deck)
print("play2 카드")
for i in play2_deck :
    print(cardShape[i // 13], cardNumber[i % 13], end=" ")
print("총합 :",play2_sum)
print()
print()
print("게임종료")