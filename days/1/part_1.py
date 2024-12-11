left_list, right_list = [], []
with open("input.txt", "r") as file:
    for line in file:
        n1, n2 = map(int, line.split())
        left_list.append(n1)
        right_list.append(n2)

left_list.sort()
print("Left list:", left_list)

right_list.sort()
print("Right list:", right_list)

total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
print("Total distance:", total_distance)
