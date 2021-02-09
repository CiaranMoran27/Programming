# Author: Ciaran Moran

# This program Reads in a string and strips any leading or trailing spaces
# Then Converts all the letters to lower case 
input_string = input("enter a string: ")
normalised_string = input_string.strip().lower()


# This stores the length of the input string and the normalised one in variables
length_of_input_string = len (input_string)
length_of_normalised_string = len(normalised_string)


print("That String normalised is: {}".format(normalised_string))
print("We Reduced the input string from {} to {} characters".format(length_of_input_string,length_of_normalised_string))