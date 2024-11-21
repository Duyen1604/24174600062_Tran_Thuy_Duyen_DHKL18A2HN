
# Bài 1
import math

#Nhập bán kính và chiều cao
r = float(input("Nhap ban kinh: "))
h = float(input("Nhap chieu cao: "))

# kiểm tra bán kính và chiều cao có hợp lệ không
if r < 0 or h < 0: 
    print("Ban kinh va chieu cao khong hop le, khong the tinh toan")
else:
    dien_tich_xung_quanh = 3.14 * 2 * r * h 
    dien_tich_toan_phan = 2 * 3.14 * r ** 2 + dien_tich_xung_quanh
    # in kết quả
    print(f"dien tich xung quan la: {dien_tich_xung_quanh:.2f}")
    print(f"dien tich toan phan la: {dien_tich_toan_phan:.2f}")


# Bài 2
import math

# nhập giá trị cho x
x = float(input("Nhập giá trị của x: "))

phan_tu = -x + math.sqrt(x**2 + 4) 
phan_mau = (x**4 + 1) ** (1/7)
ket_qua = (phan_tu / phan_mau)

# in ra kết quả
print(f"Giá trị của f(x): {ket_qua:.2f}")


# Bài 4
import math
# nhập thời gian
t = int(input("Nhap thoi gian su dung bong den(s):"))
if t < 0:
    print("thoi gian khong hop le")
else: 
    # tính công suất
    P = 220 * 2.7 * t / 3600 * 1000
    # tính tiền
    tien_phai_tra = P * 7000
    print(f"Tien dien phai tra: {tien_phai_tra}")


# Bài 8
import math

# Nhập giá trị x
x = float(input("Nhap gia tri x: "))

# Kiểm tra giá trị x hợp lệ
if x <= 0 or x == 1:
    print("Gia tri x khong hop le")
else:
    f_x = math.log(x, 4) + math.log(2, x)
    print(f"Gia tri can tim f(x)={f_x:.2f}")
