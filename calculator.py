def add(p,q):
    #this function is used for adding two numbers
    return p+q
def subtract(p,q):
    #this function is used for subtracting two numbers
    return(p-q)
def multiply(p,q):
    #this function is used for mutiplying two numbers
    return p*q
def devide(p,q):
    #this function is used for dividing two numbers
    return p/q

#now we will take inputs from user
print("please select the operation.")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")

choice=input("please enter choice(a/b/c/d):")
num_1 =int(input("please enter the first number:"))
num_2 =int(input("please enter the second number:"))

if choice =='a':
    print (num_1,"+", num_2,"=",add(num_1,num_2))
    
elif choice=='b':
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))

elif choice=='c':
    print(num_1,"*",num_2, "=",multiply(num_1,num_2))

elif choice== 'd':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))

else:
    print("this is an invalid input")
          
          

