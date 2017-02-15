stringlist = "1,2,3,4,5".split(",")
newstring = []

for item in stringlist:
    print int(item)
    newstring.append(int(item))
    
print newstring

print map(int, stringlist )

print "One fish two fish red fish blue fish".split("fish")

grocery_string = "item:apples,quantity:4,price:1.50\n"

grocery_strings2 = grocery_string.split(",")
quantity = grocery_strings2[1].split(":")
price = grocery_strings2[2].split(":")
print int(quantity[1]) * float(price[1])

grocery_list = ["item:apples,quantity:4,price:1.50\n",
                "item:pears,quantity:5,price:2.00\n",
                "item:cereal,quantity:1,price:4.49\n"]

amount = []


for item in grocery_list:
    split_data = item.split(",")

    quantity = int(split_data[1].split(":")[1])
    price = float(split_data[2].strip().split(":")[1])
    print quantity * price
    amount.append(quantity*price)

print amount

total=0

for item in amount:
    total += item

print total
