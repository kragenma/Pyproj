months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:

    date=input("Date: ")

    try:
        m,d,y=date.split("/")
        m=int(m)
        d=int(d)
        y=int(y)

        if(0 < int(m) < 13) and (0 < int(d) < 32):
            print(y, f'{m:02}', f'{d:02}', sep="-")
            break
    except:
        try:
            m,d,y=date.split(" ")
            if "," not in d:
                (prompt)
            d=d.replace(","," ")
            d=int(d)
            y=int(y)

            if m in months and (0 < int(d) < 32):
                m=(months.index(m)+1)
                print(y, f'{m:02}', f'{d:02}', sep="-")
                break
        except:
            pass