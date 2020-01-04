# Section02-2
# 몸풀기 코딩 실습

#import this
import sys

print(sys.stdin.encoding)

print(sys.stdout.encoding)

#변수
myName  = 'GoodBoy'
if myName == 'GoodBoy':
    print(myName)

#반복문
for i in range(1,10):
    for j in range(1,10):
        print("%d * %d = " % (i,j),i*j)

#함수
def agreed():
    print("안녕하세요 반갑습니다")

agreed()

#클래스
class Cookie:
    pass


#객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))