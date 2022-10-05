import serial, time, sys

targetHeadRL = 6000
targetHeadUD = 6000
targetmotor = 6000
targetmotorturn = 6000
targetwheels = 6300
targetwaist = 6700


try:
    usb = serial.Serial('/dev/ttyACM0')
    print (usb.name)
    print (usb.baudrate)

except:
    try:
        usb = serial.Serial('/dev/ttyACM1')
        print (usb.name)
        print (usb.baudrate)
    except:
        print("No servo serial ports found")
        sys.exit(0)

def initmotor():
    global targetmotor
    lsb1 = targetmotor &0x7F
    msb1 = (targetmotor >> 7) & 0x7F

    cmd1 = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x00) + chr(lsb1) +chr(msb1)

    usb.write(cmd1.encode('utf-8'))

def initmotorstop():
    global targetmotor
    targetmotor = 6000
    lsb1 = targetmotor &0x7F
    msb1 = (targetmotor >> 7) & 0x7F

    cmd1 = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x00) + chr(lsb1) +chr(msb1)

    usb.write(cmd1.encode('utf-8'))

def initmotorturn():
    global targetmotorturn
    lsb1 = targetmotorturn &0x7F
    msb1 = (targetmotorturn >> 7) & 0x7F

    cmd1 = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x00) + chr(lsb1) +chr(msb1)

    usb.write(cmd1.encode('utf-8'))

def setMiddleheadlr():

    global targetHeadRL
    lsb1 = targetHeadRL &0x7F
    msb1 = (targetHeadRL >> 7) & 0x7F

    cmd1 = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x03) + chr(lsb1) +chr(msb1)

    usb.write(cmd1.encode('utf-8'))

def setMiddleheadud():

    global targetHeadUD
    lsb2 = targetHeadUD &0x7F
    msb2 = (targetHeadUD >> 7) & 0x7F

    cmd2 = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x04) + chr(lsb2) +chr(msb2)

    usb.write(cmd2.encode('utf-8'))

def setmiddlewaist():

    global targetwaist
    lsb3 = targetwaist &0x7F
    msb3 = (targetwaist >> 7) & 0x7F
    #waist is 2
    cmd3 = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x02) + chr(lsb3) +chr(msb3)

    usb.write(cmd3.encode('utf-8'))

def moveforward():
    global targetmotor

    int = targetmotor - 200
    targetmotor = int
    if targetmotor < 4900:
        targetmotor = 5000
    print("target: {}".format(targetmotor))
    #int = 8000
    lsb = int &0x7F
    msb = (int >> 7) & 0x7F

    cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x00) + chr(lsb) +chr(msb)

    print("writing")
    #usb.write(cmd.encode('utf-8'))
    #print("reading")
    usb.write(cmd.encode('utf-8'))
    time.sleep(.3)

def moveright():
    global targetmotor
    #int = targetmotor - 200
    #targetmotor = int
    print("target: {}".format(targetmotor))
    #int = 8000
    lsb = targetmotor &0x7F
    msb = (targetmotor >> 7) & 0x7F

    cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x01) + chr(lsb) +chr(msb)

    print("writing")
    #usb.write(cmd.encode('utf-8'))
    #print("reading")
    usb.write(cmd.encode('utf-8'))
    time.sleep(.3)
    targetmotor = 6000

def moveleft():
    global targetmotor
    #int = targetmotor + 200
    #targetmotor = int
    print("target: {}".format(targetmotor))
    #int = 8000
    lsb = targetmotor &0x7F
    msb = (targetmotor >> 7) & 0x7F

    cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x01) + chr(lsb) +chr(msb)

    print("writing")
    #usb.write(cmd.encode('utf-8'))
    #print("reading")
    usb.write(cmd.encode('utf-8'))
    time.sleep(.3)
    targetmotor = 6000

def moveback():
    global targetmotor
    int = targetmotor + 200
    targetmotor = int
    if targetmotor > 7100:
        targetmotor = 7000
    print("target: {}".format(targetmotor))
    #int = 8000
    lsb = int &0x7F
    msb = (int >> 7) & 0x7F

    cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x00) + chr(lsb) +chr(msb)

    print("writing")
    #usb.write(cmd.encode('utf-8'))
    #print("reading")
    usb.write(cmd.encode('utf-8'))
    time.sleep(.3)

def movewaistLeft():
    global targetwaist
    int = targetwaist + 900
    targetwaist = int
    if targetwaist > 8600:
        targetwaist = 8500
    print("target: {}".format(targetwaist))
    #int = 8000
    lsb = int &0x7F
    msb = (int >> 7) & 0x7F
#waist is 2
    cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x02) + chr(lsb) +chr(msb)

    print("writing")
    #usb.write(cmd.encode('utf-8'))
    #print("reading")
    usb.write(cmd.encode('utf-8'))
    time.sleep(.3)

    #return int

def movewaistRight():
    global targetwaist
    int = targetwaist - 900
    targetwaist = int
    if targetwaist < 4800:
        targetwaist = 4900
    #int2 = 3000
    lsb = int &0x7F
    msb = (int >> 7) & 0x7F
#waist is 2
    cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x02) + chr(lsb) +chr(msb)

    print("writing")
    #usb.write(cmd.encode('utf-8'))
    #print("reading")
    usb.write(cmd.encode('utf-8'))

    time.sleep(.3)

    #return int

def tiltHeadUp():
    global targetHeadUD
    int = targetHeadUD + 1000
    targetHeadUD = int
    if targetHeadUD > 8100:
        targetHeadUD = 8000
    #int2 = 3000
    lsb = int &0x7F
    msb = (int >> 7) & 0x7F

    cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x04) + chr(lsb) +chr(msb)

    print("writing")
    #usb.write(cmd.encode('utf-8'))
    #print("reading")
    usb.write(cmd.encode('utf-8'))

    time.sleep(.3)


def tiltHeadDown():
    global targetHeadUD
    int = targetHeadUD - 1000
    targetHeadUD = int
    if targetHeadUD < 3900:
        targetHeadUD = 4000
    #int2 = 3000
    lsb = int &0x7F
    msb = (int >> 7) & 0x7F

    cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x04) + chr(lsb) +chr(msb)

    print("writing")
    #usb.write(cmd.encode('utf-8'))
    #print("reading")
    usb.write(cmd.encode('utf-8'))

    time.sleep(.3)

def tiltHeadLeft():
    global targetHeadRL
    int = targetHeadRL + 1000
    targetHeadRL = int
    if targetHeadRL > 8100:
        targetHeadRL = 8000
    #int2 = 3000
    lsb = int &0x7F
    msb = (int >> 7) & 0x7F

    cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x03) + chr(lsb) +chr(msb)

    print("writing")
    #usb.write(cmd.encode('utf-8'))
    #print("reading")
    usb.write(cmd.encode('utf-8'))

    time.sleep(.3)

def tiltHeadRight():
    global targetHeadRL
    int = targetHeadRL - 1000
    targetHeadRL = int
    if targetHeadRL < 3900:
        targetHeadRL = 4000
    #int2 = 3000
    lsb = int &0x7F
    msb = (int >> 7) & 0x7F

    cmd = chr(0xaa) + chr(0xC) + chr(0x04) + chr (0x03) + chr(lsb) +chr(msb)

    print("writing")
    #usb.write(cmd.encode('utf-8'))
    #print("reading")
    usb.write(cmd.encode('utf-8'))

    time.sleep(.3)
