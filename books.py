myBooks = []

while True:
    print("Enter the name book " + str(len(myBooks) + 1) + "(Or enter nothing to stop): ")
    name = input()


    if  name  == "":
        break
    myBooks = myBooks + [name]
 

print("The names of your books are: ")
for name in myBooks:
    print(name)