import inflect
import sys

p = inflect.engine()
names = []

while True:
    try:
        name=input("").title()
        if len(name) < 1:
            print("Adieu, adieu, to " + p.join(names))
            sys.exit()

        names.append(name)

    except EOFError:
        print("\n" + "Adieu, adieu, to " + p.join(names))
        break