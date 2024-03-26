twttr=input("Input: ")

output=""

for i in twttr:
    if i.lower() in ["a","e","i","o","u"]:
        pass
    else:
        output += i
print(output, end="")