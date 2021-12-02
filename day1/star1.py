depths = []
with open("input1") as file:
    for line in file:
        depths.append(int(line.rstrip()))

increases = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        increases += 1

print(increases)

