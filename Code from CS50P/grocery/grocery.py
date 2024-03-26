count = 0

grocery = {}

while True:
    try:
        item = input().strip().lower()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        print("\n")
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        break