from tkinter import *
window=Tk()
window.geometry('500x500')

equation =''
def button_press(num): 
    global equation
    equation=equation+str(num)
    equation_label.set(equation)
def sum1():
    global equation
    equation=equation+str('+')
    equation_label.set(equation)
def dif1():
    global equation
    equation=equation+str('-')
    equation_label.set(equation)
    
def mul1():
    global equation
    equation=equation+str('*')
    equation_label.set(equation)
def div1():
    global equation
    equation=equation+str('/')
    equation_label.set(equation)
def dot1():
    global equation
    equation=equation+str('.')
    equation_label.set(equation)
def clear1():
    global equation
    equation=''
    equation_label.set(equation)    
def equal1():
    global equation
    try:
        result=str(eval(equation))
        equation_label.set(result)
        equation=str(result)
    except ZeroDivisionError :
         equation_label.set('Arthematic Error')
         equation=''
    except SyntaxError :
         equation_label.set('Syntax Error')
         equation=''
  

equation_label=StringVar()
label_show=Label(window,textvariable=equation_label,font=('arial',20,'bold'),width=50,fg='black',bg='white')
label_show.pack()
frame=Frame(window)
frame.pack()
b1=Button(frame,text='1',font=('arial',20,'bold'),height=2,width=5,command=lambda : button_press(1))
b1.grid(row=0,column=0)
b2=Button(frame,text='2',font=('arial',20,'bold'),height=2,width=5,command=lambda : button_press(2))
b2.grid(row=0,column=1)
b3=Button(frame,text='3',font=('arial',20,'bold'),height=2,width=5,command=lambda : button_press(3))
b3.grid(row=0,column=2)
b4=Button(frame,text='4',font=('arial',20,'bold'),height=2,width=5,command=lambda : button_press(4))
b4.grid(row=1,column=0)
b5=Button(frame,text='5',font=('arial',20,'bold'),height=2,width=5,command=lambda : button_press(5))
b5.grid(row=1,column=1)
b6=Button(frame,text='6',font=('arial',20,'bold'),height=2,width=5,command=lambda : button_press(6))
b6.grid(row=1,column=2)
b7=Button(frame,text='7',font=('arial',20,'bold'),height=2,width=5,command=lambda : button_press(7))
b7.grid(row=2,column=0)
b8=Button(frame,text='8',font=('arial',20,'bold'),height=2,width=5,command=lambda : button_press(8))
b8.grid(row=2,column=1)
b9=Button(frame,text='9',font=('arial',20,'bold'),height=2,width=5,command=lambda : button_press(9))
b9.grid(row=2,column=2)
add=Button(frame,text='+',font=('arial',20,'bold'),height=2,width=5,command=sum1)
add.grid(row=0,column=3)
sub=Button(frame,text='-',font=('arial',20,'bold'),height=2,width=5,command=dif1)
sub.grid(row=1,column=3)
mul=Button(frame,text='X',font=('arial',20,'bold'),height=2,width=5,command=mul1)
mul.grid(row=2,column=3)
div=Button(frame,text='/',font=('arial',20,'bold'),height=2,width=5,command=div1)
div.grid(row=3,column=3)
equal=Button(frame,text='=',font=('arial',20,'bold'),height=2,width=5,command=equal1)
equal.grid(row=3,column=0)
b0=Button(frame,text='0',font=('arial',20,'bold'),height=2,width=5,command=lambda : button_press(0))
b0.grid(row=3,column=1)
dot=Button(frame,text='.',font=('arial',20,'bold'),height=2,width=5,command=dot1)
dot.grid(row=3,column=2)
clear=Button(frame,text='clear',font=('arial',20,'bold'),height=1,width=20,command=clear1)
clear.grid(row=4,column=0,columnspan=4)

window.mainloop()