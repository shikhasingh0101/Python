def add(n1,n2):
       return n1+n2
def subtract(n1,n2):
       return n1-n2
def multiply(n1,n2):
       return n1*n2
def divide(n1,n2):
       return n1/n2
        
n1 = input("enter a number:")
n2 = input("enter a number:")
print("choose operation:")
print("1.add")
print("2.sub")
print("3.multiplication")
print("4.division")
choice = input((1/2/3/4))
if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))

elif choice == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))

elif choice == '4':
            print(n1, "/", n2, "=", divide(n1, n2))
        