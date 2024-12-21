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
# gun=10
# def checkpoint(soldiers):
#     gun=20
#     print("남은 총:{0}자루.".format(gun-soldiers))# 함수 내부의 문장은 외부의 변수를 쓸 수 없음 따라서 내부에 안 만들면 오류 뜸.
# print("전체 총:{0}".format(gun)) #함수 외부임(띄어쓰기 없쥬??) 따라서 함수 외부인 총=10을 따름
# checkpoint(2)
# print("총:{0}".format(gun))#야도 외부인 건 마찬가지.

#전역변수
# gun=10
# def checkpoint(soldiers):
#     global gun
#     gun=gun-soldiers
#     print("남은 총:{0}".format(gun))
# checkpoint(2)

#체크포인트 리턴

def checkpoint(gun,soldiers):
    print("남은 총:{0}".format(gun-soldiers))
    return gun-soldiers
gun=10
gun=checkpoint(gun,2)
print(gun)

#표준 입출력
print("python", "java",sep=" vs ",end=" ")
print("무엇이 더 재밌을 까요?")

import sys
print("python","java", file=sys.stdout) #이건 더 알아보자.
print("python","java", file=sys.stderr)

scores={"수학":0, "영어":50, "코딩":100}
for subject,score in scores.items():
    print(subject.ljust(4),str(score).rjust(8),sep=":")

for num in range(1,21):
   # print("대기번호:"+str(num).zfill(3)) #3칸을 만들고 빈 공간에는 0으로 채운다.
    print("대기번호:{0}".format(str(num).zfill(3))) #zfill이 문자 메서드 따라서 str을 num에 붙인다.
#표준입력
# ans=input("아무 말이나 해보든가.")
# print("넌 {0}라고 했구나.".format(ans)) # input의 값은 숫자든 문자든 다 str, 즉 문자형태로 나온다.
# print(type(ans))

#다양한 출력포멧

print("{0: >10}".format(500))
print("{0: >+10}".format(500)) #양,음
print("{0:_<+10}".format(500))
print("{0:,}".format(100000000000000)) #3자리마다 ,찍기
print("{0:+,}".format(100000000000000)) #3자리마다 ,찍기, 양음 
# 3자리 콤마, 부호, 자릿수, 빈 자리는 ^
print("{0:^<+30,}".format(100000000000000000)) #숫자 쓸거면  숫자 앞자리는 다 채워야 이상하게 안 됨.

#소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))#특정 소수점까지만 출력.

#파일 입출력
score_file=open("score", "w", encoding="utf8")
print("영어:0",file=score_file)
print("수학:50",file=score_file)
score_file.close

score_file=open("score", "a",encoding="utf8")
score_file.write("과학:100\n")
score_file.write("코딩:100")
score_file.close

score_file=open("score", "r", encoding="utf8")
print(score_file.read()) #모두 출력한다.
score_file.close

score_file=open("score", "r", encoding="utf8")
print(score_file.readline(),end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline())
score_file.close

score_file=open("score", "r", encoding="utf8")
while True:
    line=score_file.readline()
    if not line: #not도 알아두자
        break
    print(line,end="") #,end는 쓰는 명령문에만 넣자.
score_file.close

score_file=open("score", "r", encoding="utf8")
lines=score_file.readlines() #야는 특별히 리스트로 저장되는 형식.
for line in lines: #리스트를 문자열로 바꾼다.
    print(line,end="")

#pickle
import pickle #데이터를 파일 형태로 저장한다. 우린 볼 수 없다.
profile_file=open("profile","wb") # 얘는 b를 꼭 써주고 encoding="utf8"은 안 쓴다.
profile={"이름":"권동욱","나이":19,"취미":["코딩","운동"]}
print(profile)
pickle.dump(profile,profile_file) #dump가 내놓다 데이터를 내놓다.
profile_file.close()

profile_file=open("profile","rb")
profile=pickle.load(profile_file) # 파일에 저장된 값을 불러와 프로필이라는 변수에 저장. load가 태우다. 기져오다 파일을 데이터로 가져오다.
print(profile)
profile_file.close

#with 이걸 쓰면 파일 입출력을 좀 더 편하게 할 수 있다.
import pickle
with open("profile","rb") as profile_file:
    print(pickle.load(profile_file))

with open("study","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 공부하다.")

with open("study", "r", encoding="utf8") as study_file:
    print(study_file.read())

with open("profile", "rb") as profile_file:
    print(pickle.load(profile_file))

#클래스
#마린: 공격 유닛, 군인, 총 씀
# name="마린"
# hp=40
# damage=5
# print("{0}유닛이 생성되었습니다.".format(name))
# print("체력:{0}\n공격력:{1}".format(hp, damage))

# #탱크:공격 유닛, 탱크, 포를 씀, 일반 모드/ 시즈 모드 
# name_tank="탱크"
# hp_tank=150
# damage_tank=30
# print("{0}유닛이 생성되었습니다.".format(name_tank))
# print("체력:{0}\n공격력:{1}".format(hp_tank, damage_tank))

# import sys
# def attack(name, location, damage):
#     print("{0}:{1}시 방향으로 적군을 향해 공격합니다.[공격력:{2}]".format(name , location, damage))
# location=int(input("마린, 몇 시 방향을 공격하시겠습니까?"))
# if location>24:
#     print("다시 입력해주세요.")
#     sys.exit()
# attack(name, location, damage )

# location=int(input("탱크, 몇 시 방향을 공격하시겠습니까?"))
# if location>24:
#     print("다시 입력해주세요.")
#     sys.exit()

# attack(name_tank, location, damage_tank) #이거 넘 번거로움 따라서 클래스가 있음.

#클래스는 붕어빵 틀과 같이 만들어 내는 것.-----------------------------------------이건 좀 더 알아보고 공부하기
# class 
# class unit: #여기선 unit이 함수를 부를 때 사용된다.
#     def __init__(self, name, hp, damage): # __init__은 생성하겠다는 것 객체는 마린, 탱크같은 것.
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{0}유닛이 생성되었습니다.".format(self.name))
#         print("체력:{0}, 공격력:{1}".format(self.hp, self.damage))

# marine1= unit("마린", 40, 5) #객체는 __init__ 뒤에 있는 함수 모두를 포함해야 한다.(self제외)
# marine2= unit("마린", 40, 5)
# tank= unit("탱크", 150, 35)

# #멤버 변수(self.name=name, self.hp=hp 이런것들 class내의 것을 외부에서 쓴다.)

# #레이스: 공중 유닛, 비행기, 스텔스
# wraith1= unit("레이스", 80, 5)
# print("유닛 이름:{0}, 공격력:{1}".format(wraith1.name, wraith1.damage)) #함수를 부르는 게 아닌 클래스 함수 내 변수를 이용한다.  

# #마인드 컨트롤 : 상대방 유닛을 내것으로 만든다. (빼앗음)
# wraith2=unit(" 빼앗은 레이스", 80, 5)
# wraith2.clocking=True #클래스 외부에서 내부의 변수를 확장했다.(name)

# if wraith2.clocking== True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

#메소드(일반 유닛) 
class unit: #여기선 unit이 함수를 부를 때 사용된다.
    def __init__(self, name, hp, damage): # __init__은 생성하겠다는 것 객체는 마린, 탱크같은 것.
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력:{0}, 공격력:{1}".format(self.hp, self.damage))
class attackunit:
    def __init__(self, name, hp, damage): # __init__은 생성하겠다는 것 객체는 마린, 탱크같은 것.
        self.name=name # 함수에서 name의 값을 self에 넘긴다는 뜻.
        self.hp=hp
        self.damage=damage
    
    def attack(self,location): #얘는 어택 유닛 클래스에 포함된다.
        print("{0}:{1}시 방향으로 적군을 공격합니다.[공격력:{2}]".format(self.name, location, self.damage)) #self가 있는 name과 damage는 클래스 내부 self변수를 이용히겠고 self가 없는 location은  함수 내에 변수를 이용하겠다.self는 클래스꺼다 클래스 안에서는 함수가 달라도 쓸 수 있다.

    def damaged(self,damaged):
        print("{0}:{1}데미지를 입었습니다.".format(self.name, damaged))
        self.hp-=damaged
        print("{0}:현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0}:파괴되었습니다.".format(self.name))


#파이어 벳 : 공격 유닛, 불을 뿜음
firebat1= attackunit("파이어 벳", 50, 16) #어택유닛 클래스로 지정
firebat1.attack(1) #어택 함수로 지정

firebat1.damaged(25)# 데미지드 함수로 지정
firebat1.damaged(25)

#상속
class unit: #name과 hp는 unit과 attackunit모두 있어 상속이 가능하다. 
    def __init__(self, name, hp): 
        self.name=name
        self.hp=hp
        print("{0}유닛이 생성되었습니다.".format(self.name))        

class attackunit(unit): #괄호 안의 클래스를 상속받아 어택유닛을 만든다는 의미이다.
    def __init__(self, name, hp, damage): 
        unit.__init__(self,name,hp) #상속 받을 변수 설정.
        self.damage=damage
    
    def attack(self,location):
        print("{0}:{1}시 방향으로 적군을 공격합니다.[공격력:{2}]".format(self.name, location, self.damage))

    def damaged(self,damaged):
        print("{0}:{1}데미지를 입었습니다.".format(self.name, damaged))
        self.hp-=damaged
        print("{0}:현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0}:파괴되었습니다.".format(self.name))
#매딕: 의무병.
madic= unit("매딕", 40)



firebat1= attackunit("파이어 벳", 50, 16) #어택유닛 클래스로 지정
firebat1.attack(1) #어택 함수로 지정

firebat1.damaged(25)# 데미지드 함수로 지정
firebat1.damaged(25)

#다중 상속
class unit: #name과 hp는 unit과 attackunit모두 있어 상속이 가능하다. 
    def __init__(self, name, hp): 
        self.name=name
        self.hp=hp
        print("{0}유닛이 생성되었습니다.".format(self.name))        

class attackunit(unit): #괄호 안의 클래스를 상속받아 어택유닛을 만든다는 의미이다.
    def __init__(self, name, hp, damage): 
        unit.__init__(self,name,hp) #상속 받을 변수 설정.
        self.damage=damage
        print("{0}".format(name)) #valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해 출력됨.
    
    def attack(self,location):
        print("{0}:{1}시 방향으로 적군을 공격합니다.[공격력:{2}]".format(self.name, location, self.damage))
        print("{0}".format(self.name)) #valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해 출력 안 됨.

    def damaged(self,damaged):
        print("{0}:{1}데미지를 입었습니다.".format(self.name, damaged))
        self.hp-=damaged
        print("{0}:현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0}:파괴되었습니다.".format(self.name))

#드랍쉽: 공중 유닛, 수송기, 공격 불가.

class flyable:
    def __init__(self,flying_speed):
        self.flying_speed =flying_speed

    def fly(self, name, location):
        print("{0}:{1}시 방향으로 날아갑니다. [속도:{2}]".format(name, location, self.flying_speed))

#공중 공격 유낫
class flyable_attack_unit(attackunit, flyable):
    def __init__(self,name, hp, damage, flying_speed):
        attackunit.__init__(self,name, hp, damage)
        flyable.__init__(self, flying_speed)

#발키리: 공중 공격 유닛, 한 번에 14발 발사.
valkyrie= flyable_attack_unit("발키리", 200, 6, 5) #*여기서 두 클래스 어택 유닛과 플라이어블에 바로 밑 ,즉 어택유닛클래스의 init 플라이어블 클래스의init에만 적용된다.* 따라서 어택 유닛 클래스에 어택 함수에는 print가 있어도 출력되지 않는다.
valkyrie.fly(valkyrie.name, 1) #여기선 valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해  플라이어블 클래스에는는 비행 속도 변수만 저장된다. 따라서 이름을 정해준다.
valkyrie.attack(1)

#메소드 오버라이딩.
class unit: #name과 hp는 unit과 attackunit모두 있어 상속이 가능하다. 
    def __init__(self, name, hp): 
        self.name=name
        self.hp=hp
        print("{0}유닛이 생성되었습니다.".format(self.name))        

class attackunit(unit): #괄호 안의 클래스를 상속받아 어택유닛을 만든다는 의미이다.
    def __init__(self, name, hp, damage): 
        unit.__init__(self,name,hp) #상속 받을 변수 설정.
        self.damage=damage
        print("{0}".format(name)) #valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해 출력됨.
    
    def attack(self,location):
        print("{0}:{1}시 방향으로 적군을 공격합니다.[공격력:{2}]".format(self.name, location, self.damage))
        print("{0}".format(self.name)) #valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해 출력 안 됨.

    def damaged(self,damaged):
        print("{0}:{1}데미지를 입었습니다.".format(self.name, damaged))
        self.hp-=damaged
        print("{0}:현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0}:파괴되었습니다.".format(self.name))

#드랍쉽: 공중 유닛, 수송기, 공격 불가.

class flyable:
    def __init__(self,flying_speed):
        self.flying_speed =flying_speed

    def fly(self, name, location):
        print("{0}:{1}시 방향으로 날아갑니다. [속도:{2}]".format(name, location, self.flying_speed))

#공중 공격 유낫
class flyable_attack_unit(attackunit, flyable):
    def __init__(self,name, hp, damage, flying_speed):
        attackunit.__init__(self,name, hp, damage)
        flyable.__init__(self, flying_speed)

#발키리: 공중 공격 유닛, 한 번에 14발 발사.
valkyrie= flyable_attack_unit("발키리", 200, 6, 5) #*여기서 두 클래스 어택 유닛과 플라이어블에 바로 밑 ,즉 어택유닛클래스의 init 플라이어블 클래스의init에만 적용된다.* 따라서 어택 유닛 클래스에 어택 함수에는 print가 있어도 출력되지 않는다.
valkyrie.fly(valkyrie.name, 1) #여기선 valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해  플라이어블 클래스에는는 비행 속도 변수만 저장된다. 따라서 이름을 정해준다.
valkyrie.attack(1)

#메소드 오버라이딩.
class unit: #name과 hp는 unit과 attackunit모두 있어 상속이 가능하다. 
    def __init__(self, name, hp): 
        self.name=name
        self.hp=hp
        print("{0}유닛이 생성되었습니다.".format(self.name))        

class attackunit(unit): #괄호 안의 클래스를 상속받아 어택유닛을 만든다는 의미이다.
    def __init__(self, name, hp, damage): 
        unit.__init__(self,name,hp) #상속 받을 변수 설정.
        self.damage=damage
        print("{0}".format(name)) #valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해 출력됨.
    
    def attack(self,location):
        print("{0}:{1}시 방향으로 적군을 공격합니다.[공격력:{2}]".format(self.name, location, self.damage))
        print("{0}".format(self.name)) #valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해 출력 안 됨.

    def damaged(self,damaged):
        print("{0}:{1}데미지를 입었습니다.".format(self.name, damaged))
        self.hp-=damaged
        print("{0}:현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0}:파괴되었습니다.".format(self.name))

#드랍쉽: 공중 유닛, 수송기, 공격 불가.

class flyable:
    def __init__(self,flying_speed):
        self.flying_speed =flying_speed

    def fly(self, name, location):
        print("{0}:{1}시 방향으로 날아갑니다. [속도:{2}]".format(name, location, self.flying_speed))

#공중 공격 유낫
class flyable_attack_unit(attackunit, flyable):
    def __init__(self,name, hp, damage, flying_speed):
        attackunit.__init__(self,name, hp, damage)
        flyable.__init__(self, flying_speed)

#발키리: 공중 공격 유닛, 한 번에 14발 발사.
valkyrie= flyable_attack_unit("발키리", 200, 6, 5) #*여기서 두 클래스 어택 유닛과 플라이어블에 바로 밑 ,즉 어택유닛클래스의 init 플라이어블 클래스의init에만 적용된다.* 따라서 어택 유닛 클래스에 어택 함수에는 print가 있어도 출력되지 않는다.
valkyrie.fly(valkyrie.name, 1) #여기선 valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해  플라이어블 클래스에는는 비행 속도 변수만 저장된다. 따라서 이름을 정해준다.
valkyrie.attack(1)

#메소드 오버라이딩. 자식 클래스의 메소드를 쓰고 싶을 때 쓴다.
class unit: #name과 hp는 unit과 attackunit모두 있어 상속이 가능하다. 
    def __init__(self, name, hp, speed): 
        self.name=name
        self.hp=hp
        self.speed=speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}:{1}시 방행으로 이동합니다. [이동 속도:{2}]".format(self.name, location, self.speed))        

class attackunit(unit): #괄호 안의 클래스를 상속받아 어택유닛을 만든다는 의미이다.
    def __init__(self, name, hp, speed, damage): 
        unit.__init__(self,name,hp, speed) #상속 받을 변수 설정.
        self.damage=damage
        print("{0}".format(name)) #valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해 출력됨.
    
    def attack(self,location):
        print("{0}:{1}시 방향으로 적군을 공격합니다.[공격력:{2}]".format(self.name, location, self.damage))
        print("{0}".format(self.name)) #valkyrie= flyable_attack_unit("발키리", 200, 6, 5)에 의해 출력 안 됨.

    def damaged(self,damaged):
        print("{0}:{1}데미지를 입었습니다.".format(self.name, damaged))
        self.hp-=damaged
        print("{0}:현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0}:파괴되었습니다.".format(self.name))

#드랍쉽: 공중 유닛, 수송기, 공격 불가.

class flyable:
    def __init__(self,flying_speed):
        self.flying_speed =flying_speed

    def fly(self, name, location):
        print("{0}:{1}시 방향으로 날아갑니다. [속도:{2}]".format(name, location, self.flying_speed))

#공중 공격 유닛닛
class flyable_attack_unit(attackunit, flyable):
    def __init__(self,name, hp, damage, flying_speed):
        attackunit.__init__(self,name, hp, 0,  damage) # 지상 이동 속도=0
        flyable.__init__(self, flying_speed)
    
    def move(self, location): # self하고 ,는 나머지 모두 .은 각각 하나만 있고 self를 적용할 떄도 나머지 모두이기에 , 를 쓴다.
        print("[공중 유닛 이동]")
        self.fly(self.name, location) # 이러면 그냥 move만 써도 공중 유닛 이동이 된다. 메소드 오버로딩. 지상은 유닛 클래스에만 있어 [지상 유닛 이동]이라고 뜨는데 공중 클래스의 유닛은 함수가 다시 재정의 되어 [공중 유닛 이동]이라고 뜬다. 


# 벌처: 지상 유닛, 기동성 좋음
vulture= attackunit("벌처",80, 10, 20)
vulture.move(11)
# 배틀크루저:공중 유닛
battlecruiser= flyable_attack_unit("배틀 크루저", 500, 25, 3)
battlecruiser.fly(battlecruiser.name,9) 
battlecruiser.move(9) #공중 유닛은 플라이 함수 지상 유닛은 무브 함수라 귀찮다. 따라서 매소드 오버라이딩을 쓴다.




