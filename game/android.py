#640,800
import random
import pygame
import time
pygame.init()#for initialising 
screen = pygame.display.set_mode((1400,800))
width = 1400
height = 160
background = pygame.image.load("anbac.png")
white = (255,255,255)
tree = pygame.image.load("toptree.png")
pipe = pygame.image.load("trepipe.png")
font = pygame.font.SysFont(None,43)
brick = pygame.image.load("brick.png")
player = pygame.image.load("play.png")
close = False
black = (0,0,0)
apple = pygame.image.load("apple.png")
#rapplex = round(random.randr)
rApplex = round(random.randrange(0,width-50)/20.0)*20.0
rAppley = round(random.randrange(0,height-50)/20.0)*20.0

Applex = round(random.randrange(0,width-60)/20.0)*20.0
Appley = round(random.randrange(0,height-60)/20.0)*20.0
pplex = round(random.randrange(0,width-70)/20.0)*20.0
ppley = round(random.randrange(0,height-70)/20.0)*20.0
plex = round(random.randrange(0,width-80)/20.0)*20.0
pley = round(random.randrange(0,height-80)/20.0)*20.0
def message(msg,color):
    screen_text = font.render(msg,True,color)
    screen.blit(screen_text,[300,300])

#def score(msg,color):
 #   screen_text = font.render(msg,True,color)
  #  screen.blit(screen_text,[500,310])
def scoring(msg,color):
    screen_text = font.render(msg,True,color)
    screen.blit(screen_text,[600,70])
    
s_x =700 
s_y = 650
s_y1=650
s_y2=650
s_y3=650
s_y4=650
s_y5=650
s_y6=650
s_y7=650
s_y8=650
s_y9=650
s_y10=650
s_y11=650
s_y12=650
s_y13=650
s_y14=650
s_y15=650
score = 0
high_score = 0
scores = []
def apped():
    pass

while not close:
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                close = True
            elif event.key == pygame.K_e:
                close = True
            elif event.key == pygame.K_LEFT:
                
                s_x -=20
                s_x -=20
                s_x -=20
            elif event.key == pygame.K_RIGHT:
                s_x+=20
                s_x+=20
                s_x+=20
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                s_x -=5
                s_x -=5
                s_x -=5
            elif event.key  == pygame.K_RIGHT:
                s_x+=5
                s_x+=5
                s_x+=5
    if s_x>1400 or s_x==1400 or s_x<0 or s_x==10:
        pass
    screen.blit(background,[0,0])
   
    screen.blit(pipe,[100,0])
    screen.blit(pipe,[650,0])
    screen.blit(pipe,[1200,0])
    screen.blit(tree,[0,0])   
    screen.blit(brick,[0,s_y])   
    screen.blit(brick,[92,s_y1])   
    screen.blit(brick,[184,s_y2])   
    screen.blit(brick,[276,s_y3])   
    screen.blit(brick,[368,s_y4])   
    screen.blit(brick,[460,s_y5])   
    screen.blit(brick,[552,s_y6])   
    screen.blit(brick,[644,s_y7])   
    screen.blit(brick,[736,s_y8])   
    screen.blit(brick,[828,s_y9])   
    screen.blit(brick,[920,s_y10])   
    screen.blit(brick,[1012,s_y11])   
    screen.blit(brick,[1104,s_y12])   
    screen.blit(brick,[1196,s_y13])   
    screen.blit(brick,[1288,s_y14])   
    screen.blit(brick,[1380,s_y15])   
    screen.blit(player,[s_x,549])   
    were = pygame.draw.rect(screen,white,[400,50,700,60],4)
    #were.write(f"your score:{score} High score{high_score}",font=("Courier",24,"normal"))
    #"score: 0 high score: 0",align="center",font=("Courier",24,"normal")
    
    apple1 = screen.blit(apple,[rApplex,rAppley])
   
    rAppley+=5
    
    
    """
    screen.blit(apple,[Applex,Appley])
    apple2 = screen.blit(apple,[rApplex,rAppley])
    Appley+=6
    Appley+=6
    Appley+=6
    
    screen.blit(apple,[plex,pley])
    apple3 = screen.blit(apple,[rApplex,rAppley])
    pley+=3
    pley+=3
    pley+=3
    
    screen.blit(apple,[pplex,ppley])
    apple4 = screen.blit(apple,[rApplex,rAppley])
    ppley+=1
    ppley+=1
    ppley+=1
    """
    
    if rAppley==650 and (rApplex>0 and rApplex<92):
        s_y +=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>92 and rApplex<184):
        s_y1+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>184 and rApplex<276):
        s_y2+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>276 and rApplex<368):
        s_y3+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>368 and rApplex<460):
        s_y4+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>460 and rApplex<552):
        s_y5+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>552 and rApplex<644):
        s_y6+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>644 and rApplex<736):
        s_y7+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>736 and rApplex<828):
        s_y8+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>828 and rApplex<920):
        s_y9+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>920 and rApplex<1012):
        s_y10+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>1012 and rApplex<1104):
        s_y11+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>1104 and rApplex<1196):
        s_y12+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>1196 and rApplex<1288):
        s_y13+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0
   
    elif rAppley==650 and (rApplex>1288 and rApplex<1380):
        s_y14+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif rAppley==650 and (rApplex>1380 and rApplex<1400):
        s_y15+=1000
        apped()
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

        apple1 = screen.blit(apple,[rApplex,rAppley])
        rAppley+=10
        
    
    
    
    elif (rAppley>540 and rAppley<650) and (s_x>0 and s_x<125) and (rApplex>0 and rApplex<125):
        rAppley-=10000
        
        score+=10
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif (rAppley>540 and rAppley<650) and (s_x>125 and s_x<250) and (rApplex>125 and rApplex<250):
        
        rAppley-=10000
        score+=10
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif (rAppley>540 and rAppley<650) and (s_x>250 and s_x<375) and (rApplex>250 and rApplex<375):
        rAppley-=10000
        score+=10
        
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif (rAppley>540 and rAppley<650) and (s_x>375 and s_x<500) and (rApplex>375 and rApplex<500):
        rAppley-=10000
        
        score+=10
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif (rAppley>540 and rAppley<650) and (s_x>500 and s_x<625) and (rApplex>500 and rApplex<625):
        rAppley-=10000
        
        score+=10
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif (rAppley>540 and rAppley<650) and (s_x>625 and s_x<750) and (rApplex>625 and rApplex<750):
        rAppley-=10000
        
        score+=10
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif (rAppley>540 and rAppley<650) and (s_x>750 and s_x<875) and (rApplex>750 and rApplex<875):
        rAppley-=10000
        
        score+=10
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif (rAppley>540 and rAppley<650) and (s_x>875 and s_x<1000) and (rApplex>875 and rApplex<1000):
        rAppley-=10000
        
        score+=10
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif (rAppley>540 and rAppley<650) and (s_x>1000 and s_x<1125) and (rApplex>1000 and rApplex<1125):
        rAppley-=10000
        
        score+=10
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif (rAppley>540 and rAppley<650) and (s_x>1125 and s_x<1250) and (rApplex>1125 and rApplex<1250):
   
        rAppley-=10000
        
        score+=10
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0

    elif (rAppley>540 and rAppley<650) and (s_x>1250 and s_x<1390) and (rApplex>1250 and rApplex<1390):
   
        rAppley-=10000
        
        score+=10
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0
        
    elif s_y==1650 and s_y1==1650 and s_y2==1650 and s_y3==1650 and s_y4==1650 and s_y5==1650 and s_y6==1650 and s_y7==1650 and s_y8==1650 and s_y9==1650 and s_y10==1650 and s_y11==1650 and s_y12==1650 and s_y13==1650 and s_y14==1650 and s_y15==1650:
        close = True
    
    elif rAppley>640 and rAppley<800:
        
        rApplex = round(random.randrange(0,width-50)/20.0)*20.0
        rAppley = round(random.randrange(0,height-50)/20.0)*20.0
        
    elif score==0 and high_score==0:
        score=high_score
    elif score>high_score:
        high_score=score
    
    scoring(f"your score {score} High score {high_score}",black)
    pygame.display.update()

pygame.display.update()
pygame.quit()#for quiting the game







quit()




















