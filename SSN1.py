#메인
import SSN

while(1):
    print
    print("****메뉴****")
    print("1.주민번호 입력")
    print("2.복호화")
    print("3.종료")

    menu = int(input("메뉴를 선택하세요 :"))

    if(menu==1):
        print
        a = int(input("주민번호를 입력하세요 :"))
        a = SSN.func1(a)
        print(a)

    elif(menu==2):
        print
        a = SSN.func2(a)
        print(a)

    elif(menu==3):
        print
        print("프로그램이 종료 되었습니다.")
        break;

    else :
        print("다시 입력 해주세요")

    menu=0

    
        
