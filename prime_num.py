
'''
This is a program that collects a number and prints all the
prime numbers between one and the inputted number
'''

num = int(input("Enter the number: "))
for n in range(1,num+1):
    if (n%2 != 0) or n== 1:
        if (n%3) != 0 or n == 3 :
            if (n%5) != 0 or n == 5:
                if (n%7) != 0 or n == 7:
                    print(n," is a prime number")
                #else:
                    #print(n," is not a prime number")
