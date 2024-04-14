a=50
b=5
print (a+b)
print("The value of ",a,"+",b,"is",a+b)
print("The value of ",a,"-" ,b,"is",a-b)
print("The value of ",a,"*" ,b,"is",a*b)
print("The value of ",a,"/" ,b,"is",a/b)

print("******************CALCULATOR*********************")
print("\n")

num1=float(input("Enter the frist num1 :"))
num2=float(input("Enter the frist num2 :"))


print("Enter 1 for 'Addition'\nEnter 2 for 'subtraction'\nEnter 3 for 'Multiplication'\nEnter 4 for 'Division'")
Enter_number =int(input("Choice a number 1 to 4 :"))
if Enter_number==1:
    print("Addition the frist and sceond number :",num1+num2)
elif Enter_number==2:
    print("Subrsction the frist and sceond number :",num1-num2)
elif Enter_number==3:
    print("Multiplication the frist and sceond number :",num1*num2)
elif Enter_number==4:
    print("Divison the frist and sceond number :",num1/num2)
else:
    ("invalid input ")

