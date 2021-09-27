q1=""" 
1.  what is the output of the program?

#include<stdio.h>
imt main()
{
printf("hello world");
return 0;
}


a.  hello world
b.  Hello World
c.  helloworld
d.  error
"""
#*****************************************************************************
q2="""
2.  what is the output of the program?

#include <stdio.h>
int main()
{
int a= 10;
int b= 20;
printf("addition of a and b:%d",a+b);
return 0;
}

a.  70
b.  20
c.  30
d.  error
"""
#******************************************************************************
q3= """
3.  waht is the header file for c?

a.  #include<iostream.h>
b.  #include<math.h>
c.  #include<string.h>
d.  #include<stdio.h>
"""
#******************************************************************************

q4 = """
4.  who is the father of C programming?

a.  Dennis Ritche
b.  James Gousling
c.  Sun Microsystem
d.  Elon Musk
"""
#******************************************************************************

q5="""
5.  What is the output of the expression?
3*1**3

a.  3
b.  9
c.  4
d.  19
"""
#******************************************************************************

q6="""
6.  What will be the output of the following python code,

list=[a,b,c,d,e]
print(list[3])

a.  d
b.  a
c.  No Output
d.  c

"""

#******************************************************************************

q7="""
7.  What will be the Output of the python code?

def f1():
    print("hello World!)
f1()

a.  Error
b.  f1()
c.  hello World!
d.  HelloWorld!
"""
#******************************************************************************

q8="""
8.  Which of the following can be overloaded?

a.  Object
b.  Functions
c.  Both A and B
d.  class
"""
#******************************************************************************

q9="""
9.  Which function overloads the == operator?

a.  __eq__()
b.  __equ__()
c.  __isequal__()
d.  __init__(self)
"""
#******************************************************************************

q10 = """
10.  What is setattr() used for?

a.  To access the attribute of the object
b.  To set an attribute
c.  To check if an attribute exists or not
d.  To define a module
"""

#******************************************************************************

questions = {q1:"a",q2:"c",q3:"d",q4:"a",q5:"a",q6:"a",q7:"c",q8:"b",q9:"a",q10:"b"}

name = input("Enter your name to continue the test:")
print("hello",name,"Welcome to the quiz world!")
score = 0
for i in questions:
    print(i)
    ans = input("Enter the answer ( a / b / c / d ):")
    if ans==questions[i]:
        score += 1
        print("________________________________________________________________________________________________")
        print("\n")
print("You got\t"+str(score) + "/" + str(len(questions)) + "\tcorrect")
print("________________________________________________________________________________________________________\n")
if score>7:
    print("you got Good Marks!")
elif score>=5:
    print("you got average Mark!")
else:
    print("you got low Marks!")

print("____________________________________________________________________________________________________________\n")
