from tkinter import *

window = Tk()
photo = PhotoImage(file="wl.gif")
w = Label(window, image=photo).pack(side="right") // 포토를 넣고 오른쪽에 삽입한다.
message= """삶이 그대를 속일지라도
슬퍼하거나 노하지 말라 !
우울한 날들을 견디면 : 믿으라,
기쁨의 날이 오리니.
마음은 미래에 사는 것
현재는 슬픈 것:
모든 것은 순간적인 것, 지나가는 것이니
그리고 지나가는 것은 훗날 소중하게 되리니.
"""
w2 = Label(window,
           justify=LEFT,       //왼쪽 정렬
           padx = 10,          //x 축 공백
           text=message).pack(side="left") //왼쪽으로 패킹한다.
window.mainloop()



from tkinter import *

window = Tk()

Label(window,
		 text="Times Font 폰트와 빨강색을 사용합니다.",
		 fg = "red",
		 font = "Times 32 bold italic").pack()
Label(window,
		 text="Helvetica 폰트와 녹색을 사용합니다.",
		 fg = "blue",
		 bg = "yellow",
		 font = "Helvetica 32 bold italic").pack()
window.mainloop()



-------------grid 는 격자모양 ----------------

from tkinter import *

window = Tk()
Label(window , text="이름").grid(row=0)
Label(window, text="나이").grid(row=1)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)  // 첫번째 왼쪽 (기본 값)
e2.grid(row=1, column=1)

window.mainloop( )






from tkinter import *

def show():
   print("이름: %s\n나이: %s" % (e1.get(), e2.get()))   //get 은 글자를 리턴 해준다.

parent  = Tk()
Label(parent , text="이름").grid(row=0)
Label(parent, text="나이").grid(row=1)

e1 = Entry(parent)
e2 = Entry(parent)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(parent, text='보이기', command=show).grid(row=2, column=1, sticky=W, pady=4)  //sticky = w(est) 왼쪽에 달라 붙어라
Button(parent, text='종료', command=parent.quit).grid(row=2, column=0, sticky=W, pady=4) //parent.quit 윈도우 자체를 끝내라 pady 는 y축으로 공백

mainloop( )




from tkinter import *

window = Tk()
T = Text(window, height=5, width=60)  //5줄 60글자 까지
T.pack()
T.insert(END, "테스트 위젯은 여러 줄의\n텍스트를 표시할 수 있습니다.")
mainloop()








from tkinter import *
from math import *
def calculate(event):    // 마우스 클릭 드래그 -> 이벤트 객체에 저장
    label.configure(text = "결과: " + str(eval(entry.get())))  // label 한줄의 문장을  만들어 준다.

    //enty -> string 이 들어온다 이걸 수학 계산하기 위해서는 eval 이 필요하다 .
    //eval 은 스트링으로 되어 있는 사칙연산을 수학 계산으로 바꿔서 사용해준다.

window = Tk()

Label(window, text="파이썬 수식 입력:").pack()
entry = Entry(window)
entry.bind("<Return>", calculate) // 콜백함수 등록
entry.pack()

label = Label(window, text ="결과:")
label.pack()

w.mainloop()


콜백 함수 사용 2가지 방법

객체.bind
command

---------------eval----------------------



>>> from math import *
>>> eval("3*4")
12
>>> eval(3*4)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    eval(3*4)
TypeError: eval() arg 1 must be a string, bytes or code object
>>>





-----------canvas 그리기 --------------


from tkinter import *

window = Tk()

w = Canvas(window, width=300, height=200)
w.pack()

w.create_rectangle(50, 25, 200, 100, fill="blue")  //좌측 상단가 우측 하단의 점을 언급해준다.(50,25) (200,100)
w.create_line(0, 0, 300, 200)
w.create_line(0, 0, 300, 100, fill="red")

mainloop()





>>> import random
>>> a=[10,20,30,40,50]
>>> random.choice(a)
40
>>> 40
40
>>> random.choice(a)
10
>>> random.choice(a)
30
>>> random.choice(a)
30






import random
from tkinter import *

window = Tk()
canvas = Canvas(window, width=500, height=400)
canvas.pack()
color = ["red", "orange", "yellow", "green", "blue", "violet"]

def draw_rect():
    x = random.randint(0, 500)    //0에서 500 사이 (크기가 500이 최대 위에서 정해서)
    y = random.randint(0, 400)    //0에서 400 사이
    w = random.randrange(100)     //0~99를 리턴해준다.
    h = random.randrange(100)     //0~99를 임의의 수로 해놓은다.
    canvas.create_rectangle(x, y, x+w, y+h, fill = random.choice(color))

for i in range(10):
    draw_rect()

window.mainloop()





원그리기

from tkinter import *
window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()
canvas.create_oval(10, 10, 200, 150)
window.mainloop()

외접하는 사각형을 가정하여 그리고 그 사각형에 맞춰 원을 그린다.




호 그리기

from tkinter import *
window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()
canvas.create_arc(10, 10, 200, 150, extent=90, style=ARC)
window.mainloop()


가상의 사각형에서 x 쪽에서 y 쪽으로 1 2 3 4 분면으로 간다.



이미지 넣기



from tkinter import *
window = Tk()

canvas = Canvas(window,  width=300, height=200)
canvas.pack()

img = PhotoImage(file="D:\\starship.png")
canvas.create_image(20, 20, anchor=NW, image=img) (nw north west 이걸 점으로 잡고 그림을 그린다.)

mainloop()





from tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()

id=canvas.create_oval(10, 100, 50, 150, fill="green")

def move_right(event):           // 롤백함수
    canvas.move(id, 5, 0)
canvas.bind_all('<KeyPress-Right>', move_right)
