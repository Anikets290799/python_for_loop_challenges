n = (input("Enter a String: "))
sum = ""
for i in range(len(n)-1,-1,-1):
    sum += n[i]
if (sum == n):
    print("palindrome") 
else:
    print("not Palindrome")