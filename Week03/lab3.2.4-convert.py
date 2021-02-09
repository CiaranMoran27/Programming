#This program takes a user input as a float as this datatype will accept decimal places (9.44 dollars mentioned in question)
#Next converts the float to an abso1ute value (to remove and negative signs) 
#Next converts the absolute value to cent and rounds result to the nearest integer (zero decimal places)
#Author: Ciaran Moran

moneyAmount = float(input("Enter the amount of money in dollars: "))
absoluteValue = abs(moneyAmount)
dollarToCent =  round(absoluteValue* 100,0) 

print(dollarToCent)