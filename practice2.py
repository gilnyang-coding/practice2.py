menu = {"우유", "커피", "주스"}
print(menu,type(menu))
#자료 형태 바꾸기기
menu=list(menu)
print(menu,type(menu))

menu=tuple(menu)
print(menu,type(menu))

menu=set(menu)
print(menu,type(menu))

#if
weather="맑음"
if weather=="비":
    print("우산을 챙기세요") #만약 비가 아니라면 아무것도 출력되지 않는다.
elif weather=="미세먼지": #elif를 쓰기도 한다.
    print("미스크를 챙기세요.")
else:
    print("준비물은 필요 없어요.")

#사람의 값을 기다리는 input
# weather=input("오늘 날씨는 어떄요?")
# if weather=="비":
#     print("우산을 챙기세요") #만약 비가 아니라면 아무것도 출력되지 않는다.
# elif weather=="미세먼지": 
#     print("미스크를 챙기세요.")
# else:
#     print("준비물은 필요 없어요.")
# # 두 가지 경우
# weather="눈"
# if weather=="비" or "눈":
#     print("우산을 챙기세요.")
# temp=int(input("오늘 날씨 몇 도예요?"))
# if temp>=30:
#     print("너무 덥네요. 나가지 말아요")
# elif temp<30 and temp>10:
#     print("날씨 좋네요. 나가 놀아요")
# elif temp<=10 and temp>0: #또는 바로 0<temp<10으로 쓸 수 있다.
#     print("쌀쌀하네요. 외투를 챙겨요.")
# else:
#     print("너무 추워요. 나가지 말아요.")

#for (반복문) 반복 횟수가 명확할 때 사용됩니다. 리스트, 튜플, 문자열 같은 시퀀스 자료형을 순회할 때 많이 사용하죠.
print("대기번호: 1")
print("대기번호: 2")
print("대기번호: 3")
print("대기번호: 4") #이는 너무 번거롭다 따라서 for를 쓴다.
for waiting in[1,2,3,4,]:
    print("대기번호:{0}".format(waiting))


for waiting in range(1,6): #또는 range(5), 선택이 :이고 이건,이다. 또한 (x,y)는 y이전까지인 거 알지??
    print("대기번호:{0}".format(waiting))
starbucks=["아이언맨", "토르", "헐크"]
for customers in starbucks:
    print("{0}님 커피 나왔습니다.".format(customers))

#while (조건을 만족한다면 계속 반복) 반복 횟수가 명확하지 않거나 조건에 따라 반복을 멈춰야 할 때 사용됩니다. 무한 루프를 생성하거나, 특정 조건을 만족할 때까지 반복해야 하는 경우에 적합합니다.
# customers="토르"
# 횟수= 5
# while 횟수>=1:
#     print("{0}님, 커피 나왔습니다. {1}번 남았어요.".format(customers,횟수))
#     횟수-=1
# if 횟수<1:
#     print("커피는 폐기 처리되었습니다.")

# customers="토르"
# index=1
# while True: #무한 루프
#     print("{0}님, 커피 나왔습니다. {1}번 불렀습니다.".format(customers,index))
#     index+=1

# customer="토르"
# person="Unknown"
# while person != customer:
#     print("{0}님, 커피 나왔습니다.".format(customer))
#     person=input("성함이 어떻게 되세요?")

#continue와 break
# absent=[2,5] #결석
# no_book=[13,17]
# for students in range(1,21):
#     if students in absent:
#         continue #만족한다면 밑의 실행문을 건너뛴다.
#     elif students in no_book:
#         print("오늘 수업은 끝 {0}는 교무실로 와".format(no_book))
#         break # 아예 실행을 종료료
#     print("{0}이 발표하자.".format(students))
    
# 한 줄 for / 임마는 리스트임 따라서[]랑 같이 씀 하지만 그냥 for와는 다르게 한 줄 for은 단독으로 사용하는 것은 불가능. 또한 이 변수를 활용하려면 in 뒤의 변수를 활용한다.
students=[1,2,3,4,5]
students=[100+i for i in students] #for 앞 뒤의 변수가 같게 students의 반복을 i가 받고 그걸 100+1로 출력.
print(students)

# 이름을 글자 길이로 변환.
students=["아이언맨","토르","그루트"]
students=[len(i) for i in students]
print(students)

#학생 이름을 대문자로 바꾸기.
students=["iron man", "thor", "groot"]
students=[i.upper() for i in students ] 
print(students)

#함수 def

# def deposit(balance,money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
#     return balance+money #이게 deposit의 값이 되고 따라서 balance의 값도 1010 print(balance)의 값도 1010이 된다.
# balance=0
# balance=deposit(balance,1000)
# print(balance)

# def deposit(balance,money): #입금(다른 예시)
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
#     return balance+money 
# balance=0
# money=deposit(balance,1000)
# print(money) #여기서도 똑같이 money로 바꾸면 리턴의 발란스+돈의 값을 디포짓이 받고 그 값이 돈과 같다고 했으니 돈을 출력하면 1000이 나온다.

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
def deposit(balance,money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance,money): #출금
    if balance>=money:
        print("출금이 완료되었습니다. 남은 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    elif balance<money:
        print("잔액이 부족합니다. 남은 잔액은 {0}원 입니다.".format(balance))
        return balance
money=500
balance=500
balance=withdraw(balance,money) #순서대로 입금 먼저 그다음 출금, 문장을 바꾸면 또 순서를 바꿀 수 있다.
balance=deposit(balance,money)
print(balance)
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#저녁 출금
def withdraw_night(balance,money): # 리턴값을 ~~,~~로 튜플 형식도 가능하다. 그럼 반환값으로 수수료, 잔액=withdraw_night(수수료, 잔액) 그 다음줄에 print()를 써서 수수료와 잔액 변수를 활용할 수 있다.
    if balance>=money:
        time=int(input("몇 시에 출금하시나요?")) #정수로 변환해야 했다 in
        if time>=22:
            Q=input("밤 22시 이후 할증 100원이 붙습니다. 그래도 출금하시겠습니까?")
            if Q=="네":
                print("예약되었습니다. 남은 잔액은 {0}원입니다.".format(balance-money-100))
                return balance-money-100
            elif Q=="아니요":
                print("취소되었습니다. 남은 잔액은 {0}원입니다.".format(balance))
                return balance
            else:
                print("다시 시도해주십시오. 남은 잔액은 {0}원입니다.")
                return balance
        elif time<22:
            print("정상 예약되었으며, 수수료는 없습니다. 남은 잔액은 {0}원입니다.".format(balance-money))
            return balance-money
    elif balance<money:
        print("잔액이 부족합니다.")
        return balance

balance=1000
money=5000
balance=withdraw_night(balance,money)
print(balance)

#기본값
def profile(name, age, main_lang):
    print("이름:{0}, 나이:{1}, 주 사용 언어:{2}".format(name, age, main_lang))

profile("유재석", 19, "자바")
profile("하하", 21, "파이썬")

#정보가 같을 떄 기본값을 활용한다.
def profile(name, age=17, main_lang="파이썬"): #이름만 다르게 하면 다른 건 다 똑같이 나온다.
    print("이름:{0}, 나이:{1}, 주 사용 언어:{2}".format(name, age, main_lang))
profile("유재석")
profile("김태호")

#키워드값
def profile(name, age, main_lang):
    print(main_lang, age, name)
profile(age=14, name="유재석", main_lang="파이썬") #순서가 달라도 나이 언어 이름 등 딱 정해 놓으면 순서가 달라도 상관 없다.

#가변인자
def profile(name, age, *language): # 변수 앞에 *을 넣으면 여러개를 쓸 수 있다.
    print("이름:{1}, 나이:{0}".format(age, name),end=" ") # ,end=""는 프린트하고 다음 프린트가 바로 뒤에 붙을 수 있게한다.또한 ""안에 띄어쓰기를 넣으면 뒷 문장을 띄워서 쓸 수 있다.
    for lang in language:
        print(lang,end=" ")

profile("유재석", 45,"c","c++","c#")

#지역변수(함수 내에서만 쓸 수 있다.)와 전역변수(프로그램 내에 어디서든 쓸 수 있다.)

#지역변수 
gun=10
def checkpoint(soldiers):
    gun=20
    print("남은 총:{0}자루.".format(gun-soldiers))# 함수 내부의 문장은 외부의 변수를 쓸 수 없음 따라서 내부에 안 만들면 오류 뜸.
print("전체 총:{0}".format(gun)) #함수 외부임(띄어쓰기 없쥬??) 따라서 함수 외부인 총=10을 따름
checkpoint(2)
print("총:{0}".format(gun))#야도 외부인 건 마찬가지.

#전역변수

