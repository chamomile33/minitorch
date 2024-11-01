import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N: int) -> List[Tuple[float, float]]:
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N: int) -> Graph:
    """
    Dataset with randomly located points which are divided into
    classes according to the condition: x1 < 0.5 (separated by a vertical line x1 = 0.5)
    Args:
        N: number of points

    Returns:
        Dataset with N points
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N: int) -> Graph:
    """
    Dataset with randomly located points which are divided into
    classes according to the condition: x1 + x2 < 0.5 (separated by a diagonal line)
    Args:
        N: number of points

    Returns:
        Dataset with N points
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N: int) -> Graph:
    """
    Dataset with randomly located points which are divided into
    3 groups vertically and the middle group differs from the rest in color
    Args:
        N: number of points

    Returns:
        Dataset with N points
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N: int) -> Graph:
    """
    Dataset with randomly located points, the field of points is divided into
    4 equal squares and the points on the side and main diagonals of the resulting matrix have different colors
    Args:
        N: number of points

    Returns:
        Dataset with N points
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if ((x_1 < 0.5 and x_2 > 0.5) or (x_1 > 0.5 and x_2 < 0.5)) else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N: int) -> Graph:
    """
    Dataset with randomly located points that are colored depending on hitting the circle in the center of the field
    Args:
        N: number of points

    Returns:
        Dataset with N points
    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = (x_1 - 0.5, x_2 - 0.5)
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N: int) -> Graph:
    """
    Dataset where points of each color are located on their own spiral
    Args:
        N: number of points

    Returns:
        Dataset with N points
    """
    def x(t: float) -> float:
        return t * math.cos(t) / 20.0

    def y(t: float) -> float:
        return t * math.sin(t) / 20.0

    X = [
        (x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    X = X + [
        (y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {
    "Simple": simple,
    "Diag": diag,
    "Split": split,
    "Xor": xor,
    "Circle": circle,
    "Spiral": spiral,
}
