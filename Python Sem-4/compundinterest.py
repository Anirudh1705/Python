p = float(input("Enter the Principal amount: "))
r = float(input("Enter the rate of Interest: "))
t = int(input("Enter the time in years: "))
n = int(input("Enter the no.of times compounding occurs in a year: "))
a = p*((1 + (r/ 100) / n) ** (n*t))
print(a)