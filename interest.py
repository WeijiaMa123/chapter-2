t = float (input ("what is the number of years"))
P = 10000
r = 0.08
n = 12
A = P * (1 + r/n) ** (t*n)
print ("$",A)