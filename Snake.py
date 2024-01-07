from pygame import*
from random import randint

init()
dis=display.set_mode((1000,500))
dis.fill("MAROON")
display.update()
display.set_caption("Snake Lar Lar")
running=True
x1=500
y1=250
x1_change=0
y1_change=0
snakelist=[]
snakelength=4
snakespeed=10
clock=time.Clock()
def snake(snakelist):
    for x in snakelist:
        draw.rect(dis,"RED",[x[0],x[1],30,30])
foodx=randint(20,980)
foody=randint(20,500)
poisonx=randint(20,980)
poisony=randint(20,500)
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==KEYDOWN:
            if e.key==K_LEFT:
                x1_change=-10
                y1_change=0
            elif e.key==K_RIGHT:
                x1_change=10
                y1_change=0
            elif e.key==K_UP:
                x1_change=0
                y1_change=-10
            elif e.key==K_DOWN:
                x1_change=0
                y1_change=10
    x1+=x1_change
    y1+=y1_change
    dis.fill("MAROON")
    draw.rect(dis,"RED",[x1,y1,30,30])
    draw.rect(dis,"GREEN",[foodx,foody,30,30])
    draw.rect(dis,"PURPLE",[poisonx,poisony,30,30])
    snakehead=[]
    snakehead.append(x1)
    snakehead.append(y1)
    snakelist.append(snakehead)
    if len(snakelist)>(snakelength):
        del snakelist[0]
    for i in snakelist[:-1]:
        if i == snakehead:
            gameover=True

    snake(snakelist)
    display.update()
    if x1>=foodx-15 and x1<=foodx+15 and y1>=foody-15 and y1<=foody+15:
        foodx=randint(20,980)
        foody=randint(20,500)
        snakelength+=2
        snakespeed+=5
    if x1>=poisonx-15 and x1<=poisonx+15 and y1>=poisony-15 and y1<=poisony+15:
        poisonx=randint(20,980)
        poisony=randint(20,500)
        snakelength-=2
        snakespeed-=5
    clock.tick(snakespeed)
quit()

