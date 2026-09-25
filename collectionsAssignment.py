#name input
name = input("Enter your name: \n")

#grade inputs and finding the average
grade1 = float(input("Enter a grade: \n"))
grade2 = float(input("Enter a grade: \n"))
grade3 = float(input("Enter a grade: \n"))
grade4 = float(input("Enter a grade \n"))
grade5 = float(input("Enter a grade \n"))
avg = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
#print (avg)

#finding letter grade
if avg >= 90:
    letter = "A"
elif avg >= 80:
    letter = "B"
elif avg >= 70:
    letter = "C"
elif avg >= 60:
    letter = "D"
else:
    letter = "F"

#print the output
print(name)
print ("Average: ", "%.1f" % (avg))
print ("Letter Grade:", letter)

