st = (input("Enter a String: "))
vowels = "aeiouAeiou"
new = ""
for char in st:
    if char in vowels:
        new += "*"
    else:
        new += char

print(new)
