print("Welcome to fruit shop!")
print('Mr.프룻맨의 과일가게에 오신 것을  환영합니다!')
print('이 가게는 미국인 프룻맨이 운영하는 과일가게입니다.')
print("Mr.프룻맨은 한국에 온지 얼마 안되어 한국말을 하지 못합니다.")
print("Mr.프룻맨이 알아들을 수 있도록 영어로 과일을 주문해주세요!")
print('')
print('[규칙]')
print('1.랜덤으로 나오는 10개의 과일을 영어로 말해야 과일을 구매할 수 있습니다.')
print('2.입력을 할 때는 과일단어만을 단수로 입력해야합니다.')
print('3.하나의 단어를 맞힐때마다 15점이 부여됩니다. ')
print('4.총합 점수가 100점 이상 되면 게임이 종료되고 과일을 구매할 수 있습니다.')
print('')
print('')
print('게임 시작!')
print('')
print('')
print("Mr.프룻맨: Welcome to fruit shop!")
print("Mr.프룻맨: What do you need?")
import random

words_dict = {
    "사과": "apple",
    "포도": "grape",
    "오렌지": "orange",
    "복숭아": "peach",
    "망고": "mango",
    "파인애플": "pineapple",
    "딸기": "strawberry",
    "수박": "watermelon",
    "용과": "dragonfruit",
    "두리안": "durian"
}
score_sum = 0


words = [w for w in words_dict]
random.shuffle(words)

for w in words:
  answer = input(f'{w}을(를) 구매하자! 나: Umm.. I am looking for..->').strip()
  english = words_dict[w]
  if answer.lower() == english.lower():
    print("Mr.프룻맨: Oh! that's good!")
    score_sum = score_sum +15

  else:
    print("Mr.프룻맨: What the..?")

print(f'당신의 점수는 {score_sum}점 입니다!')

if score_sum >= 100 :
  print("Mr.프룻맨: Thank you for purchasing the fruit!")
if score_sum <= 45 :
  print("Mr.프룻맨: No... I don't understand you'r saying at all...")
