import tkinter as tk
import random,math,sys
root = tk.Tk()
root.title("game")
root.geometry("800x600+350+90")
#paixu
lists=[]

for i in range(0,6):

    child_list=[]

    for j in range(0,6):

        x=random.choice("ggrrr")

        child_list.append(x)

    lists.append(child_list)
A = []
B = []
x = 0
n = 0
for i in lists:
    for j in i:
        if j == 'g':
            x = x + 1
        if j == 'r':
            if x != 0:
                A.append(x)
                x = 0
    if x != 0:        
        A.append(x)
    x = 0
    for a in A:
        if a == 0:
            A.remove(0) 
    m = len(A)
    for z in range(0,m):
        n = n + A[z]*pow(10,m-z-1)
    B.append(n)
    n = 0
    A = []
C = []
D = []
for j in range(0,6):
    for i in range(0,6):
        if lists[i][j] == 'g':
            x = x + 1
        if lists[i][j] == 'r':
            if x != 0:
                C.append(x)
                x = 0
    if x != 0:        
        C.append(x)
    x = 0
    for c in C:
        if c == 0:
            C.remove(0) 
    m = len(C)
    for z in range(0,m):
        n = n + C[z]*pow(10,m-z-1)
    D.append(n)
    n = 0
    C = []


for x in range(0,6):
    tk.Label(root,text="{}".format(D[x])).grid(row=0,column=x+1)
for y in range(0,6):
    tk.Label(root,text="{}".format(B[y])).grid(row=y+1,column=0)
imgg=tk.PhotoImage(file="green3.png")
imgr=tk.PhotoImage(file="red3.png")
gameover=3    
def change_image(nbt,w):
    global imgg
    global imgr
    global gameover
    global oppo
    if w == "g" and gameover > 0:
        nbt.config(image=imgg)
    elif w == "r" and gameover > 0:
        nbt.config(image=imgr)
        gameover=gameover-1
    if gameover <= 0:
        oppo.config(text="end")

def the_end():
    sys.exit()


img=tk.PhotoImage(file="first.png")     #使用循环创建每一个button

oppo=tk.Button(width=10,height=4,text='go on',command = the_end)
oppo.grid(row=1,column=8)
#a
a1=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(a1,lists[0][0]))
a1.grid(row=1,column=1)
a2=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(a2,lists[0][1]))
a2.grid(row=1,column=2)
a3=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(a3,lists[0][2]))
a3.grid(row=1,column=3)
a4=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(a4,lists[0][3]))
a4.grid(row=1,column=4)
a5=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(a5,lists[0][4]))
a5.grid(row=1,column=5)
a6=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(a6,lists[0][5]))
a6.grid(row=1,column=6)
#b
b1=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(b1,lists[1][0]))
b1.grid(row=2,column=1)
b2=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(b2,lists[1][1]))
b2.grid(row=2,column=2)
b3=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(b3,lists[1][2]))
b3.grid(row=2,column=3)
b4=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(b4,lists[1][3]))
b4.grid(row=2,column=4)
b5=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(b5,lists[1][4]))
b5.grid(row=2,column=5)
b6=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(b6,lists[1][5]))
b6.grid(row=2,column=6)

#c
c1=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(c1,lists[2][0]))
c1.grid(row=3,column=1)
c2=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(c2,lists[2][1]))
c2.grid(row=3,column=2)
c3=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(c3,lists[2][2]))
c3.grid(row=3,column=3)
c4=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(c4,lists[2][3]))
c4.grid(row=3,column=4) 
c5=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(c5,lists[2][4]))
c5.grid(row=3,column=5)
c6=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(c6,lists[2][5]))
c6.grid(row=3,column=6)

#d
d1=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(d1,lists[3][0]))
d1.grid(row=4,column=1)
d2=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(d2,lists[3][1]))
d2.grid(row=4,column=2)
d3=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(d3,lists[3][2]))
d3.grid(row=4,column=3)
d4=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(d4,lists[3][3]))
d4.grid(row=4,column=4) 
d5=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(d5,lists[3][4]))
d5.grid(row=4,column=5)
d6=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda :change_image(d6,lists[3][5]))
d6.grid(row=4,column=6)
 

e1=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(e1,lists[4][0]))
e1.grid(row=5,column=1)
e2=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(e2,lists[4][1]))
e2.grid(row=5,column=2)
e3=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(e3,lists[4][2]))
e3.grid(row=5,column=3)
e4=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(e4,lists[4][3]))
e4.grid(row=5,column=4)
e5=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(e5,lists[4][4]))
e5.grid(row=5,column=5)
e6=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(e6,lists[4][5]))
e6.grid(row=5,column=6)

f1=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(f1,lists[5][0]))
f1.grid(row=6,column=1)
f2=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(f2,lists[5][1]))
f2.grid(row=6,column=2)
f3=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(f3,lists[5][2]))
f3.grid(row=6,column=3)
f4=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(f4,lists[5][3]))
f4.grid(row=6,column=4)
f5=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(f5,lists[5][4]))
f5.grid(row=6,column=5)
f6=tk.Button(root,width=78,height=78,bitmap="gray50",image=img,command=lambda : change_image(f6,lists[5][5]))
f6.grid(row=6,column=6)



root.mainloop()

