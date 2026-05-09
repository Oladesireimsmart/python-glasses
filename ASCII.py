print("ASCII Value Checker")

char = input("Enter a character: ")

if len(char) == 1:
    ascii_value = ord(char)
    print("Charactrer: ", char) 
    print("ASCII Value: ", ascii_value)
else:
    print("Please enter a single character.")