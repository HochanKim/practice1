# 함수를 이용해서 블랙잭 게임 프로그램 만들기
import random

# 블랙잭 게임 구현
cardShape = ["하트", "스페이드", "다이아", "크로바"]
cardNumber = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = [] 

play1_deck = []
play2_deck = []

is_play1_flag = True    # True면 p1은 게임을 계속함
is_play2_flag = True    # True면 p2은 게임을 계속함

def play_blackjack() :
    while is_play1_flag or is_play2_flag :   # 카드 받는 작업을 반복적으로 실행
        get_card()

def initialize_deck() :
    # 1. 카드 초기화
        # 1-1. 카드 생성
        # 1-2. 카드섞기
    global deck     # 전역변수 선언
    deck = [i for i in range(52)]   # deck을 0부터 51까지 넣기
    # 카드 출력하기
    # 카드 섞기
    random.shuffle(deck)

def get_card() :
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

def play_game() :
    # 2. 카드 받기
    # 3. 카드 점수 계산
    # 4. 승패 확인
    pass

