convert = {
    "i":"1",
    "a":"@",
    "m":"M",
    "B":"8",
    "s":"$"
}

your_pass = input("Enter your password: ")
secure_pass = ""

for each in your_pass:
    if each in convert:
        each = convert[each]
    secure_pass += each

print (f"Consider changing that to: {secure_pass}!")


