
def go(no):
    n=0
    while n < no :
        if on_beeper():
            pick_beeper()
            if on_beeper():
                pick_beeper()
            else:
                move()
                n=n+1
                print(n)
        else:
            move()
            n=n+1
            print(n)
    turn_left()



go(6)
go(5)
go(5)
go(4)
go(4)
go(3)
go(3)
go(2)
go(2)
go(1)
go(1)
turn_off()
