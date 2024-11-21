
# Câu 1
# Nhập vào 1 số nguyên. Kiểm tra xem nó là số chẵn hay số lẻ.

# Câu 2
# Nhập vào 2 số nguyên. Kiểm tra xem chúng cùng dấu hay trái dấu.

# Câu 3
# Giải phương trình bậc nhất ax+b=0 (với a, b là kiểu số nguyên).

# Câu 4
# Giải phương trình bậc hai a*x**2 + b*x + c=0 (với a, b, c là kiểu số nguyên). a,b,c là các số âm
a = input("Nhap gia tri a")
b = input("Nhap gia tri b")
c = input("Nhap gia tri c")

a = int(a)
b = int(b)
c = int(c)

if a < 0 and b <0 and c < 0:
    if a != 0:
        delta = b**2 - 4*a*c
        if delta > 0:
            x_1 = (-b + delta**(1/2))/(2*a)
            x_2 = (-b - delta**(1/2))/(2*a)
            print(f"Phuong trinh co 2 nghiem phan biet {x_1}, {x_2}")
        elif delta == 0:
            x_3 = -b/(2*a)
            print(f"Phuong trinh co 1 nghiem kep {x_3}")
        else:
            print(f"Phuong trinh vo nghiem")
    else:
        if b != 0:
            x_0 = (-c)/b
            print(f"Phuong trinh co 1 nghiem duy nhat {x_0}")
        else:
            if c != 0:
                print("Phuong trinh vo nghiem")
            else:
                print("Phuong trinh co vo so nghiem")
print("Chuong trinh ket thuc")

# Câu 5
# Cho tọa độ 3 điểm A(x1, y1, z1), B(x2, y2, z2), C(x3, y3, z3). 
# Với các giá trị x1, x2, x3, y1, y2, y3, z1, z2, z3, tìm khoảng cách giữa các điểm này

print("Nhap toa do A:")
x_1 = input("x1 = ")
y_1 = input("y1 = ")
z_1 = input("z1 = ")

print("Nhap toa do B:")
x_2 = input("x2 = ")
y_2 = input("y2 = ")
z_2 = input("z2 = ")

print("Nhap toa do C:")
x_3 = input("x3 = ")
y_3 = input("y3 = ")
z_3 = input("z3 = ")

x_1 = float(x_1)
x_2 = float(x_2)
x_3 = float(x_3)
y_1 = float(y_1)
y_2 = float(y_2)
y_3 = float(y_3)
z_1 = float(z_1)
z_2 = float(z_2)
z_3 = float(z_3)
#tính độ dài giữa 2 tọa độ A(x1, y1, z1), B(x2, y2, z2)
#Công thức: AB = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**(1/2)
do_dai_AB = ((x_1-x_2)**2 + (y_1-y_2)**2 + (z_1-z_2)**2)**(1/2)
do_dai_BC = ((x_3-x_2)**2 + (y_3-y_2)**2 + (z_3-z_2)**2)**(1/2)
do_dai_AC = ((x_1-x_3)**2 + (y_1-y_3)**2 + (z_1-z_3)**2)**(1/2)
print(f"Do dai AB = {do_dai_AB}")
print(f"Do dai BC = {do_dai_BC}")
print(f"Do dai AC = {do_dai_AC}")


# Câu 6
# Cho tọa độ I(x,y), bán kính R và một điểm M(a,b). 
# Với các giá trị a, b, x, y, R bất kì, tìm vị trí của M so với mặt cầu tâm I bán kính R

print("Nhap toa do I:")
x = input("x = ")
y = input("y = ")

print("Nhap toa do M:")
a = input("a = ")
b = input("b = ")

x = float(x)
y = float(y)
a = float(a)
b = float(b)

ban_kinh_r = input("Nhap vao ban kinh R: ")
ban_kinh_r = float(ban_kinh_r)

do_dai_IM = ((a-x)**2+(b-y)**2)**(1/2)
if do_dai_IM > ban_kinh_r:
    print("Diem M nam ngoai duong tron")
elif do_dai_IM < ban_kinh_r:
    print("Diem M nam trong duong tron")
else:
    print("Diem M nam tren duong tron")

# Câu 7
# Cho tọa độ 2 điểm A(x1, y1), B(x2, y2). 
# Với các giá trị x1,x2,y1,y2 bất kỳ, tìm phương trình tổng quát của đường thẳng đi qua 2 điểm này.

print("Nhap toa do A:")
x_1 = input("x_1 = ")
y_1 = input("y_1 = ")

print("Nhap toa do B:")
x_2 = input("x_2 = ")
y_2 = input("y_2 = ")

x_1 = float(x_1)
x_2 = float(x_2)
y_1 = float(y_1)
y_2 = float(y_2)

#Tìm vecto phap tuyen n(a,b)
a = -(y_2 - y_1)
b = x_2 - x_1
#phương trình tổng quát của đường thẳng ax + by + c = 0
c = -((-(y_2 - y_1))*x_1 + (x_2 - x_1)*y_1)

print(f"Phuong trinh tong quat cua duong thang di qua AB: {a}*x + {b}*y + {c} = 0")


# Câu 8
# Viết chương trình tính điểm của sinh viên.
# Chương trình này sẽ đọc vào các loại điểm của sinh viên (điểm chuyên cần, điểm giữa kỳ, và điểm cuối kỳ) và xếp loại điểm theo quy luật sau:
# – if điểm trung bình >=9 =>loại=A
# – if điểm trung bình >= 7 và < 9 => loại=B
# – if điểm trung bình >= 5 and < 7 =>loại=C
# – if điểm trung bình < 5 => loại=D

diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
diem_giua_ky = float(input("Nhập điểm giữa kỳ: "))
diem_cuoi_ky = float(input("Nhập điểm cuối kỳ: "))
diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3
if diem_trung_binh >= 9:
    loai = "A"
elif diem_trung_binh >= 7:
    loai = "B"
elif diem_trung_binh >= 5:
    loai = "C"
else:
    loai = "D"
print(f"Điểm của sinh viên là: {diem_trung_binh:.2f}")
print(f"Xếp loại: {loai}")
    
