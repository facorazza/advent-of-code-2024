import itertools

def is_safe(report):
    delta = [p[1] - p[0] for p in itertools.pairwise(report)]

    return (
        all(map(lambda x: x >= -3 and x < 0 or x > 0 and x <= 3, delta))
    ) and ( \
        all(map(lambda x: x < 0, delta)) or \
        all(map(lambda x: x > 0, delta))
    )

safe_reports = 0
with open("input.txt", "r") as file:
    for line in file:
        report = list(map(int, line.split()))

        if any(map(is_safe, [report[:i] + report[i + 1:] for i in range(0, len(report))])):
            safe_reports += 1

print("Number of safe reports:", safe_reports)
