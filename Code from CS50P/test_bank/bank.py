def main():
    greeting = str(input("Greeting: ").lower().strip())
    x = value(greeting)
    print(f"${x}")

def value(greeting):
    if greeting.startswith("hello"):
        return(0)
    for i in greeting:
        if i[0] == "h":
            return(20)
        else:
            return(100)

if __name__ == "__main__":
    main()