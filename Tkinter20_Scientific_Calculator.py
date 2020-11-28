def on_click(event):
    global screen_val
    text=event.widget.cget("text")  #TODO:By using event.widget we can get that button and cget() is used to get text on that button
    val=screen_val.get()           #TODO:To get value from the screen
    result=''

    if text=="=":
        if screen_val.get().isdigit():
            result=int(val)
        else:
            try:
                result=eval(screen_val.get())
            except Exception as e:
                print(e)
                result="Error"

        screen_val.set(result)
        screen.update()

    elif text=="C":  #TODO:To Cler The screen
        screen_val.set("")
        screen.update()

    elif text=="DEL":
        last = val[:len(val) - 1]  #TODO:here we decrement the val(this val variable stores screen values as a string) string by 1
        screen_val.set(last)
        screen.update()

    elif text=="lg":
        if screen_val.get().isdigit():
            result=str(m.log10(float(val)))
        else:
            try:
                val = eval(screen_val.get())
                result = str(m.log10(float(val)))

            except Exception as e:
                print(e)
                result= "Error"
        screen_val.set(result)
        screen.update()

    elif text=="ln":
        if screen_val.get().isdigit():
            result=str(m.log(float(val)))
        else:
            try:
                val = eval(screen_val.get())
                result = str(m.log(float(val)))
            except Exception as e:
                print(e)
                result= "Error"
        screen_val.set(result)
        screen.update()

    elif text=="1/x":
        if screen_val.get().isdigit():
            result=str(1/(float(val)))
        else:
            try:
                val = eval(screen_val.get())
                result = str(1 / (float(val)))
            except Exception as e:
                print(e)
                result= "Error"
        screen_val.set(result)
        screen.update()

    elif text=="deg":
        if screen_val.get().isdigit():
            result=str(m.degrees(float(val)))
        else:
            try:
                val = eval(screen_val.get())
                result = str(m.degrees(float(val)))
            except Exception as e:
                print(e)
                result= "Error"
        screen_val.set(result)
        screen.update()

    elif text=="sin":
        if screen_val.get().isdigit():
            result=str(m.sin(float(val)))
        else:
            try:
                val = eval(screen_val.get())
                result=str(m.sin(float(val)))
            except Exception as e:
                print(e)
                result = "Error"
        screen_val.set(result)
        screen.update()

    elif text=="sqrt":
        if screen_val.get().isdigit():
            result=str(m.sqrt(float(val)))
        else:
            try:
                val = eval(screen_val.get())
                result = str(m.sqrt(float(val)))
            except Exception as e:
                print(e)
                result = "Error"
        screen_val.set(result)
        screen.update()

    elif text=="x!":
        if screen_val.get().isdigit():
            result = str(m.factorial(float(val)))
        else:
            try:
                val = eval(screen_val.get())
                result = str(m.factorial(float(val)))
            except Exception as e:
                print(e)
                result = "Error"
        screen_val.set(result)
        screen.update()

    #TODO:Different Logic
    elif text=="pi":
        if val=="":
            result=str(m.pi)
        else:
            result=str(float(val) * m.pi)
        screen_val.set(result)
        screen.update()
    elif text=="e":
        if val=="":
            result=str(m.e)
        else:
            result=str(m.e ** float(val))
        screen_val.set(result)
        screen.update()

    elif text=="cos":
        if screen_val.get().isdigit():
            result = str(m.cos(float(val)))
        else:
            try:
                val = eval(screen_val.get())
                result = str(m.cos(float(val)))
            except Exception as e:
                print(e)
                result = "Error"
        screen_val.set(result)
        screen.update()

    elif text=="tan":
        if screen_val.get().isdigit():
            result = str(m.tan(float(val)))
        else:
            try:
                val = eval(screen_val.get())
                result = str(m.tan(float(val)))
            except Exception as e:
                print(e)
                result = "Error"
        screen_val.set(result)
        screen.update()

    else:
        screen_val.set(screen_val.get()+text)
        screen.update()

    if result == "Error":
        screen.configure(background="red")
        ans = tmsg.showerror("Error!", "Wrong Input")
        screen.update()
        if ans == "ok":
            screen.configure(background="white")
            screen_val.set("")


from tkinter import *
import tkinter.messagebox as tmsg
import math as m
root=Tk()
root.title("Calculator")
root.wm_iconbitmap("calculator_2.ico")
root.geometry("600x600")
root.configure(background="black")

#TODO:To Make Screen
screen_val=StringVar()
screen_val.set("")
screen=Entry(root,textvariable=screen_val,font="lucida 35 bold",relief=RIDGE,borderwidth=8,bg="white")
screen.pack(fill=X,padx=10,pady=10,ipadx=8)

#TODO:List Of attributes in frames
cal_list=["C","%","/","*","lg","9","8","7","-","ln","6","5","4","1/x","deg","3","2","1","+","sin","sqrt","x!","pi","e","cos","0",".","DEL","=","tan"]

#TODO:Making Buttons In Frames
frame = Frame(root,bg="white")
k=0
for i in cal_list:
    b = Button(frame, text=i, fg="red", padx=35, width=1,pady=10, font="lucida 20 bold")
    b.grid(row=k//5,column=k%5,padx=5,pady=5)
    k=k+1
    b.bind("<Button-1>", on_click)

frame.pack()
root=mainloop()