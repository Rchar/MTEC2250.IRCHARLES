import sys


print("What will be my grade  this semster? \n A. \n B. \n C. \n D. \n F.")

answer = input("Answer: ")

ans = (answer)

print("Are you sure " + str(ans) + "?")


if(ans == "A"):
    print("Great!")
elif(ans == "B"):
    print("Good enough")
elif(ans == "C"):
	print("ummm")    
elif(ans == "D"):
	print("really..?!")
elif(ans == "F"):
	print("Incorrect, try again")	
else:
    print( ans + " is not valid. Choose a letter grade.")


print("Next question? \n Yes \n No ")

answer = input("Answer: ")

ans = (answer)

print("Are you sure " + str(ans) + "?")


if(ans == "Yes"):
    print("There is no more questions!")
else:
	print("Good")

