A = [1, 2, 4, 5, 6, 29, 30]
closest_to_sev = min(A, key=lambda x: abs(x - 7))

pointer = A.index(closest_to_sev)
print(pointer)
count_lower_half = pointer - 0 + 1
count_upper_half = len(A) - pointer - 1

#will go for seven day package if count of upper half is gretter than 3

cost_lower_half = 699 if count_lower_half > 3 else count_lower_half * 199
cost_upper_half = 2499 if count_upper_half > 9 else count_upper_half * 199

print(cost_lower_half + cost_upper_half)
