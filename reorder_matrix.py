import numpy as np
from typing import List

def countOnes(row):
    return row.count(1)

def reorderMatrixInAscOrder(matrixToOrder: List[List[int]]) -> List[List[int]]:
    return sorted(matrixToOrder, key=countOnes)

