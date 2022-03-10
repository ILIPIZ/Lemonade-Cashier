lemonade_cups = int(input("How Many Cups Do You Want?  "))
print(" ")

i = lemonade_cups * 1.50

print("That Will Be $",i)
print(" ")

given = int(input("How Much Money Is Given? $"))
print(" ")

if given < i:
    print("Not Enough Money")

if given >= i:
    e = given - i
    print("Change $", e)
    print(" ")
    print(lemonade_cups, "cups of lemonade for you.")
    print(" ")

print("Have A Nice Day!")