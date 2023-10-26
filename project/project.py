#importing tkinter and math libraries
from tkinter import*
import math
from tkinter import messagebox
#declaring variables
root=Tk()#root variable creates window

#variables for inputting values
a_var=IntVar()
b_var=IntVar()
c_var=IntVar()
n_var=IntVar()

#variables for outputting values
first_ans=StringVar()
second_ans=StringVar()
third_ans=StringVar()
fourth_ans=StringVar()

#function for finding 10-adic number roots that shows first 10 digits 
def func():
    #getting values from the entry fields
    a=a_var.get()
    b=b_var.get()
    c=c_var.get()   
    #checking the quadratic equation
    if a==0:
        messagebox.showerror("Қате","a-ның басқа мәнің жазыңыз")
    elif b==0:
        messagebox.showerror("Қате","b-ның басқа мәнің жазыңыз")
    elif c==0:
        messagebox.showerror("Қате","c-ның басқа мәнің жазыңыз")
    else:
        d=math.gcd(b,c)
        d=math.gcd(a,d)
        a=a/d
        b=b/d
        c=c/d
        ans =[]
        ans2=[]
        ans3=[]
        ans4=[]
        for i in range (1,11):
            if i==1:
                    for x in range(0,10):
                        y=a*(x**2)+b*x+c
                        if y%10==0:
                            if len(ans)==0:
                                ans.insert(0,x)
                            elif len(ans2)==0:
                                ans2.insert(0,x)
                            elif len(ans3)==0:
                                ans3.insert(0,x)
                            else:
                                ans4.insert(0,x)   
            #finding all answers to quadratic equation                     
            else:
                if len(ans)==i-1:
                    r=''.join(map(str, ans))
                    r=int(r)
                    z=a*(r**2)+b*r+c
                    z=z/(10**(i-1))
                    z=int(z)
                    coef=2*a*ans[-1]+b
                    coef=coef%10
                    coef=int(coef)
                    d=math.gcd(coef,z)
                    coef=coef/d
                    z=z/d
                    for x in range(0,10):
                        y=z+coef*x
                        if y%10==0:
                            ans.insert(0,x)
                if len(ans2)==i-1:
                    r=''.join(map(str, ans2))
                    r=int(r)
                    z=a*(r**2)+b*r+c
                    z=z/(10**(i-1))
                    z=int(z)
                    coef=2*a*ans2[-1]+b
                    coef=coef%10
                    coef=int(coef)
                    d=math.gcd(coef,z)
                    coef=coef/d
                    z=z/d
                    for x in range(0,10):
                        y=z+coef*x
                        if y%10==0:
                            ans2.insert(0,x)
                if len(ans3)==i-1:
                    r=''.join(map(str, ans3))
                    r=int(r)
                    z=a*(r**2)+b*r+c
                    z=z/(10**(i-1))
                    z=int(z)
                    coef=2*a*ans3[-1]+b
                    coef=coef%10
                    coef=int(coef)
                    d=math.gcd(coef,z)
                    coef=coef/d
                    z=z/d
                    for x in range(0,10):
                        y=z+coef*x
                        if y%10==0:
                            ans3.insert(0,x)  
                if len(ans4)==i-1:
                    r=''.join(map(str, ans4))
                    r=int(r)
                    z=a*(r**2)+b*r+c
                    z=z/(10**(i-1))
                    z=int(z)
                    coef=2*a*ans4[-1]+b
                    coef=coef%10
                    coef=int(coef)
                    d=math.gcd(coef,z)
                    coef=coef/d
                    z=z/d
                    for x in range(0,10):
                        y=z+coef*x
                        if y%10==0:
                            ans4.insert(0,x)
        #checking the length of answers,if they are not equal,then solution does not exist
        q=len(ans)==10
        q2=len(ans2)==10
        q3=len(ans3)==10
        q4=len(ans4)==10
        if q or q2 or q3 or q4:
            if len(ans)==10:
                y=''.join(map(str, ans))
                first_ans.set("..."+y)
            if len(ans2)==10:
                y=''.join(map(str, ans2))
                second_ans.set("..."+y)
            else:
                second_ans.set('zhok')
            if len(ans3)==10:
                y=''.join(map(str, ans3))
                third_ans.set("..."+y)
            else:
                third_ans.set('zhok')
            if len(ans4)==10:
                y=''.join(map(str, ans4))
                fourth_ans.set("..."+y)
            else:
                fourth_ans.set('zhok')
        else:
            first_ans.set("zhok")
            second_ans.set('zhok')
            third_ans.set('zhok')
            fourth_ans.set('zhok')
#creating user interface with entries,labels, and buttons and outputting our values to the users
e_a= Entry(root,textvariable=a_var,font=("Times New Roman",24)).grid(row=1,column=1,ipadx=25,ipady=25)
label_a=Label(root,text='A',font=("Times New Roman",30)).grid(row=1,column=0,ipadx=30,ipady=10)
e_b= Entry(root,textvariable=b_var,font=("Times New Roman",24)).grid(row=2,column=1,ipadx=25,ipady=25)
label_b=Label(root,text='B',font=("Times New Roman",30)).grid(row=2,column=0,ipadx=30,ipady=10)
e_c=Entry(root,textvariable=c_var,font=("Times New Roman",24)).grid(row=3,column=1,ipadx=25,ipady=25)
label_c=Label(root,text='C',font=("Times New Roman",30)).grid(row=3,column=0,ipadx=30,ipady=10)
button1=Button(root,text='OK',command=func)#connecting button with our function
label_first_ans=Label(root,textvariable=first_ans,font=("Times New Roman",24)).grid(row=0,column=3)
label_second_ans=Label(root,textvariable=second_ans,font=("Times New Roman",24)).grid(row=1,column=3)
label_third_ans=Label(root,textvariable=third_ans,font=("Times New Roman",24)).grid(row=2,column=3)
label_fourth_ans=Label(root,textvariable=fourth_ans,font=("Times New Roman",24)).grid(row=3,column=3)
button1.grid(row=4,column=4,ipadx=40,ipady=20)
root.mainloop()
