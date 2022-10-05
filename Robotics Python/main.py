import KeyPress, motorControl, time

#initialize keyboard read
KeyPress.init()

#initialize wheel Motor------------------------------
motorControl.initmotor()
time.sleep(.1)
#motorControl.initmotorturn()
#time.sleep(.1)

#set waist to middle
motorControl.setmiddlewaist()
time.sleep(.1)

#set head lr Middle
motorControl.setMiddleheadlr()
time.sleep(.1)

#set head middle up down
motorControl.setMiddleheadud()
time.sleep(.1)
#end initialize wheel Motor------------------------------


#cnt = 0
def main():
    #global cnt
    #WAIST left
    if KeyPress.getKey('q'):
        motorControl.movewaistLeft()

    #wheels turn
    if KeyPress.getKey('RIGHT'):
        motorControl.moveright()
        motorControl.initmotor()
        time.sleep(.1)

    #Stop Function
    if KeyPress.getKey('SPACE'):
        motorControl.initmotorstop()

    #turn Wheels Left
    if KeyPress.getKey('LEFT'):
        motorControl.moveleft()
        motorControl.initmotor()
        time.sleep(.1)

    #set wheel speed up
    if KeyPress.getKey('UP'):
        motorControl.moveforward()

    #set wheel speed down
    if KeyPress.getKey('DOWN'):
        motorControl.moveback()

    #WAIST right
    if KeyPress.getKey('e'):
        motorControl.movewaistRight()

    #tilt HEAD up
    if KeyPress.getKey('w'):
        motorControl.tiltHeadUp()

    #titl HEAD Down
    if KeyPress.getKey('s'):
        motorControl.tiltHeadDown()

    #tilt HEAD right
    if KeyPress.getKey('d'):
        motorControl.tiltHeadRight()

    #tilt HEAD left
    if KeyPress.getKey('a'):
        motorControl.tiltHeadLeft()



if __name__ == '__main__':
    #init()
    while True:
        main()
