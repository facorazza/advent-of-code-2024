left_list, right_list = [], []
with open("input.txt", "r") as file:
    for line in file:
        n1, n2 = map(int, line.split())
        left_list.append(n1)
        right_list.append(n2)

total_distance = sum(right_list.count(el) * el for el in left_list)
print("Total distance:", total_distance)
