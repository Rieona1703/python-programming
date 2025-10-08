

array = [1, 2, 3, 4, 1]
print("Original array:", array)

unique_array = []
for num in array:
    if num not in unique_array:
        unique_array.append(num)

print("duplicate array =", unique_array)
