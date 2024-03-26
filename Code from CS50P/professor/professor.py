import random

def main():

    level_input = get_level()
    out_of_ten = 0
    i = 0
    while i < 10:
        o = 0
        X_Y = generate_integer(level_input)
        X = str(X_Y[0])
        Y = str(X_Y[1])
        Z = X_Y[0] + X_Y[1]
        i = i + 1
        while o < 3:
            user_answer = int(input(X + ' + ' + Y + ' = '))
            if user_answer == Z:
                break
            elif user_answer != Z:
                o = o + 1
                print('EEE')
                if o == 3:
                    break
        if o == 3:
            print(Z)
            continue

        elif o < 3:
            out_of_ten = 1 + out_of_ten
        continue
    str_out_of_ten = str(out_of_ten)
    print('Score ' + str_out_of_ten)

def get_level():
    while True:
        str_level_input = input('Level: ')
        try:
            level_input = int(str_level_input)
        except ValueError:
            continue
        else:
            if level_input == 1:
                return(1)
            elif level_input == 2:
                return(2)
            elif level_input == 3:
                return(3)
            elif level_input <= 0 or level_input > 3:
                continue
            elif str_level_input.isalpha():
                continue




def generate_integer(level):
    if level == 1:
        X  = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level == 2:
        X  = random.randint(10, 99)
        Y = random.randint(10, 99)
    elif level == 3:
        X  = random.randint(100, 999)
        Y = random.randint(100, 999)
    X_Y = list()
    X_Y.append(X)
    X_Y.append(Y)
    return X_Y

if __name__ == "__main__":
    main()