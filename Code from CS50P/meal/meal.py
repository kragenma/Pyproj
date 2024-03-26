def main():
    time=input("What is the time? ")
    float_time=convert(time)

    if 7<=float_time<=8:
        print("breakfast time")
    elif 12<=float_time<=13:
        print("lunch time")
    elif 18<=float_time<=19:
        print("dinner time")
    else:
        print("")

def convert(time):
    hr, min = time.split(":")
    hr = float(hr)
    min = float(min)/60
    float_time = hr+min
    return float_time

if __name__ =="__main__":
    main()