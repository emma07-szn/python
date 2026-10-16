marks=int(input("Enter Students Marks: "))

if(marks>=80 and marks<=100):
    print("Excellent")

elif(marks>=65 and marks<=79):
    print("Above Average")


elif(marks>=50 and marks<=65):
    print("Average")

elif(marks>=35 and marks<=45):
    print("Below Average")

elif(marks>=0 and marks<=34):
    print("Failed")

else:
    print("Invalid Marks")