import sys

calc = 0 
cmd = input("enter a number")
cmd2 = input("enter an operation")
cmd3 = input("enter another number")
print(cmd + cmd2 + cmd3)
if (cmd2 == "+"):
    calc = int(cmd) + int(cmd3)
    print(calc)

if (cmd2 == "-"):
    calc = int(cmd) - int(cmd3)
    print(calc)
if (cmd2 == "*"):
    calc = int(cmd) * int(cmd3)
    print(calc)    
if (cmd2 == "/"):
    calc = int(cmd) / int(cmd3)
    print(calc)
if (cmd2 == "%"):
    calc = int(cmd) % int(cmd3)
    print(calc)
