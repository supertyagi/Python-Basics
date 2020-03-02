# program to find profit or loss

cost_price = int(input("Enter cost price : "))

selling_price = int(input("Enter selling price : "))

if cost_price > selling_price :
    loss = cost_price-selling_price
    print("Total loss of ",loss)

elif cost_price < selling_price :
    profit = selling_price-cost_price
    print("Total profit of ",profit)

else :
    print("NO loss or profit")