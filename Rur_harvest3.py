

def go1():
    move()
def go(no):
    n=0
    while n < no :
        if on_beeper():
            pick_beeper()
            move()

        else:
            move()
            n=n+1
            print(n)
    turn_left()




go1()
turn_off()
