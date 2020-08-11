def add(num_1, num_2):
    return num_1 + num_2


print("This is an addition calculator.")
num_1 = int(input("Pick any number: "))
num_2 = int(input("Pick another number: "))
print(num_1, "+", num_2, "=", 
					add(num_1, num_2))