from typing import Dict, Set, Tuple, List
from utils import get_directions, get_rotate, get_base_pattern


def parse_input(filename: str) -> Dict[str, Set[Tuple[int, int]]]:
    with open(filename, "r") as f:
        data = f.read().splitlines()

        occ = {letter: set() for letter in {"X", "M", "A", "S"}}
        for i, line in enumerate(data):
            for j, char in enumerate(line):
                if char in occ:
                    occ[char].add((i, j))

        return occ


def check_sequence(
    occ: Dict[str, Set[Tuple[int, int]]],
    start: Tuple[int, int],
    direction: Tuple[int, int],
) -> bool:
    x, y = start
    dx, dy = direction

    return all(
        (x + dx * k, y + dy * k) in occ[ch] for k, ch in enumerate("XMAS", start=0)
    )


def find_XMAS(occ: Dict[str, Set[Tuple[int, int]]]) -> int:
    total = 0
    directions = get_directions()

    for start in occ["X"]:
        total += sum(check_sequence(occ, start, direction) for direction in directions)

    return total


def detect_MAS_crossing(occ: Dict[str, Set[Tuple[int, int]]]) -> int:
    total = 0
    base_pattern = get_base_pattern()
    rotate = get_rotate

    cross_patterns = []
    for k in range(4):
        rotated_pattern = [(rotate(dx, dy, k), ch) for (dx, dy), ch in base_pattern]
        cross_patterns.append(rotated_pattern)

    for a in occ["A"]:
        for pattern in cross_patterns:
            if all((a[0] + dx, a[1] + dy) in occ[ch] for (dx, dy), ch in pattern):
                total += 1

    return total


def main():
    occ = parse_input("input.txt")
    print("Part one:", find_XMAS(occ))
    print("Part two:", detect_MAS_crossing(occ))


if __name__ == "__main__":
    main()
