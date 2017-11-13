# 전체 반복할 횟수를 입력받는다
T = input()
# 각각 짝수 번째 문자와 홀수 번째 문자를 저장할 리스트를 선언한다
even = []
odd = []
#입력받은 횟수만큼 반복하는 반복문을 만든다
for i in range(int(T)):
#암호화할 문자열을 입력 받는다
    x = input().strip()
#슬라이싱할 문자열의 순서를 가리키는 변수를 초기화한다
    y = 0
    z = 1
#입력받은 문자열의 갯수만큼 반복하는 반복문을 만든다
#y가 짝수이고 z가 홀수 일 때 짝수 리스트에 문자열을 추가한다. ex(y=0, z=1 or y=2,z=3..)
# 그 반대로는 홀수 리스트에 추가한다.
    for t in range(int(len(x))):
        X = x[y:z]
        if y % 2 == 0 and z % 2 != 0:
            even.append(X)
        else:
            odd.append(X)
#y와 z를 1씩 증가시켜 다음 순서로 이동시킨다
        y = y + 1
        z = z + 1
#리스트 두 개를 짝수 리스트가 앞에 오도록 더한다
        result = even + odd
#result를 연결하여 출력한다
    print("".join(result))
#다음 문자열을 출력하기 위해 result, even, odd를 pop을 사용해 비워준다
    while len(result) > 0 : result.pop()
    while len(even) > 0 : even.pop()
    while len(odd) > 0 : odd.pop()