# If n is odd print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive ranfe of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

N = int(input())

if N%2!=0:
    print ("Weird")
else:
    if N>=2 and N<=5:
        print ("Not Weird")
    elif N>=6 and N<=20:
        print ("Weird")
    elif N>20:
        print ("Not Weird")
