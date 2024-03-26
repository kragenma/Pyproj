while True:
    try:
        x,y=input("Fraction: ").split("/")

        x=int(x)
        y=int(y)

        fuel=round((x/y),2)*100

        if y == 0:
            continue
        elif x > y:
            continue
        elif fuel <= 1:
            print ("E")
        elif fuel >= 99:
            print ("F")
        elif 1 < fuel < 101:
            print(f"{fuel:.0f}%")
        break

    except (ValueError, ZeroDivisionError):
        pass
