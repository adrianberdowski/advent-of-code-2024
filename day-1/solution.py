from collections import Counter


def parseInput(file_path):
    try:
        left, right = [], []
        with open(file_path, encoding="UTF-8") as file:
            for index, line in enumerate(file):
                for i, n in enumerate(line.split()):
                    if (index * len(line.split()) + i) % 2 == 0:
                        left.append(int(n))
                    else:
                        right.append(int(n))
        return left, right

    except Exception as e:
        print("Validate the input file")
        return [], []


def totalDistance(left, right):
    return sum(
        map(lambda pair: abs(pair[0] - pair[1]), zip(sorted(left), sorted(right)))
    )


def totalSimilarity(left, right):
    right_counter = Counter(right)
    return sum(left_value * right_counter.get(left_value, 0) for left_value in left)


def main():
    left, right = parseInput("input.txt")
    print("Distance:", totalDistance(left, right))
    print("Similarity:", totalSimilarity(left, right))


if __name__ == "__main__":
    main()


# Distance: 1189304
# Similarity: 24349736
