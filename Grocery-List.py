items_list=[]
i=0
#here we took input for iteams in lists
for i in range(1,6):
    item=input(f"{i} Iteam is : ")
    items_list.append(item)
print(items_list)
#here we took prices of iteams 
item_prices=[]
for i in range(5):
    price=int(input(f"Enter price of {items_list[i]} : "))
    item_prices.append(price)
print(item_prices)
#items lists with there prices 
print("\niteam list with their prices ")
for i in range (5):
    print(f"{items_list[i]} : {item_prices[i]}")
#fun to calculate total bill 
def bill():
    total=0
    for price in item_prices:
        total=total+item_prices[i]
    print(f"Your Final Bill is : {total}")

bill()

