arr = [14, 16, 87, 36, 25, 89, 34]
M, N = 1, 3
arr_sorted = sorted(arr)

Mth_max = sorted(arr, reverse=True)[M-1]
Nth_min = arr_sorted[N-1]

print(f"{M}st Maximum Number =", Mth_max)
print(f"{N}rd Minimum Number =", Nth_min)
print("Sum =", Mth_max + Nth_min)
print("Difference =", Mth_max - Nth_min)
