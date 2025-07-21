n = int(input("Enter a Number: "))
sum = 0
num = 0 
even = 0
odd = 0
for i in range(1,n+1):
    if (i % 2 == 0):
        sum += 1
        even += i
    else:
        num += 1
        odd += i
print("The Toatl number of even number are",sum,"The Sum fo all the even number is",even)
print("The Toatl number of even number are",num,"The Sum fo all the even number is",odd)
