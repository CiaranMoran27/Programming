
# why does the following cause an error?
"""
message = 'I have eaten ' + 99 + ' burritos.'
print (message)
"""



# Answer = # Causes an error as python cant concatenate str and int: 
# Solution is to convert the int (99) to type string as below:

message = 'I have eaten ' + str(99) + ' burritos.'
print (message)