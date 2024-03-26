current_price=50

while current_price>0:
    coke=int(input("Insert Coin: "))
    if coke not in[5,10,25]:
        pass
    else:
        current_price=current_price-coke
    if current_price>0:
        print(f"Amount Due: {current_price}")
    elif current_price<=0:
        print(f"Change Owed: {current_price*-1}")