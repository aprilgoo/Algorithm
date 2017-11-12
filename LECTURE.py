#몇 번 반복할지 횟수를 입력받음
for t in range(int(input())):
#문자열 입력받음
 x = input()
#변수 y, z를 초기화함
 y = 0
 z = 2
 list = []
#입력받은 문자열 x의 갯수를 2로 나눈 만큼 반복하는 반복문
#문자열이 2개씩 리스트에 저장되므로 2로 나눠줌
 for t in range(int(len(x)/2)):
#리스트 슬라이싱을 이용해서 문자열을 2개씩 자름 x[0:2], x[2:4]..이런 식으로 될 수 있도록 함.
  X = x[y : z]
  y = y + 2
  z = z + 2
#append()함수를 이용하여 위에 만들어놓은 list에 두개씩 자른 문자열을 넣어줌
  list.append(X)
#sort()함수를 이용하여 정렬함
  list.sort()
#문제의 요구에 맞춰 list안에 있는 정렬된 문자열들을 출력함
 for result in list:
  print(result, end="")
 print("")








































