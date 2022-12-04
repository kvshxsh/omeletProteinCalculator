eggs = float(input("Input the number of eggs the omelet contains: "))
bread = float(input("Input the number of bread loaves the omelet contains: "))

protein_eggs = 6 #grams
protein_bread = 2 #grams
protein_omelet = (eggs*protein_eggs) + (bread*protein_bread)

print("The omelet has %0.1f grams of protein"%(protein_omelet)) #grams