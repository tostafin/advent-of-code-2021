bin_numbers = []
zero_cnt = 0
with open("input6") as file:
    for line in file:
        num = line.rstrip()
        bin_numbers.append(num)
        if num[0] == "0":
            zero_cnt += 1

oxygen, co2 = [], []


def filter_initial(oxygen, co2, bit):
    oxygen_zero_cnt = co2_zero_cnt = 0
    for num in bin_numbers:
        if num[0] == bit:
            oxygen.append(num)
            if len(num) > 0 and num[1] == "0":
                oxygen_zero_cnt += 1

        else:
            co2.append(num)
            if len(num) > 0 and num[1] == "0":
                co2_zero_cnt += 1
    
    return oxygen_zero_cnt, co2_zero_cnt


if len(bin_numbers) // 2 >= zero_cnt:
    oxygen_zero_cnt, co2_zero_cnt = filter_initial(oxygen, co2, "1")
    
else:
    oxygen_zero_cnt, co2_zero_cnt = filter_initial(oxygen, co2, "0")


def filter_container(container, zero_cnt, bit):
    idx = 1
    while len(container) > 1:
        new_container = []
        if zero_cnt > len(container) // 2:
            zero_cnt = 0
            for num in container:
                if int(num[idx]) == bit:
                    new_container.append(num)
                    if len(num) > idx + 1 and num[idx + 1] == "0":
                        zero_cnt += 1
        else:
            zero_cnt = 0
            for num in container:
                if int(num[idx]) == bit ^ 1:
                    new_container.append(num)
                    if len(num) > idx + 1 and num[idx + 1] == "0":
                        zero_cnt += 1
        
        idx += 1
        container = new_container
    
    return container


oxygen = filter_container(oxygen, oxygen_zero_cnt, 0)
co2 = filter_container(co2, co2_zero_cnt, 1)

print(int(oxygen[0], 2) * int(co2[0], 2))
