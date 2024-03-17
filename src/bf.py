from classes import Point
from typing import List

def rumus(p0: Point, p1: Point, p2: Point, t: float) -> Point:
    newX = ((1 - t) ** 2) * p0.x + 2 * (1 - t) * t * p1.x + (t ** 2) * p2.x
    newY = ((1 - t) ** 2) * p0.y + 2 * (1 - t) * t * p1.y + (t ** 2) * p2.y
    return Point(newX, newY)

def generateN(i: int) -> int:
    if i == 0:
        return 0
    if i == 1:
        return 1
    else:
        return 2 ** (i - 1) + generateN(i - 1)

def generateT(iterasi: int) -> List[float]:
    if iterasi < 0:
        return []

    listofFloat = []
    selisih = 1 / ((generateN(iterasi)) + 1)

    i = selisih
    while i < 1:
        listofFloat.append(i)
        i += selisih
    return listofFloat

def kurvaBezierBF(p0: Point, p1: Point, p2: Point, iterasi: int, listPoint: List[Point]):
    listT = generateT(iterasi)
    temp = [rumus(p0, p1, p2, t) for t in listT]
    listPoint.extend(temp)
    listPoint.append(p2)