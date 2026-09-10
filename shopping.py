shop ={
    "bread": 1000,
    "milk": 1500,
    "rice": 5000,
    "egg": 300
}
cart = ["bread", "egg","rice", "egg"]

total = 0

for items in cart:
    print("")
    if items in shop:
        print(f"{items}: {shop[items]}") 
    total += shop[items]
print(f"Total: {total}")
print(len(set(cart)))
if total > 5000:
    print("You qualify for a discount!")
else:
    print("No discount")
    
    
        