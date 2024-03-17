from classes import Point
from typing import List

def titikTengah(p1: Point, p2: Point) -> Point:
    # Mengembalikan titik tengah dari dua titik
    newX = (p1.x + p2.x) / 2
    newY = (p1.y + p2.y) / 2
    return Point(newX, newY)

def kurvaBezierDNC(p0: Point, p1: Point, p2: Point, iterasi: int, iterasiMax: int, listPoint: List[Point]):
    if iterasi < iterasiMax:
        iterasi += 1

        q0 = titikTengah(p0, p1)
        q1 = titikTengah(p1, p2)
        r0 = titikTengah(q0, q1)
        
        # Branch Kiri
        kurvaBezierDNC(p0, q0, r0, iterasi, iterasiMax, listPoint)
        # Append titik tengah
        listPoint.append(r0)
        # Branch Kanan
        kurvaBezierDNC(r0, q1, p2, iterasi, iterasiMax, listPoint)
    else:
        listPoint.append(p2)
