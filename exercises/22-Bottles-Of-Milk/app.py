def number_of_bottles():
    for i in range(99, 1, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down pass it around, {i-1} bottles of beer on the wall\n")
    i -=1
    print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
    print(f"Take it down, pass it around, No more bottles of beer on the wall.\n")
    print(f"No more bottles of beer on the wall, no more bottles of beer.")
    i = 99
    print(f"Go to the store and buy some more, {i} bottles of beer on the wall.\n")
    

number_of_bottles()