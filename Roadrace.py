import pygame
import random
import math

pygame.init()
pygame.mixer.init()
red=(255,0,0)
SCORE=0
li=[r'img\car1.png',r'img\car2.png',r'img\car4.png',r'img\car5.png',r'img\car6.png',r'img\car7.png',r'img\car8.png',r'img\car9.png',r'img\car10.png',r'img\car11.png',r'img\car12.png']
j=[110,170,230]
k=[110,170,230]
Speed=6
FPS =40
clock=pygame.time.Clock()
FX=0
FY=0
F2Y=-600
PX=170
PY=400
W=60
H=100
font = pygame.font.SysFont('comicsans',44)
highsocer = pygame.font.SysFont('comicsans',88)
#Enemy Car X and Y
EX = j[random.randint(0,2)]
EY = -100
EX1=k[random.randint(0,2)]
EY1=-300
i=random.randint(0,10)
p=random.randint(0,10)


############################################################################
gamewindo = pygame.display.set_mode((400,600))

Frame=pygame.image.load(r'img\road.png')
Frame=pygame.transform.scale(Frame,(400,600)).convert_alpha()
Frame2=pygame.image.load(r'img\road.png')
Frame2=pygame.transform.scale(Frame2,(400,600)).convert_alpha()

Car = pygame.image.load(r'img\car3.png')
Car = pygame.transform.scale(Car,(W,H)).convert_alpha()

############################################################################

def HighScore():
     startwindo=pygame.display.set_mode((400,600))
     pygame.display.set_caption("Cars")
     SF = pygame.image.load(r'img\road.png')
     SF = pygame.transform.scale(SF,(400,600)).convert_alpha()
     GAME=True
     scor=highsocer.render(str(SCORE),True,red)
     high=highsocer.render("YOUR SCORE ",True,red)
     while GAME:
    
   
         startwindo.blit(SF,(0,0))
         
         startwindo.blit(high,[0,200])
        
         startwindo.blit(scor,[180,300])
    
         for event in pygame.event.get():
        
        
             if event.type==pygame.QUIT:
                 pygame.quit()
                 quit()
             if event.type==pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                       GAME = False
          
             pygame.display.update()
    
     pygame.quit()
     quit()

def Start():
     startwindo=pygame.display.set_mode((400,600))
     pygame.display.set_caption("Cars")
     SF = pygame.image.load(r'img\Start.png')
     SF = pygame.transform.scale(SF,(400,600)).convert_alpha()
     GAME=True
    
     while GAME:
    
   
         startwindo.blit(SF,(0,0))
    
         for event in pygame.event.get():
        
        
             if event.type==pygame.QUIT:
                 pygame.quit()
                 quit()
             if event.type==pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                       GAME = False
          
             pygame.display.update()



def text_screen(text,color,x,y):
    screen_text=font.render(text, True, color)
    gamewindo.blit(screen_text,[x,y])



def Check(Carx,Cary,Ecarx,Ecary,E1x,E1y):
    global SCORE
    distance = math.sqrt((math.pow(Carx-Ecarx,2)) +( math.pow(Cary-Ecary,2)))
    dis =math.sqrt((math.pow(Carx-E1x,2))+(math.pow(Cary-E1y,2)))
    if (distance<90.0 and Carx==Ecarx) or (dis<90.0 and Carx==E1x) :
      # pygame.mixer.music.load('bomb.mp3')
      # pygame.mixer.music.play()
       BL=pygame.image.load(r'img\blast.png')
       BL=pygame.transform.scale(BL,(60,100)).convert_alpha()
       gamewindo.blit(Frame,(FX,FY))
       gamewindo.blit(Frame2,(FX,F2Y))
       gamewindo.blit(BL,(PX-20,PY))
       gamewindo.blit(ECar,(EX,EY))
       gamewindo.blit(ECar2,(EX1,EY1))
       text_screen('Score : '+str(SCORE),red,5,5)
       pygame.display.update()
       pygame.time.wait(200)
       
       
       HighScore()
############################################################################
Start()
E=True
while E:
   # pygame.mixer.music.load('f1.mp3')
   # pygame.mixer.music.play()
    pygame.display.update()
    if (SCORE+1)%5==0:
        Speed=Speed+1
        SCORE=SCORE+1
    ECar= pygame.image.load(li[i])
    ECar= pygame.transform.scale(ECar,(W,H)).convert_alpha()

    ECar2 = pygame.image.load(li[p])
    ECar2 = pygame.transform.scale(ECar2,(W,H)).convert_alpha()
    
    gamewindo.blit(Frame,(FX,FY))
    gamewindo.blit(Frame2,(FX,F2Y))
    gamewindo.blit(Car,(PX,PY))
    gamewindo.blit(ECar,(EX,EY))
    gamewindo.blit(ECar2,(EX1,EY1))
    text_screen('Score : '+str(SCORE),red,5,5)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            E=False
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if PX <229:
                    PX=PX+60
                    
                    
            if event.key == pygame.K_LEFT:
                 if PX>111:
                     PX=PX-60
                     
            if event.key == pygame.K_UP:
                 Speed=Speed+1
            if event.key == pygame.K_DOWN:
                 if Speed>2:
                     Speed=Speed-1
            

    pygame.display.update()
    clock.tick(FPS)
    FY=FY+Speed
    F2Y=F2Y+Speed
    EY1=EY1+(Speed-2)
    EY=EY+(Speed-2)
    if FY>605:
        FY=-600
    if F2Y>605:
        F2Y=-600
    
    if EY>605:
        EY=-100
        SCORE=SCORE+1
        i=random.randint(0,10)
        EX = j[random.randint(0,2)]
    
    if EY1>690:
        EY1=-100
        SCORE=SCORE+1
        p=random.randint(0,10)
        EX1 = j[random.randint(0,2)]
    Check(PX,PY,EX,EY,EX1,EY1)
pygame.quit()
