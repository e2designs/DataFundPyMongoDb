my_list = ["apple", "banana", "pear", "apple"]
count = 0
target = "apple"
for entry in my_list:
    if entry == target:
        count += 1
print(f"There are {count} {target} in the list")

# OUTPUT: There are 2 apple in the list
