T = input()
for i in range(int(T)):
    a = b = 0
    for  i in range(3):
        x, y = map(int, input().split())
        a = a ^ x
        b = b ^ y
    print(a , b)

















