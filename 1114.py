>>> from tkinter import *
>>> window=Tk()
>>> label = Label(window, text="안녕하세요")
>>> label = pack()

>>> label.pack()
>>> label1=Label(window, text = "파이썬 프로그램")
>>> label1.pack()


window.mainloop()

$ 이창을 꺼야 >>>가 나온다.



버튼 만들기


>>> window=Tk()
>>> b=Button(window, text="첫번째 버튼")
>>> b.pack()
지금 까지 한 걸 해라 ! 



지금까지 한 것을 잊어라

>>> b.forget()



방향 생성


>>> b.pack(side=LEFT)
>>> b1.pack(side=LEFT)




공백 생성

>>> b1.pack(side=LEFT, padx = 10)




버튼 이름 바꾸기 
>>> b["text"]="첫번째"
>>> b.pack()





이벤트처리


>>> def callback():
	button["text"]="버튼이 클릭되었음!"

	
>>> window = Tk()
>>> button = Button(window, text="클릭", command=callback)
>>> button.pack(side=LEFT)
>>> window.mainloop()






Grid 
격자 배치 관리자(grid geometry manager)는 테이블 형태의 배치
Pack
압축 배치 관리자(pack geometry manager)는 위젯들을 부모 위젯 안에 압축
Place
절대 배치 관리자(place geometry manager)는 주어진 위치에 위젯을 배치



>>> import tkinter.colorchooser
>>> color = tkinter.colorchooser.askcolor()
>>> color
((116.453125, 91.35546875, 230.8984375), '#745be6')
>>> color[1]
'#745be6'

색 깔은 튜플로 되어있다.


RGB 색깔

#000000
# ff 00 00
이렇게 8진수로 나와 있다.

