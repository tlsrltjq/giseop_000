#
# 조건문 
#

#1 두 수 비교하기
'''
A, B = map(int, input().split( ))

if A > B :
    print(">")
elif A < B :
    print("<")
else :
    print("==")
'''

#2 시험 성적
'''
score = int(input())

if score <= 100 and score >= 90 :
    print("A")
elif score < 90 and score >= 80 :
    print("B")
elif score < 80 and score >= 70 :
    print("C")
elif score < 70 and score >= 60 :
    print("D")  
else :
    print("F")
'''

#3 윤년
'''
y = int(input())

if y % 4 == 0 :
    if y % 400 == 0 :
        print("1")
    elif y % 100 == 0 :
        print("0")
    else :
        print("1")
else :
    print("0")
'''

#4 사분면 고르기
'''
x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print("1")
elif x < 0 and y > 0 :
    print("2")
elif x < 0 and y < 0 :
    print("3")
elif x > 0 and y < 0 :
    print("4")
'''

#5 알람 시계
'''
H, M = map(int, input().split( ))

M = M - 45

if M < 0 :
    M = 60 + M
    H = H - 1
    if H < 0 :
        H = 24 + H
    print(H, M)
else :
    print(H, M)
'''

#6 오븐 시계
'''
A, B = map(int, input().split())
C = int(input())

B = B + C

if B > 59 :
    A = A + (B//60)
    B = B % 60
    if A > 23 :
        A = A - 24
    print(A, B)
else :
    print(A, B)
'''

#7 주사위 세개
'''
a, b, c = map(int, input().split())
max,reword = 0, 0

if a == b == c :
    reword = 10000 + a * 1000
    print(reword)
elif a==b!=c or a==c!=b or b==c!=a:
    if a-b==0:
        reword = 1000 + a * 100
    elif a-c==0:
        reword = 1000 + a * 100
    elif b-c==0:
        reword = 1000 + b * 100
    print(reword)
elif a!=b!=c :
    if a > b and a > c :
        max = a
    elif b > a and b > c :
        max = b
    elif c > a and c > b :
        max = c
    reword = max * 100
    print(reword)
'''

#
# 반복문
#

#1 구구단
'''
n=int(input(""))

for i in range(1,10) :
    print("%d * %d = %d" %(n,i,n*i))
'''

#2 A+B
'''
T = int(input())

for i in range(0,T):
    A,B = map(int,input().split())
    print(A+B)
'''

#3 1부터 n
'''
n = int(input())
gkq = 0

for i in range(1, n+1) :
    gkq = gkq + i
print(gkq)
'''

#4 영수증

x = int(input())
n = int(input())
chd = 0

for i in range(0, n) :
    a,b = map(int,input().split())
    chd = chd + (a*b)
if x == chd :
    print("Yes")
else :
    print("No")














        
