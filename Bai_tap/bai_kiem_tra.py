#Câu 1:Nhập tọa độ 4 đỉnh của hình thoi, tính chu vi hình thoi. (tọa độ Oxy)
import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def perimeter_of_rhombus():
    print("Nhập tọa độ 4 đỉnh của hình thoi (A, B, C, D):")
    x1, y1 = map(float, input("Tọa độ A (x1, y1): ").split())
    x2, y2 = map(float, input("Tọa độ B (x2, y2): ").split())
    x3, y3 = map(float, input("Tọa độ C (x3, y3): ").split())
    x4, y4 = map(float, input("Tọa độ D (x4, y4): ").split())
    side = distance(x1, y1, x2, y2)
    perimeter = 4* side
    print(f"Chu vi hình thoi là: {perimeter:.2f}")
perimeter_of_rhombus()

#Câu 2:Nhập vào số nguyên dương n, tính tổng các số lẻ nhỏ hơn n
def sum_of_odds():
    n = int(input("Nhập số nguyên dương n: "))
    total = sum(i for i in range(1, n) if i% 2 != 0)
    print(f"Tổng các số lẻ nhỏ hơn {n} là; {total}")
sum_of_odds()


#Câu 3:Nhập vào một số nguyên dương n tính S=
import math
def calculate_s():
    n = int(input("Nhập số nguyên dương n: "))
    s = 0
    for k in range(1, n + 1):
        factorial_k1 = math.factorial(k + 1)
        S += k**(1/3) / factorial_k1
    print(f"Giấ trị của s là: {S:.5f}")
calculate_s()

#Câu 4:Viết chương trình khi nhập vào "in ra màn hình" xuất ra tên mình trên màn hình
def print_name():
    name = input("Nhập họ và tên của bạn: ")
    print(f"Tên của bạn là :{name}")
print_name()
