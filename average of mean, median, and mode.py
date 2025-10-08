import statistics as st

# Input
data = [12, 45, 83, 52]

# Calculate mean, median, and mode
mean_val = st.mean(data)
median_val = st.median(data)
mode_val = st.mode(data)

# Average of mean, median, and mode
average = (mean_val + median_val + mode_val) / 3

print("Output:", int(average))  # int to match sample output
