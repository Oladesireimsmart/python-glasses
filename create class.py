class IOstring:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print(self.string.upper())

str1=IOstring()
str1.get_string()
str1.print_string()