#����
import SSN

while(1):
    print
    print("****�޴�****")
    print("1.�ֹι�ȣ �Է�")
    print("2.��ȣȭ")
    print("3.����")

    menu = int(input("�޴��� �����ϼ��� :"))

    if(menu==1):
        print
        a = int(input("�ֹι�ȣ�� �Է��ϼ��� :"))
        a = SSN.func1(a)
        print(a)

    elif(menu==2):
        print
        a = SSN.func2(a)
        print(a)

    elif(menu==3):
        print
        print("���α׷��� ���� �Ǿ����ϴ�.")
        break;

    else :
        print("�ٽ� �Է� ���ּ���")

    menu=0

    
        
