from matplotlib import pyplot as plt
from typing import Tuple, List
from dnc import *
from bf import *
import time

def createKurva(p0: Point, p1: Point, p2: Point, iterasiMax: int, isBF: bool) -> Tuple[List[Point], float]:
    waktuAwal = time.time()

    listPoint = [p0]
    if isBF:
        kurvaBezierBF(p0, p1, p2, iterasiMax, listPoint)
    else:
        kurvaBezierDNC(p0, p1, p2, 0, iterasiMax, listPoint)

    waktuAkhir = time.time()
    return listPoint, (waktuAkhir - waktuAwal)

def ambilInput():
    # Mengembalikan 3 control point, jumlah iterasi, dan metode yang dimasukkan oleh user
    
    # Input control point
    pointList = []
    for i in range(3):
        print(f"Point {i + 1}")
        point = Point(float(input("x = ")), float(input("y = ")))
        pointList.append(point)

    # Input jumlah iterasi
    nIterasi = int(input("Jumlah Iterasi: "))
    while (nIterasi < 0):
        print("Jumlah iterasi harus lebih dari 0!")
        nIterasi = int(input("Jumlah Iterasi: "))
    
    # Input metode brute force atau divide and conquer
    metode = str(input("Metode Brute Force [B] / Divide and Conquer [D]: "))
    while metode != 'D' and metode != 'B':
        print("Masukan tidak valid, ", end="")
        metode = str(input("Metode Brute Force [B] / Divide and Conquer [D]: "))
    if metode == 'D':
        isBF = False
    elif metode == 'B':
        isBF = True
    return pointList, nIterasi, isBF

def main():
    # Input
    inputUser, iterasiMax, isBF = ambilInput()

    # Proses 
    listPoint, runtime = createKurva(inputUser[0], inputUser[1], inputUser[2], iterasiMax, isBF)
    x = [p.x for p in listPoint]
    y = [p.y for p in listPoint]

    # Output
    print(f"Runtime: {runtime} s")
    plt.plot(x, y, "ro-")
    plt.show()

main()