'''
2020.11.07. Woosang Cho
천문학 자료처리에서 사용되는 율리우스력을 계산하는 프로그램 입니다.
y, m, d에 각각 년, 달, 일 을 입력받아, 계산합니다. 
결과는 실수 십진수 형태입니다.
'''
import time 
start = time.time()

y = int(input('Enter the year: ')) #년도 입력
m = int(input('Enter the month: ')) #달 입력
d = int(input('Enter the day: ')) #날짜 입력

print(367*y - (7*(y + (m+9)/12))/4 - (3*((y + (m-9)/7)/100 + 1))/4 + 275*m/9 + d + 1721029) #율리우스일 계산
