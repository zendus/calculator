#This code is used to create a basic calculator
#I was playing eleko while writing this simple code

num_1 = float(input('Ogbeni enter the 1st number: '))
ope = input('Biko tinye operator: ')
num_2 = float(input('Oga boss enter the 2nd number: '))
if ope == '+':
    print(num_1 + num_2)
elif ope == '-':
    print(num_1-num_2)
elif ope == '*':
    print(num_1*num_2)
elif ope == '/':
    print(num_1/num_2)
#Maka ndi owo ga acho itinye modulus.....ah gat you efi hausa
elif ope == '%':
    print(num_1%num_2)
else:
    print("Onye mpi anya, asim gi tinye operator")