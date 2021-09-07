#  Write a Python function to find the Max of three numbers.

'''
def max( x, y ):
    if x > y:
        return x
    return y
def maxx( x, y, z ):
    return max( x, max( y, z ) )
print("max number is ",maxx(5, 65, 24))
'''
'''
n1=int(input("Enter first number: "));
n2=int(input("Enter second number: "));
n3=int(input("Enter Third number: "));
def f():
    if(n1>=n2) and (n1>=n3):
        l=n1
    elif(n2>=n1) and (n2>=n3):
        l=n2
    else:
        l=n3
    print("Largest number among  the three is",l)
f()
'''

def f():
    if (n1>n2) and (n2>n3):
        m=n1
    elif (n2>n1) and (n1>n3):
        m=n2
    elif (n3>n1) and (n1>n2):
        m=n3
    # else:
    #     print('Choice is not valid.')

    print('Largest Number among the three is ', m)

n1 = float(input('Enter First Number: '))
n2 = float(input('Enter Second Number: '))
n3 = float(input('Enter Third Number: '))

f()