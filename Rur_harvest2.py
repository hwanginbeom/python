def go1(no):
    n=0
    while n<no:
        move()
        if on_beeper():
            pick_beeper()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        n=n+1
def go2(no):
    turn_left()
    move()
    n=0
    while n<no:
        
        if on_beeper():
            pick_beeper()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        if on_beeper():
            pick_beeper()
            turn_left()
        n=n+1
        

def go3(no):
    move()
    turn_left()
    move()
    n=0
    while n<no:
        if on_beeper():
            pick_beeper()
        n=n+1
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        move()
def go4(no):
    n=0
    while n< no:
        if on_beeper():
            pick_beeper()
        move()
        turn_left()
        move()
        if on_beeper():
            pick_beeper()
        turn_left()
        turn_left()
        turn_left()
        n=n+1
        
        
def start2():
    turn_left()
    move()
    turn_left()
def start():
    move()
    move()
    move()
    move()
    move()
    turn_left()

def last():
    move()
    turn_left()
    move()
    pick_beeper()

start()
go1(6)
go2(5)
go3(4)
go4(4)
start2()
go1(4)
go2(3)
go3(2)
go4(2)
start2()
go1(2)
go2(1)
last()

turn_off()
