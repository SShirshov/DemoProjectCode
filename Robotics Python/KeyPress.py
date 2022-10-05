import pygame

def init():
    pygame.init()
    box = pygame.display.set_mode((100,100))

def getKey(keyName):

    ans = False

    for e in pygame.event.get():pass

    keystroke = pygame.key.get_pressed()

    myKey = getattr(pygame, 'K_{}'.format(keyName))

    if keystroke[myKey]:
        ans = True
        
    pygame.display.update()

    return ans

#def main():
    #if getKey('UP'):
        #print('key Up was pressed')
    #if getKey('DOWN'):
        #print('key Down was pressed')
    #if getKey('RIGHT'):
        #print('key Up was pressed')
    #if getKey('LEFT'):
        #print('key Down was pressed')


#if __name__ == '__main__':
    #init()
    #while True:
        #main()
