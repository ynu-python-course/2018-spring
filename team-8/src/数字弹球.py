# -*- coding: utf-8 -*-
import pygame,sys,math,random

def show_text(surface_handle, pos, text, color, font_bold = False, font_size = 13, font_italic = False): 
        cur_font = pygame.font.SysFont("宋体", 40)  
        cur_font.set_bold(font_bold)  
        cur_font.set_italic(font_italic)  
        text_fmt = cur_font.render(text, 1, color)   
        surface_handle.blit(text_fmt, pos)

class myball():

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.speed=[0,0]
        self.type=1
        self.hit=[0,0,0,0]

    def move(self):
        global balls
        pygame.draw.circle(screen,[255,255,255],[int(self.x),int(self.y)],r,0)
        if self.x<=r or self.x>=400-r:
            self.speed[0]= -self.speed[0]
            
        if self.y<=r:
            self.speed[1]= -self.speed[1]
                             
        self.x+=self.speed[0]
        self.y+=self.speed[1]
        
        pygame.draw.circle(screen,[255,0,0],[int(self.x),int(self.y)],r,0)

    def check(self):
        global ballnum
        global rs
        if int(self.x)%50==12 or int(self.x)%50==37 or int(self.y)%50==12 or int(self.y)%50==37:
            self.hit[0]=int((int(self.x))/50)
            self.hit[1]=int((int(self.y))/50)
            self.hit[2]=int((int(self.x))/50)
            self.hit[3]=int((int(self.y))/50)
            if int(self.x)%50==12and int((int(self.x))/50)>0:
                self.hit[0]-=1
                self.hit[2]-=1
                if int(self.y)%50<12and int((int(self.y))/50)>0:
                    self.hit[3]=self.hit[1]-1
                elif int(self.y)%50>37and int((int(self.y))/50)<12:
                    self.hit[3]=self.hit[1]+1
                    
            elif int(self.x)%50==37 and int((int(self.x))/50)<7:
                self.hit[0]+=1
                self.hit[2]+=1
                if int(self.y)%50<12and int((int(self.y))/50)>0:
                    self.hit[3]=self.hit[1]-1
                elif int(self.y)%50>37and int((int(self.y))/50)<12:
                    self.hit[3]=self.hit[1]+1
            if int(self.y)%50==12and int((int(self.y))/50)>0:
                self.hit[1]-=1
                self.hit[3]-=1
                if int(self.x)%50<12and int((int(self.x))/50)>0:
                    self.hit[2]=self.hit[0]-1
                elif int(self.x)%50>37and int((int(self.x))/50)<7:
                    self.hit[2]=self.hit[0]+1
            elif int(self.y)%50==37and int((int(self.y))/50)<12:
                self.hit[1]+=1
                self.hit[3]+=1
                if int(self.x)%50<12and int((int(self.x))/50)>0:
                    self.hit[2]=self.hit[0]-1
                elif int(self.x)%50>37and int((int(self.x))/50)<7:
                    self.hit[2]=self.hit[0]+1
            if self.hit[0]!=int((int(self.x))/50) and self.hit[1]!=int((int(self.y))/50):
                a=(self.hit[0]<int((int(self.x))/50)) and speed[0]<0
                b=(self.hit[0]>int((int(self.x))/50)) and speed[0]>0
                c=(self.hit[1]<int((int(self.y))/50)) and speed[1]<0
                d=(self.hit[1]>int((int(self.y))/50)) and speed[1]>0
                if (a or b)and(c or d):
                    if data[self.hit[1]][self.hit[0]]>0:
                        data[self.hit[1]][self.hit[0]]-=1
                        self.speed[0]=-self.speed[0]
                        self.speed[1]=-self.speed[1]
                        if data[self.hit[1]][self.hit[0]]>0:
                            pygame.draw.rect(screen,[0,0,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                            textnum = u"%d" % ( data[self.hit[1]][self.hit[0]])
                            show_text(screen, (self.hit[0]*50+12, self.hit[1]*50+12), textnum, (0, 255, 255), False)
                        else :
                            pygame.draw.rect(screen,[255,255,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                    elif data[self.hit[1]][self.hit[0]]==-1:
                        data[self.hit[1]][self.hit[0]]=0
                        pygame.draw.rect(screen,[255,255,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                        ballnum+=1
                        if data[self.hit[1]][self.hit[0]]==-2 and rs<3:
                            rs+=1
                elif c or d:
                    if self.speed[1]>0 and self.hit[1]<12:
                        self.hit[1]+=1
                    elif self.speed[1]<0 and self.hit[1]>0:
                        self.hit[1]-=1

                    if data[self.hit[1]][self.hit[0]]>0:
                        data[self.hit[1]][self.hit[0]]-=1
                        self.speed[1]=-self.speed[1]
                        if data[self.hit[1]][self.hit[0]]>0:
                            pygame.draw.rect(screen,[0,0,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                            textnum = u"%d" % ( data[self.hit[1]][self.hit[0]])
                            show_text(screen, (self.hit[0]*50+12, self.hit[1]*50+12), textnum, (0, 255, 255), False)
                            pass
                        else :
                            pygame.draw.rect(screen,[255,255,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                    elif data[self.hit[1]][self.hit[0]]==-1:
                        data[self.hit[1]][self.hit[0]]=0
                        pygame.draw.rect(screen,[255,255,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                        ballnum+=1
                        if data[self.hit[1]][self.hit[0]]==-2 and rs<3:
                            rs+=1
                            

                elif a or b:
                    if self.speed[0]>0 and self.hit[0]<7:
                        self.hit[0]+=1
                    elif self.speed[0]<0 and self.hit[0]>0:
                        self.hit[0]-=1
                        pass

                    if data[self.hit[1]][self.hit[0]]>0:
                        data[self.hit[1]][self.hit[0]]-=1
                        self.speed[0]=-self.speed[0]
                        if data[self.hit[1]][self.hit[0]]>0:
                            pygame.draw.rect(screen,[0,0,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                            textnum = u"%d" % ( data[self.hit[1]][self.hit[0]])
                            show_text(screen, (self.hit[0]*50+12, self.hit[1]*50+12), textnum, (0, 255, 255), False)
                        else :
                            pygame.draw.rect(screen,[255,255,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                    elif data[self.hit[1]][self.hit[0]]==-1:
                        data[self.hit[1]][self.hit[0]]=0
                        pygame.draw.rect(screen,[255,255,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                        ballnum+=1
                        if data[self.hit[1]][self.hit[0]]==-2 and rs<3:
                            rs+=1
                   

            elif data[self.hit[1]][self.hit[0]]>0:
                data[self.hit[1]][self.hit[0]]-=1
                if data[self.hit[1]][self.hit[0]]>0:
                    pygame.draw.rect(screen,[0,0,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                    textnum = u"%d" % ( data[self.hit[1]][self.hit[0]])
                    show_text(screen, (self.hit[0]*50+12, self.hit[1]*50+12), textnum, (0, 255, 255), False)
                else :
                    pygame.draw.rect(screen,[255,255,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)

                if self.hit[0]!=int((int(self.x))/50):
                    self.speed[0]=-self.speed[0]
                if self.hit[1]!=int((int(self.y))/50):
                    self.speed[1]=-self.speed[1]
            elif data[self.hit[1]][self.hit[0]]<=-1:
                data[self.hit[1]][self.hit[0]]=0
                pygame.draw.rect(screen,[255,255,255],[self.hit[0]*50+1,self.hit[1]*50+1,48,48],0)
                ballnum+=1
                if data[self.hit[1]][self.hit[0]]==-2 and rs<3:
                    rs+=1
            elif data[self.hit[3]][self.hit[2]]>0:
                data[self.hit[3]][self.hit[2]]-=1
                if data[self.hit[3]][self.hit[2]]>0:
                    pygame.draw.rect(screen,[0,0,255],[self.hit[2]*50+1,self.hit[3]*50+1,48,48],0)
                    textnum = u"%d" % ( data[self.hit[3]][self.hit[2]])
                    show_text(screen, (self.hit[2]*50+12, self.hit[3]*50+12), textnum, (0, 255, 255), False)
                else :
                    pygame.draw.rect(screen,[255,255,255],[self.hit[2]*50+1,self.hit[3]*50+1,48,48],0)

                if self.hit[0]!=int((int(self.x))/50):
                    self.speed[0]=-self.speed[0]
                if self.hit[1]!=int((int(self.y))/50):
                    self.speed[1]=-self.speed[1]
            elif data[self.hit[3]][self.hit[2]]<=-1:
                 data[self.hit[3]][self.hit[2]]=0
                 pygame.draw.rect(screen,[255,255,255],[self.hit[2]*50+1,self.hit[3]*50+1,48,48],0)
                 ballnum+=1
                 if data[self.hit[3]][self.hit[2]]==-2 and rs<3:
                    rs+=1

            
class dmap():
    def __init__(self,level):
        self.lel=level
        
    def up(self):
        for i in range(8):
            if data[11][i]!=0:
                screen.fill([255,255,255])
                textnum = u"You lose!" 
                show_text(screen, (300, 350), textnum, (255, 0, 0), False)
                pygame.display.flip()
                input()
                sys.exit()

        if self.lel<40:
            num=random.randint(1,3)
        elif self.lel<80:
            num=random.randint(1,int((int(self.lel))/10))
        else :
            num=random.randint(2,7)
        sample=random.sample([0,1,2,3,4,5,6,7],num)

        freebox=[]

        #下移
        for i in range(12,0,-1):
            for j in range(8):
                data[i][j]=data[i-1][j]
        
        #生成方块
        data[0]=[0,0,0,0,0,0,0,0]
        for i in sample:
            data[0][i]=self.lel

        #生成道具
        for i in range(8):
            if data[0][i]==0:
                freebox.append(i)
        sample=random.sample(freebox,1)
        
        if self.lel>30 and self.lel%10==0:
            data[0][sample[0]]=-2
        else :
            data[0][sample[0]]=-1
        screen.fill([255,255,255])
        pygame.draw.rect(screen,[0,0,0],[400,0,25,700],0)
        for i in range(13):
            for j in range(8):
                if data[i][j]>0:
                    pygame.draw.rect(screen,[0,0,255],[j*50+1,i*50+1,48,48],0)
                    textnum = u"%d" % (data[i][j])
                    show_text(screen, (j*50+12, i*50+12), textnum, (0, 255, 255), False)
                elif data[i][j]==-1:
                    pygame.draw.circle(screen,[255,0,255],[j*50+24,i*50+24],r,0)
                elif data[i][j]==-2:
                    screen.blit(image2,[j*50+1,i*50+1])
        textnum = u"lel:%d   ball:%d" % (self.lel,ballnum)
        show_text(screen, (450, 0), textnum, (0, 0, 0), False)
        textnum = u"Reading Steiner:%d" % (rs)
        show_text(screen, (450, 50), textnum, (0, 0, 0), False)


                    
pygame.init()
screen=pygame.display.set_mode([800,700])

pygame.mixer.init()
pygame.mixer.music.load("music.mp3") 

 
    

#图片加载
image2=pygame.image.load("道具2.jpg")
rect =image2.get_rect()

data=[]
datas=[]
for i in range(13):
    data.append([])
    datas.append([])
    for j in range(8):
        data[i].append(0)
        datas[i].append(0)
screen.fill([255,255,255])

pygame.draw.rect(screen,[255,255,255],[400,0,25,700],0)

x=200
xs=200
y=650
r=12
ballnum=1
ballnums=1
time=0
key=1
rs=1

type=[0,1,2]
speed=[1,1]
balls=[]
ball=myball(x,y)
balls.append(ball)

maps=dmap(1)
maps.up()

pygame.display.flip()
clock=pygame.time.Clock()
while True:

    if pygame.mixer.music.get_busy()==False:  
        pygame.mixer.music.play()  


    pygame.draw.circle(screen,[255,0,0],[int(balls[0].x),int(balls[0].y)],r,0)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            key=1
            press=pygame.mouse.get_pressed()
            if press[0]==1:
                x=0  
                mouse=pygame.mouse.get_pos()
                speed[0]=(mouse[0]-balls[0].x)/100
                speed[1]=(mouse[1]-balls[0].y)/100
                k=pow(1/(speed[0]*speed[0]+speed[1]*speed[1]),0.5)
                speed[0]=k*speed[0]
                speed[1]=k*speed[1]
                
                for i in balls:
                    i.speed[0]=speed[0]
                    i.speed[1]=speed[1]
                while key==1:
                    key=0
                    for i in range(len(balls)):
                        if i*40<=time:
                            if balls[i-1].y<=650:
                                balls[i-1].move()
                            if balls[i-1].y<650:
                            
                                balls[i-1].check()
                                key=1
                            elif x==0:
                                x=balls[i-1].x
                    #pygame.time.delay(2)
                    clock.tick(1000)
                    pygame.display.flip()
                    time+=1
                

                maps.lel+=1
                maps.up()

                for i in balls:
                    i.y=y
                    i.x=int(x)
            

            elif press[2]==1 and rs>0:
                rs-=1
                for i in range(13):
                    for j in range(8):
                        datas[i][j]=data[i][j]
                ballnums=ballnum
                xs=balls[0].x

                x=0
                mouse=pygame.mouse.get_pos()
                speed[0]=(mouse[0]-balls[0].x)/100
                speed[1]=(mouse[1]-balls[0].y)/100
                k=pow(1/(speed[0]*speed[0]+speed[1]*speed[1]),0.5)
                speed[0]=k*speed[0]
                speed[1]=k*speed[1]
                for i in balls:
                    i.speed[0]=speed[0]
                    i.speed[1]=speed[1]
                while key==1:
                    key=0
                
                    for i in range(len(balls)):
                        if i*40<=time:
                            if balls[i-1].y<=650:
                                balls[i-1].move()
                            if balls[i-1].y<650:
                            
                                balls[i-1].check()
                                key=1
                            elif x==0:
                                x=balls[i-1].x
                    time+=1
                ballnum=ballnums
                x=xs
                for i in balls:
                    i.x=int(x)
                    i.y=y


                for i in range(13):
                    for j in range(8):
                        if datas[i][j]!=0:
                            if data[i][j]==0:
                                data[i][j]=datas[i][j]
                                datas[i][j]=1
                            else :
                                data[i][j]=datas[i][j]
                                datas[i][j]=0
                screen.fill([255,255,255])
                pygame.draw.rect(screen,[0,0,0],[400,0,25,700],0)
                for i in range(13):
                    for j in range(8):
                        if data[i][j]>0:
                            if datas[i][j]!=1:
                                pygame.draw.rect(screen,[0,0,255],[j*50+1,i*50+1,48,48],0)
                            else :
                                pygame.draw.rect(screen,[100,0,100],[j*50+1,i*50+1,48,48],0)
                            textnum = u"%d" % (data[i][j])
                            show_text(screen, (j*50+12, i*50+12), textnum, (0, 255, 255), False)
                        elif data[i][j]==-1:
                            pygame.draw.circle(screen,[255,0,255],[j*50+24,i*50+24],r,0)
                        elif data[i][j]==-2:
                            screen.blit(image2,[j*50+1,i*50+1])

            pygame.draw.circle(screen,[255,255,255],[int(ball.x),int(ball.y)],r,0)

            while ballnum>len(balls):
                ball=myball(int(x),y)
                balls.append(ball)
            if key==0:
                x=0
                time=0
        textnum = u"lel:%d   ball:%d" % (maps.lel,ballnum)
        show_text(screen, (450, 0), textnum, (0, 0, 0), False)
        textnum = u"Reading Steiner:%d" % (rs)
        show_text(screen, (450, 50), textnum, (0, 0, 0), False)
    pygame.time.delay(10)
    pygame.display.flip()