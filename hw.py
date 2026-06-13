file = open("shopping list.txt","w")
file.write("1.Bread \n")
file.write("2.Milk \n")
file.write("3.Maggi\n")
file.close()
print("Bucket list saved to a1.txt!")

file = open("shopping list.txt","r")
content = file.read()
print("\n=== shopping list.txt", "r")
print(content)
file.close()

file = open("shopping list.txt","r")
lines = file.readlines()
for i in range(1,{len-1}):
 print[lines(i)]
file.close()

file = open("shopping list.txt","a")
file.write("4.Chips \n")
file.write("5.pasta \n")
file.close()
print("\n 2 more items added!")

file = open("shopping list.txt","r")
print("\n=== updated shopping list.txt ===")
print(file.read())
file.close()