#Write a Python program to solve the general version of the above problem.
#Ask the user for the time now (in hours 0-24), and ask for the number of hours to wait.
#Your program should output what the time will be on the clock when the alarm goes off.
tw= int (input ("numbers of hours to wait"))
tn= int (input ("what time is now"))
a = (tw + tn) % 24
if a > 12:
    a= a -12
    print (str(a) + "PM")
else:
    print (str(a) + "AM")
    
