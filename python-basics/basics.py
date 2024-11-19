### Variables
# assgning a variable (assignment statement)
plant = "poppy"

# Expression - combination of variables, values and operators
plant_name = "pop" + "py"
print(plant_name)

# Data types - check data type
print(type(plant))


### Functions
# 1
def greeter (name):
    print(f"Good morning, {name}!")

greeter("Joules")

# 2
def bouquet_maker(size, flowers):
    """Summarize the bouqet we are about to make"""
    print(f"Making a {size} boquet with {flowers}.")

bouquet_maker("large", "lillies")

plants = ["sunflowers", "cornflowers", "poppies"]

# 3
plants = ["sunflowers", "cornflowers", "poppies"]

def order_maker(plant):
  for plant in plants:
   print(f"Adding {plant} to your order!")

order_maker(plants)


### For loops 
plants = ["sunflower", "cornflower", "poppies"]

for plant in plants:
    print(plant)

# Passing a list to a function with a for loop
flowers = ["poppies", "sunflowers", "daisies", "cornflowers"]

def plant_praiser(flower):
   for flower in flowers:
    print(f"What lovely {flower}!")

plant_praiser(flowers)



### Conditional
# if/else statement
plant = "rose"

if plant == "rose":
    print("So romantic!")
elif plant == "sunflower":
    print("You brighten up my day!")
else:
    print("oh!")



