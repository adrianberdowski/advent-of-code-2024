import re
from operator import mul


def parseInput(file_path) -> list:
    with open(file_path, "r") as f:
        res = re.findall(r"(do\(\)|don\'t\(\)|mul\(\d+,\d+\))", f.read())
        return [
            (
                instr
                if instr.startswith("do")
                else [int(num) for num in re.findall(r"\d+", instr)]
            )
            for instr in res
        ]


def partOne(data: list) -> int:
    return sum(mul(*instr) for instr in data if isinstance(instr, list))


def partTwo(data: list) -> int:
    total = 0
    canAdd = True

    for instr in data:
        match instr:
            case "do()":
                canAdd = True
            case "don't()":
                canAdd = False
            case [a, b]:
                if canAdd:
                    total += mul(a, b)
    return total


def main():
    data = parseInput("input.txt")
    print(f"Part 1: {partOne(data)}")
    print(f"Part 2: {partTwo(data)}")


if __name__ == "__main__":
    main()
