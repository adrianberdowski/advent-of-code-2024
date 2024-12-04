from typing import Dict, Set, Tuple, List


def get_rotate(dx, dy, k):
    for _ in range(k):
        dx, dy = -dy, dx
    return dx, dy


def get_base_pattern():
    return [((-1, -1), "M"), ((1, -1), "M"), ((-1, 1), "S"), ((1, 1), "S")]


def get_directions():
    return {
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    }
