# Bài tập về chuỗi ký tự
# Dạng thứ nhât: áp dụng xử lý chuỗi ký tự bằng các phương thức có sẵn
# Bài 1: Nhận vào một chuoiix ký tự bất kỳ. Đếm số ký tự trong chuỗi
# cách 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
so_ky_tu_trong_chuoi = len(chuoi_nhap_vao)
print(f"So ky tu trong chuoi là {so_ky_tu_trong_chuoi}")
# cách 2:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem = 0
for chu in chuoi_nhap_vao:
    print(chu)
    dem = dem + 1
print(f"So ky tu trong chuoi la {dem}")

# Bài 2: Nhập vào một chuỗi bất kỳ. Xóa các khoảng trống ở đâu và cuối chuỗi
#Cách 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
chuoi_da_xoa_khoang_trong = chuoi_nhap_vao.strip()
print(f"Chuoi sau khi xoa khoang trong {chuoi_da_xoa_khoang_trong}")
#cách 2:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
#"    chuoi nhap vao            "
chuoi_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_nhap_vao:
    if chu == " " and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau == True
        chuoi_xu_ly_dau = chuoi_xu_ly_dau + chu
chuoi_dao_nguoc = chuoi_xu_ly_dau[::-1]

chuoi_ket_qua = chuoi_dao_nguoc_xu_ly_dau[::-1]
print(f"chuoi sau khi xoa khoang trong {chuoi_ket_qua}")

# bài 3: Nhập vào một chuỗi bất kỳ. Xóa tất cả khoảng trống thừa trong chuỗi
#ví dụ:  "   chuoi    nhap       vao      "
#cách 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)
#"chuoi nhap vao"
print(f"Chuoi ket qua: {chuoi_ket_qua}"):






# cách 2: BTVN xử lý yêu cầu trên mà không sử dụng các phương thức
nhap_chuoi_vao = input("Nhập chuỗi của bạn vào :")
bien_luu_vao = []
bien_hien_tai = ""
for chu in nhap_chuoi_vao :
    if chu != " "


# Dạng thứ hai: áp dụng kết hợp xử lý vòng lặp và xử lý chuỗi ký tự
#Bài 1:Nhập vào một chuỗi ký tự bất kỳ. Đếm xem có bao nhiêu ký tự là số bao nhiêu ký tự đặc biệt
# isalpha(): kiểm tra chữ cái
# isdigit(): kiểm tra số

chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
for chu in chuoi_nhap_vao:




#Bài 2: Nhập vào một số bất kỳ, kiểm tra xem số này có phải số nguyên tố hay không

n = input("Nhap vao ")



# BÀi 3:Nhập vào 2 số thực bất kỳ. Tính tổng 2 số thực đó
While True:
a = input("Nhap vao so thuc a: ") #"-7.86"
so_kiem_tra = a.replace(".","")
so_kiem_tra = so_kiem_tra.replace(".","")
if a.isdigit() == False:
    print("Gia tri nhap vao khong phai gia tri so")
else:
    dem_dau_cham = a.count(".")
    dem_dau_gach = a.count("-")
    if dem_dau_cham = 









