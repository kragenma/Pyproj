camel=input("camelCase: ")

output=""

for i in camel:
    if i.isupper():
        output+=f"_{i.lower()}"
    elif i.islower():
        output+=i
print(output)