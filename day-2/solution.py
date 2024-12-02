def parseInput():
    report = []
    with open("input.txt", "r") as f:
        for line in f:
            report.append(list(map(int, line.split())))
    return report


def getDifferences(sequence):
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


def isSafe(distances):
    all_positive = all([d > 0 for d in distances])
    all_negative = all([d < 0 for d in distances])
    safe_range = all(1 <= abs(d) <= 3 for d in distances)

    return (all_positive or all_negative) and safe_range


def countSafeReports(report):
    total = 0
    for sequence in report:
        distances = getDifferences(sequence)
        if isSafe(distances):
            total += 1
    return total


def countSafeDampener(report):
    total = 0
    for sequence in report:
        if isSafe(getDifferences(sequence)):
            total += 1
        else:
            for i in range(len(sequence)):
                modified_sequence = sequence[:i] + sequence[i + 1 :]
                if isSafe(getDifferences(modified_sequence)):
                    total += 1
                    break
    return total


def main():
    report = parseInput()
    print("Total safe reports: ", countSafeReports(report))
    print("Total safe with Problem Dampener: ", countSafeDampener(report))


if __name__ == "__main__":
    main()
