#필요한 모듈들을 부착
import random
import hangman_word
import hangman_pic
#행맨 사진 모듈에서 로고 출력
print(hangman_pic.logo)
#행만 문자 모듈 에서 문자열리스트를 word_list에 선언
word_list = hangman_word.word_list
#유저가 한정된 목숨을 가지고 도전할수 있도록 목숨 갯수 선언
user_life = 6
#랜덤으로 리스트 에서 단어 한개 선택
chosen_word = random.choice(word_list)
#빈칸을 출력하기 위한 공백 리스트 선언
show_list = []
word_length = len(chosen_word)
#선택된 단어의 크기만큼 반복하며 _ 표시
for char in chosen_word:
    #선언된 _ 는 show_list에 추가되며 문자열 만큼 더해짐
    show_list += "_"
#게임을 끝내기 위한 조건 반복문 while에 들어갈 변수 선언
end_game = False
#end_game 이 False일 동안 반복
while not end_game:
    #입력을 대문자로 할수도 있으니 소문자로 전부 변환하여 입력 받는다
    chosen_user1 = input("글자를 입력하세요 : ").lower()
    #선택된 단어의 길이만큼 반복
    for answer in range(word_length):
        #단어가 반복되는 동안 answer 를 chosen_word[]에 추가하여 word에 저장한다
        word = chosen_word[answer]
        #만약 word가 유저가 입력한 것과 동일 하다면
        if word == chosen_user1:
            #show_list리스트에 word값을 입력한다
            show_list[answer] = word
    #조건 검사가 끝나면 남은 갯수 출력
    print(show_list)
    #입력받은글이 컴퓨터가 선정한 글자에 존재하지 않는다면 목숨을 1개 깎고, 목숨이 0이 되면 False를 True로 바꾸어 while을 종료 시켜 끝낸다.
    if chosen_user1 not in chosen_word:
        user_life -= 1
        if user_life == 0:
            end_game = True
            print("정답을 맞추지 못했습니다 ㅠㅠ")
            print(f"정답은 {chosen_word} 입니다.")
    #만약 줄13 show_list에 삽입되었던 _가 전부 유저가 입력한 word로 대체 된다면 프로그램 종료
    if "_" not in show_list:
        end_game = True
        print("전부 맞추는데 성공하였습니다!")
    #행맨 사진 모듈에서 목슴을 표현할수 있는 행맨 이모지 출력
    print(hangman_pic.stages[user_life])
