import sys

def main():
    fuel = input("Fraction: ")

    f = convert(fuel)

    print(gauge(f))

def convert(fuel):
    while True:
        try:
            x,y = fuel.split("/")

            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            return round((x/y),2)*100

        except ZeroDivisionError:
            raise ZeroDivisionError
        except ValueError:
            raise ValueError


def gauge(f):
    if f <= 1:
        return ("E")
    elif f >= 99:
        return ("F")
    else:
        return(f"{f:.0f}%")

if __name__ == "__main__":
    main()