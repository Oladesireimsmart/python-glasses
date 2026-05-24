string=input("Enter your own word: ")

char=input("Enter the character you want to check: ")
i=0
count=0

while (i<len(string)):

   if(string[i]==char):
        count=count+1
i=i+1

print("The total number of times", char, "has occured =", count)