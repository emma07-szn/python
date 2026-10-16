# Gross salary

salary=int(input("Monthly contribution:"))

if salary >=0 and salary<5999:
    print("150")

elif(salary>=6500 and salary<=7999):
    print("300")

elif(salary>=8000 and salary<=11999):
    print("400")

elif(salary>=12000 and salary<=14999):
    print("500")

elif(salary>=15000 and salary<=19999):
    print("600")

elif(salary>=20000 and salary<=24999):
    print("750")

elif(salary>=25000 and salary<=29000):
    print("850")

elif(salary>=30000 and salary<=49000):
    print("1000")

elif(salary>=50000 and salary<=99000):
    print("1500")

elif(salary>10000):
    print("2000")

else:
    print("Invalide salary")