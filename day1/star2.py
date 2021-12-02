depths = []
with open("input2") as file:
    for line in file:
        depths.append(int(line.rstrip()))

increases = 0
last_sum = depths[0] + depths[1] + depths[2]
for i in range(1, len(depths) - 2):
    curr_sum = depths[i] + depths[i + 1] + depths[i + 2]
    if curr_sum > last_sum:
        increases += 1

    last_sum = curr_sum

print(increases)

