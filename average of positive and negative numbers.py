

print("Enter numbers (-1 to stop):")

pos_sum = 0
pos_count = 0
neg_sum = 0
neg_count = 0

while True:
    num = int(input())
    if num == -1:   
        break
    elif num > 0:
        pos_sum += num
        pos_count += 1
    elif num < 0:
        neg_sum += num
        neg_count += 1

# Calculate averages safely
if pos_count > 0:
    pos_avg = pos_sum // pos_count   # integer avg
else:
    pos_avg = 0

if neg_count > 0:
    neg_avg = neg_sum // neg_count   # integer avg
else:
    neg_avg = 0

print(f"avg negative number is {neg_avg}, avg positive number is {pos_avg}")
