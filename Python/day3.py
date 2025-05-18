# 3. Trim whitespace from strings using built in function

# strip(): This method removes both leading and trailing whitespace from a string.
# lstrip(): This method removes only leading whitespace from a string.
# rstrip(): This method removes only trailing whitespace from a string.

string1: str = "     Hello     "
print(string1.strip())

# Additional
# lstrip() 
print(string1.lstrip())
# rstrip()
print(string1.rstrip())