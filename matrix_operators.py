from typing import List
from enum import Enum

from yyc_implementation import yycAlgorithm

class OperatorEnum(Enum):
    THETHA = 1
    GAMMA = 2
    PHI = 3

def thetaOperator(matrixA: List[List[int]], matrixB: List[List[int]] = None, nTimes: int = 1) -> List[List[int]]:
    result:List[List[int]] = []    

    # Si no se recibe un valor para la matriz B, esto quiere decir que el operador va a actuar sobre
    # la misma matriz A.
    if (matrixB is None):

        if (nTimes == 1 ):
            return matrixA

        # Se debe restar una unidad ya que, si el usuario solicita 2 veces, el for se ejecutaria desde
        # 0 a 2 (0, 1, 2). Por tal razon, se hace la resta.
        nTimes = nTimes - 1
        matrixB = matrixA
        
        
    for times in range(0, nTimes):

        if (times != 0):
            matrixA = result
            result:List[List[int]] = []  

        for rowA in matrixA:

            for rowB in matrixB:
                result.append([*rowA, *rowB])


    return result

def gammaOperator(matrixA: List[List[int]], matrixB: List[List[int]] = None, nTimes: int = 1) -> List[List[int]]:
    result:List[List[int]] = []    

    # Si no se recibe un valor para la matriz B, esto quiere decir que el operador va a actuar sobre
    # la misma matriz A.
    if (matrixB is None):

        if (nTimes == 1 ):
            return matrixA

        # Se debe restar una unidad ya que, si el usuario solicita 2 veces, el for se ejecutaria desde
        # 0 a 2 (0, 1, 2). Por tal razon, se hace la resta.
        nTimes = nTimes - 1
        matrixB = matrixA

    numColumnsB = len(matrixB[0])
    emptyZerosForA = [0]*numColumnsB

    for times in range(0, nTimes):

        if (times != 0):
            matrixA = result
            result:List[List[int]] = []  

        numColumnsA = len(matrixA[0])
        emptyZerosForB = [0]*numColumnsA

        for rowA in matrixA:
            result.append([*rowA, *emptyZerosForA])

        for rowB in matrixB:
            result.append([*emptyZerosForB, *rowB])


    return result


def phiOperator(matrixA: List[List[int]], matrixB: List[List[int]] = None, nTimes: int = 1) -> List[List[int]]:
    result:List[List[int]] = []    

    # Si no se recibe un valor para la matriz B, esto quiere decir que el operador va a actuar sobre
    # la misma matriz A.
    if (matrixB is None):

        if (nTimes == 1 ):
            return matrixA

        # Se debe restar una unidad ya que, si el usuario solicita 2 veces, el for se ejecutaria desde
        # 0 a 2 (0, 1, 2). Por tal razon, se hace la resta.
        nTimes = nTimes - 1
        matrixB = matrixA

    
    # El operador phi trabaja exclusivamente con matrices que tienen el mismo numero de filas
    assert(len(matrixA) == len(matrixB)), "El número de filas de la matriz A y de la matriz B deben ser iguales."
        
    for times in range(0, nTimes):

        if (times != 0):
            matrixA = result
            result:List[List[int]] = []  

        for index in range(len(matrixA)):
            result.append([*matrixA[index], *matrixB[index]])

    return result


def calculateRowsAndColumns(matrix: List[List[int]]):
    print(f"Número de filas: {len(matrix)}")
    print(f"Número de Columnas: {len(matrix[0])}")



