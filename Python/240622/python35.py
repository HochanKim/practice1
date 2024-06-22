import random


def initialize_deck() :
    for i in range(52):
        deck.append(i)
    print(deck)


    # 34  모양 // 13
    print(34//13)  #모양  2
    print(34%13)    #숫자 8
    print(cardShape[34//13] , cardNumber[34%13]) #34에 대한 카드정


    #deck에 들어 있는 모든 카드를 출력
    for card in deck:
        print(card,"번 카드 :", cardShape[card//13],cardNumber[card%13])


    #카드 섞기

    for i in range(9999):

        popValue=deck.pop(random.randint(0,51))

        deck.insert(0,popValue)


    for card in deck:

        print(card,"번 카드 :", cardShape[card//13],cardNumber[card%13])


def play_blackjack() :
    while is_play1_flag or is_play2_flag :

        play1_sum=0
        play2_sum=0

        #카드 받는 작업

        if is_play1_flag :
            p1_input=input("play1님 카드를 받으시겠습니까?1.yes 2.no")

            if p1_input=='1':
                play1_deck.append(deck.pop())
            else:
                is_play1_flag=False

                

        if is_play2_flag :
            p2_input=input("play2님 카드를 받으시겠습니까?1.yes 2.no")

            if p2_input=='1':
                play2_deck.append(deck.pop())

            else:
                is_play2_flag=False

        

        #카드 계산
        #play1_sum  

        for i in play1_deck:
            cardNum=0
            if i%13==0: #A
                cardNum=11 #A를 11처리
            elif i%13 <=9 :
                cardNum=i%13+1
            else:
                cardNum=10

            play1_sum=play1_sum+cardNum

    #A 처리  11 or 1 이된다.  21이 넘어가면 A는 1로처리 안넘어가면 11로 처리

        for i in play1_deck:
            #21이 안넘으면
            if play1_sum <=21:
                break

            else:    #21이 넘으면
                if i%13==0 : #A이면
                    play1_sum=play1_sum-10

        #최종적으로 play1의 점수가 21초과되면 게임에서 짐
        if play1_sum >21 :
            result_value="play2 승리"
            break

        #play2_sum  
        for i in play2_deck:
            cardNum=0
            if i%13==0: #A
                cardNum=11 #A를 1처리
            elif i%13 <=9 :
                cardNum=i%13+1

            else:
                cardNum=10

            play2_sum=play2_sum+cardNum

        #A 처리  11 or 1 이된다.  21이 넘어가면 A는 1로처리 안넘어가면 11로 처리
        for i in play2_deck:
            #21이 안넘으면
            if play2_sum <=21:
                break
            else:    #21이 넘으면
                if i%13==0 : #A이면
                    play2_sum=play2_sum-10            
        if play2_sum >21 :
            result_value="play1 승리"
            break

        # print(play1_deck)      
        print("play1 카드")

        for i in play1_deck:
            print(cardShape[i//13],cardNumber[i%13],end=" ")
        print("총합 :",play1_sum)    

        #print(play2_deck) 
        print("play2 카드")  

        for i in play2_deck:
            print(cardShape[i//13],cardNumber[i%13],end=" ")
        print("총합 :",play2_sum) 

     
        #승패 결과 값

        if play1_sum >play2_sum:
            result_value="play1 승리"
        elif play2_sum>play1_sum:
            result_value="play2 승리"
        else:
            result_value="무승부"
        print("중간결과:",result_value)                


def play_result() :
    print("최종결과:",result_value)    

    # print(play1_deck)      
    print("play1 카드")
    for i in play1_deck:
        print(cardShape[i//13],cardNumber[i%13],end=" ")

    #print(play2_deck) 
    print("play2 카드")  
    for i in play2_deck:
        print(cardShape[i//13],cardNumber[i%13],end=" ")
    print("게임 종료")


cardShape=["하트","스페이드","다이아","크로바"]
cardNumber=["A","2","3","4","5","6","7","8","9","10","j","q","k"]
deck = []


play1_deck = []
play2_deck = []

is_play1_flag=True; #True면 p1은 게임을 계속함
is_play2_flag=True; #True면 p2은 게임을 계속함

play1_sum=0
play2_sum=0

result_value="무승부"

# 카드 초기화 하기
def play_game() :
    initialize_deck()
    play_blackjack()
    play_result()