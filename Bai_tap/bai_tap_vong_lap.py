
# bài 1
for i in range(100):
    if i % 2 == 1:
        print(i)
        
# bài 2 
# Tính S1
n = int(input("Nhập số n: "))
S1 = 0
for i in range(n):  
    S1 += (i + 1)  
print("Tổng S1 =", S1)  
# TÍnh S2
n = int(input("Nhập giá trị của n: "))
S2 = 1
for i in range(n):  
    if i > 0:  
        S2 *= i  
print("Tích S2 =", S2)
# Tính S3
n = int(input("Nhập giá trị của n: "))
S3 = 0
for i in range(n):  
    S3 += ((-1) ** i) / (i + 1)  
print("Giá trị S3 =", S3)
# Tính S4
n = int(input("Nhập giá trị của n: "))
S = 0
for k in range(n + 1):  
    S += k / (k + 2)  
print("Tổng S =", S)

# bài 3
a = 0
b = 1
for i in range(50):
    print(a)
    sum_a_b = a + b
    a = b
    b = sum_a_b 

# bài 4
n = int(input("Nhập vào số nguyên dương cần kiểm tra: "))
if n <= 1:
    print("Số này không phải là số nguyên tố")
else: 
    k = n 
    for i in range(n):
        if n % k == 0 and k != n and k != 1:
            print("Số này không phải là số nguyên tố")
            break
        k = k - 1
    else: 
        print("số này là số nguyên tố")

# bài 5
a = int(input("Nhập vào một số: "))
if a <= 1:
    print(f"{a} không phải là số hoàn hảo.")
else:
    tong = 0
    for i in range(1, a):
        if a % i == 0:
            tong += i

    if tong == a:
        print(f"{a} là số hoàn hảo.")
    else:
        print(f"{a} không phải là số hoàn hảo.")

# bài 6
a = int(input("Nhập vào một số nguyên dương: "))
so_chinh_phuong = False
for i in range(a + 1):
    if i * i == a:
        so_chinh_phuong = True
        break
if so_chinh_phuong:
    print(f"{a} là số chính phương.")
else:
    print(f"{a} không phải là số chính phương.")

# bài 7
n = int(input("Nhập vào một số nguyên dương n: "))
print(f"Các số nguyên tố nhỏ hơn {n} là:")
for i in range(2, n):  
    for a in range(2, i):  
        if i % a == 0:  
            break  
    else:
        print(i)

# bài 8
n = int(input("Nhập vào một số nguyên dương n: "))
if n <= 6:
    print("Không có số hoàn hảo nào nhỏ hơn", n)
else:
    print(f"Các số hoàn hảo nhỏ hơn {n} là:")
    for a in range(1, n): 
        tong = 0  
        for i in range(1, a): 
            if a % i == 0:  
                tong += i  
        if tong == a:
            print(a)  

# bài 9
n = int(input("Nhập vào một số nguyên dương n: "))
print(f"Các số chính phương nhỏ hơn {n} là:")
for i in range(1, n):  
    if i * i < n:  
        print(i * i) 

# bài 10
a = int(input("Nhập vào số thứ nhất: "))
b = int(input("Nhập vào số thứ hai: "))
UCLN = 1  
if a < b:
    UCLN_moi = a
else:
    UCLN_moi = b
for i in range(1, UCLN_moi + 1):
    if a % i == 0 and b % i == 0:  
        UCLN = i  
print(f"Ước chung lớn nhất của {a} và {b} là: {UCLN}")

# bài 11
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if a > b:
    so_lon_nhat = a
else:
    so_lon_nhat = b
for i in range(so_lon_nhat, a * b + 1, so_lon_nhat):
    if i % a == 0 and i % b == 0:
        bcnn = i
        break
print(f"Bội chung nhỏ nhất của {a} và {b} là: {bcnn}")

# bài 12
tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
if tu_so > mau_so:
    so_nho_nhat = mau_so
else:
    so_nho_nhat = tu_so
for i in range(so_nho_nhat, 0, -1):  
    if tu_so % i == 0 and mau_so % i == 0:  
        ucln = i  
        break
tu_so_toi_gian = tu_so // ucln
mau_so_toi_gian = mau_so // ucln
print(f"Phân số tối giản là: {tu_so_toi_gian}/{mau_so_toi_gian}")

# bài 13
n = int(input("Nhập số nguyên: "))
print("1", end = "*")
for i in range (2, n+1):
    while n % i == 0:
        print(i, end="*")
        n = n // i

# bài 14
n = int(input("Nhập số dòng cho Tam giác Pascal: "))
for i in range(n):  
    print(" " * (n - i - 1), end="")
    a = 1
    for j in range(i + 1):  
        print(a, end=" ")
        a = a * (i - j) // (j + 1)
    print()

# bài 15
