menu = {"우유", "커피", "주스"}
print(menu,type(menu))
# #자료 형태 바꾸기기
# menu=list(menu)
# print(menu,type(menu))

# menu=tuple(menu)
# print(menu,type(menu))

# menu=set(menu)
# print(menu,type(menu))

# #if
# weather="맑음"
# if weather=="비":
#     print("우산을 챙기세요") #만약 비가 아니라면 아무것도 출력되지 않는다.
# elif weather=="미세먼지": #elif를 쓰기도 한다.
#     print("미스크를 챙기세요.")
# else:
#     print("준비물은 필요 없어요.")

# #사람의 값을 기다리는 input
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
temp=int(input("오늘 날씨 몇 도예요?"))
if temp>=30:
    print("너무 덥네요. 나가지 말아요")
elif temp<30 and temp>10:
    print("날씨 좋네요. 나가 놀아요")
elif temp<=10 and temp>0: #또는 바로 0<temp<10으로 쓸 수 있다.
    print("쌀쌀하네요. 외투를 챙겨요.")
else:
    print("너무 추워요. 나가지 말아요.")

# #for (반복문)
# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4") #이는 너무 번거롭다 따라서 for를 쓴다.
# for waiting in[1,2,3,4,]:
#     print("대기번호:{0}".format(waiting))


# for waiting in range(1,6): #또는 range(5), 선택이 :이고 이건,이다. 또한 (x,y)는 y이전까지인 거 알지??
#     print("대기번호:{0}".format(waiting))
# starbucks=["아이언맨", "토르", "헐크"]
# for customers in starbucks:
#     print("{0}님 커피 나왔습니다.".format(customers))
