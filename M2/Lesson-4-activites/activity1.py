nom = input("enter ur name pls ")
c = input("enter a character to search for in a word ")
i = 0 
count = 0 
while i < len(nom):
    if nom[i] == c:
        count += 1
    i += 1

print("the character", c, "appears", count, "times in the word", nom)