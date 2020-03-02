# program to check number of notes needed to match the given amount

amount = int(input("Enter the amount : "))

while amount!=0:
    two_thousand = amount//2000
    amount = amount%2000
    five_hundred = amount//500
    amount = amount%500
    one_hundred = amount//100
    amount = amount%100
    fifty = amount//50
    amount = amount%50

total_notes = two_thousand+five_hundred+one_hundred+fifty

print("total no of two thousand notes ",two_thousand)
print("total no of five hundred notes ",five_hundred)
print("total no of one hundred notes ",one_hundred)
print("total no of fifty notes ",fifty)
print("total no of notes ",total_notes)