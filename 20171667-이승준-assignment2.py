def isNumber(s):
  try:
    int(s)
    return True
  except ValueError:
    return False
  #입력받은 값이 정수인지 아닌지 판별하는 함수

while True:
    num=input("Enter a number :")#수를 입력받음 
    if isNumber(num) and int(num) >= -1: #입력받은수가 정수이고 양수인지 판별
        if int(num )== -1 : # 입력받은 수가 -1이면 프로그램 종료 
            break
        else :
            ans = 1
            for i in range(1, int(num)):
                ans = ans * (i + 1)#입력받은 수가 -1이 아니라면 팩토리얼 계산
            print(num, end='')
            print('! =', ans)#결과값 출력
