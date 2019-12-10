inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for i in inventory:
    item, num, price = i.split(", ")
    print("The store has {} {}, each for {} USD.".format(num, item, price))
