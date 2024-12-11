import itertools

safe_reports = 0
with open("input.txt", "r") as file:
    for line in file:
        el = list(map(int, line.split()))
        delta = [p[1] - p[0] for p in itertools.pairwise(el)]

        print(f"{el} {delta}")

        if (
                all(map(lambda x: x >= -3 and x < 0, delta)) or \
                all(map(lambda x: x > 0 and x <= 3, delta))
            ) and ( \
                all(map(lambda x: x < 0, delta)) or \
                all(map(lambda x: x > 0, delta))
            ):
            safe_reports += 1

print("Number of safe reports:", safe_reports)
