# Từ điển trong python
#- Lưu trữ các kiểu dữ liệu khác nhau
#- Có thể thay đỏi các giá trị trong tử điển
#- Có thể lưu các kiểu dữ liệu tuần tự khác tạo thành mạng lưới
#- Không thể sử dụng chỉ mục mà thay vào đó các khóa (key)
#- Tất cả các giá trị phải truy cập bằng khóa
tu_dien = {"abc":1,
            3:[1,2,3],
            (0,1):"hijk"}
#khai báo từ điển
#- Từ điển sử dụng ngoặc {} để khởi tạo
#- Mỗi phần tử phải theo cặp khóa: giá trị
#- Khóa trong từ điển phải là không thể thay đổi
#- Khóa không được giống nhau
list_a = [(0, "Hoang"), (1, "Cuong"), (2, "Lam")]
tu_dien_a = dict(list_a)
#Từ điển trong python có cách hoạt động giông như JSON


#Truy cập các phần tử trong từ điển
tu_dien = {"a": 1,
           "b": 2,
           "c": 3}
tu_dien["a"]
#lấy tập hợp khóa
tap_hop_khoa = tu_dien.key()
#lấy danh sách giá trị
danh_sach_gia_tri= list(tu_dien.values())
#lấy danh sách các cặp khóa giá trị
danh_sach_khoa_gia_tri = list(tu_dien.items())

#thêm giá trị vào trong từ điển
tu_dien = {"a": 1,
           "b": 2,
           "c": 3}

tu_dien["d"] = 4

tu_dien.update({"e": 5, "f": 6, "g": 7})
print(tu_dien)

#xóa phần tử trong từ điền
tu_dien.clear() #xóa toàn bộ các giá trị
tu_dien.pop("b") #lấy ra và xóa phần tử tại khóa
tu_dien.popitem() #lấy ra và xóa phần tử bất kỳ