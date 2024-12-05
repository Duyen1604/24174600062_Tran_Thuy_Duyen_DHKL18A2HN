
#Bài 1: Nhập vào số nguyên dương n. 
#In ra màn hình dãy số các số nguyên tố nhỏ hơn n theo thứ tự từ nhỏ đến lớn
ds_nguyen_to = []
while True:
    n = input("Nhap vào so nguyen duong: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(1, n):
    if i == 1:
        ds_nguyen_to.append(i)
        continue
    for j in range(1, i):
        if i%j == 0 and j != 1 and i != j:
            break
    else:
        ds_nguyen_to.append(i)

ds_nguyen_to.sort()
print(ds_nguyen_to)


#Bài 2: Nhập vào dãy A gồm n phần tử từ bàn phím. 
#Tính tổng các phần tử trong dãy A
ds_so = []
while True:
    n = input("Nhap vào so phan tu n trong danh sach: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(n):
    while True:
        so = input(f"Nhap gia tri so thu (i + 1): ")
        if n.isdigit() == False:
            print("Yeu cau nhap vao so!!")
        else:
            so = float(so)
            break
    ds_so.append(so)


ds_so = []

while True:
    n = input("Nhập vào số phần tử n trong danh sách: ")
    if not n.isdigit():  
        print("Yêu cầu nhập lại số nguyên dương!!")
    else:
        n = int(n)
        break
for i in range(n):
    while True:
        so = input(f"Nhập giá trị số thứ {i + 1}: ")
        if so.lstrip('-').replace('.', '', 1).isdigit():  
            so = float(so)  
            ds_so.append(so)  
            break 
        else:
            print("Bạn hãy nhập lại!")
tong = sum(ds_so)
print(f"Tổng các số vừa nhập: {tong}")




#Bài 3: Nhập vào số nguyên dương n.
#In ra màn hình: 
# - Danh sách A gồm các số lẻ nhỏ hơn n
# - Danh sách B gồm các số chẵn nhỏ hơn n
#Sắp xếp dãy số theo thứ tự giảm dần

while True:
    try:
        n = int(input("Nhập vào số nguyên dương n: "))
        if n > 0:
            break 
        else:
            print("Số vừa nhập không phải là số nguyên dương!")
    except ValueError:
        print("Vui lòng nhập một số nguyên!")
A = []
B = []
for i in range(n-1, -1, -1):
    if i % 2 != 0:
        A.append(i) 
    else:
        B.append(i)  
print(f"Danh sách A (số lẻ):{A}")
print(f"Danh sách B (số chẵn):{B}")


#Bài 4: Viết chương trình sinh ra ma trận K kích cỡ m*n chỉ chứa số 0
n = int(input("Nhap vapp so cot cua ma tran m = "))
n = int(input("Nhap vao so hang cua ma tran n = "))
#0 ... m
#.     .
#.     .
#.     .
#n ... 0
ma_tran_a = [[0,0,0]
             [0,0,0],
             [0,0,0]]
ma_tran_a = []
for hang in range(n):
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu_trong_hang.append(0)
    ma_tran_a.append(phan_tu_trong_hang)
print(ma_tran_a)

ma_tran_a = [[0]*m]*n #=> [0,,0,0,0,...,m]
print(ma_tran_a)


#Bài 5: Viết chương trình nhập vào n. Sinh ra ma trận đơn vị I kích cỡ n*n
#1 0 0 0
#0 1 0 0
#0 0 1 0
#0 0 0 1
n = int(input("Nhap vao n = "))
ma_tran_don_vi = []
for i in range(n):
    phan_tu_trong_hang = [0]*i + [1] + [0]*(n-1-i)
    ma_tran_don_vi.append(phan_tu_trong_hang)
print(ma_tran_don_vi)



#Bài 6: Viết chương trình nhập vào ma trận A kích cỡ m*n và in ra màn hình

#Bài 7: Viết chương trình đảo vị trí hai hàng i, j của ma trận A kích cỡ m*n
#1 0 0 0
#0 1 0 0
#0 0 1 0
#0 0 0 1
i = int(input("Nhap vao hang i: "))
j = int(input("Nhap vao hang J: "))
[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
temp = ma_tran_don_vi[i]
ma_tran_don_vi[i] = ma_tran_don_vi[j]
ma_tran_don_vi[j] = temp
print(ma_tran_don_vi)


#Bài 8: Viết chương trình đảo vị trí hai cột i, j của ma trận A kích cỡ m*n
# Nhập các thông số cơ bản
m, n = 3, 3  # Kích thước của ma trận
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
i, j = 0, 2  # Hai cột cần đảo vị trí

# Đảo vị trí hai cột i và j
for row in range(m):
    A[row][i], A[row][j] = A[row][j], A[row][i]

# In kết quả
for row in A:
    print(row)

#Bài 9: Viết chương trình nhập vào hai ma trận A, B có cùng kích thước.
#Tính:
# - Tổng hai ma trận A, B
# - Hiệu hai ma trận A, B
# - Tích của ma trận A với số k nhập từ bàn phím
# - Tích hai ma trận A, B
# - Ma trận đối xứng của ma trận A
m = int(input("nhap vap so hang cua ma tran : m = "))
n = int(input("nhap vao so cot cua ma tran : n = "))
ma_tran_A = []
print("nhap cac phan tu cua ma tran A: ")
for i in range(m):
    hang = []
    for j in range(n):
        phan_tu = int(input(f"nhap phan tu A[{i+1}][{j+1}] = ")) 
        hang.append(phan_tu) 
    ma_tran_A.append(hang) 
ma_tran_B = []
print("nhap cac phan tu cua ma tran B: ")
for i in range(m):
    hang = []
    for j in range(n):
        phan_tu = int(input(f"nhap phan tu B[{i+1}][{j+1}] = ")) 
        hang.append(phan_tu) 
    ma_tran_B.append(hang)  
print("ma tran A vua lap la:")
for a in ma_tran_A:
    print(a) 
print("ma tran B vua lap la:")
for b in ma_tran_B:
    print(b) 
# print("tong 2 ma tran la")
# tong_ma_tran = []
# for i in range(m):
#     hang = []
#     for j in range(n):
#         tong_phan_tu = ma_tran_A[i][j] + ma_tran_B[i][j]
#         hang.append(tong_phan_tu) 
#     tong_ma_tran.append(hang)
# for c in tong_ma_tran:
#     print(c)
# print("hieu 2 ma tran la")
# hieu_ma_tran = []
# for i in range(m):
#     hang = []
#     for j in range(n):
#         hieu_phan_tu = ma_tran_A[i][j] - ma_tran_B[i][j]
#         hang.append(hieu_phan_tu) 
#     hieu_ma_tran.append(hang)
# for d in hieu_ma_tran:
#     print(d)
# print("tich cua ma tran A voi 1 so k la")
# k = int(input("nhap vao so k: "))
# tich_ma_tran_Ak = ma_tran_A.copy()
# for hang in range(len(tich_ma_tran_Ak)):
#     for cot in range(len(tich_ma_tran_Ak[hang])):
#         tich_ma_tran_Ak[hang][cot] = tich_ma_tran_Ak[hang][cot] * k
# for d in tich_ma_tran_Ak:
#     print(d)
print("tich 2 ma tran la")
if m != n:
    print("khong tinh duoc tich 2 ma tran")
else:
    tich_ma_tran_AB = []
    for i in range(m):
        hang = []
        tong = 0
        ton = 0
        for j in range(n):
            tong = ma_tran_A[i][j] * ma_tran_B[i][j]    
            ton = ma_tran_A[i+1][j+1] * ma_tran_B[i+1][j+1]
            
            hang.append(tong+ton)
        tich_ma_tran_AB.append(hang)
    for e in tich_ma_tran_AB:
        print(e)
#Bài 10: Lập một danh sách với n sinh viên bao gồm thông tin tên và điểm tổng kết cuối năm của các sinh viên đó
# thong_tin_sinh_vien = {"Hung": 4.0}
# ds_sinh_vien = [{"Hung": 4.0},{"Hung": 4.0},{"Hung": 4.0},{"Hung": 4.0}]
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {ten: diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)

#Bài 11: Viết lệnh in danh sách sinh viên ở bài 10. Có dạng:
#Ten    Diem
#Dung   10.0
#Quang  5.3
#Trang  7.5
ds_sinh_vien = ["ten   diem"]
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {ten: diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)
print("danh sach sinh vien")
for i in ds_sinh_vien:
    print(i)
#Bài 12: Viết lệnh xóa thông tin của sinh viên trong danh sách sinh viên ở bài 10 ứng với tên được nhập vào bàn phím

ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = thong_tin_sinh_vien.append(ten)
    ds_sinh_vien.append(thong_tin_sinh_vien)
for i in ds_sinh_vien:
    print(i)

#Bài 13: Viết lệnh thêm một sinh viên vào danh sách sinh viên ở bài 10. Với điều kiện:
# - Nếu tên sinh viên đã tồn tại, thông báo: "Thông tin sinh viên đã tồn tại"
# - Nếu chưa có sinh viên này, thông báo: "Đã thêm sinh viên"

#Bài 14: Viết lệnh sửa thông tin của một sinh viên ở bài 10 ứng với tên được nhập vào bàn phím

#Bài 15: Viết một chương trình quản lý một danh sách sinh viên.
# Danh sách sinh viên chứa các thông tin:
# - "Mã sinh viên"
# - "Họ đệm"
# - "Tên"
# - "Điểm toán"
# - "Điểm lý"
# - "Điểm hóa"
# - "Điểm trung bình" được tính từ 3 điểm toán, lý, hóa
# Thiết kế chương trình quản lý có menu như sau:
# 1. Xem danh sách sinh viên
# 2. Nhập thông tin sinh viên mới vào danh sách
# 3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên
# 4. Xóa thông tin sinh viên ứng với mã sinh viên
# 5. Thoát chương trình

print("MENU:")
print("1. Xem danh sách sinh viên")
print("2. Nhập thông tin sinh viên mới vào danh sách")
print("3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
print("4. Xóa thông tin sinh viên ứng với mã sinh viên")
print("5. Thoát chương trình")
lua_chon = input("Nhap lua chon ma ban muon su dung: ")
if lua_chon.isdigit() == False:
    print("Yeu cau nhap lai")
else:
    lua_chon = int(lua_chon)
    if lua_chon == 1:
        print("chay 1")
    elif lua_chon == 2:
        print("chạy 2")
    elif lua_chon == 3:
        print("chay 3")
    elif lua_chon == 4:
        print("chay 4")
    elif lua_chon == 5:
        print("thoat chuong trinh")
        break
    else: 
        print("Yeu cau nhap lai")
  