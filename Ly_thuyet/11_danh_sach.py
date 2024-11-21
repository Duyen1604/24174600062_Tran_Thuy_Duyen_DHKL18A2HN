#Khởi tạo một danh sách
a = []
b = ["abc", 1, 5, 6.7, []]

a = 5
b = a
b = a + 1
print(a)
print(b)

# Bộ nhớ của list được chia sẻ cho nhau
a = ["abc", "def", "ghifk", 1, 2, 3]
b = a
b[0] = "chuoi thay doi"
print(a)
print(b)


#Phương thức sao lưu
a = ["abc", "def", "ghijk", 1, 2, 3]
b = a.copy()
b[0] = "chuoi thay doi"
print(a)
print(b)


#thay đổi giá trị trong danh sách
a = ["abc", "def", "ghijk", 1, 2, 3]
a[3] = 10  
a[1:4] = [6,7,8]
print(a)
#độ dài của danh sách 
print(len(a))
#các phương thức
# Phương thức thêm và bớt
# Thêm vào cuối danh sách
a.append("abcd")
a.append([1,2,3])
print(a)

#thêm nhiều phàn tử vào danh sách
a.extend([1,2,3])
print(a)
#Xóa tất cả các phần tử trong danh sách
a.clear()
#xóa tất cả các phần tử trong danh sách sử dụng và xóa nó khỏi danh sách 
b = a.pop()
print(a)
print(b)

# lấy phần tử cuối cùng ra khỏi danh sách
b = a.pop()
print(a)
print(b)
#xóa một phàn tử trong chuỗi
a.remove("abc")
#thêm một phần tử vào vị trị index
a.insert(3,  "kkk")
#Thêm số lần phần tử xuất hiện
a.count("abc")

#Đảo ngược danh danh
a.reverse()
#trả về vị trí xuất hiện đầu tiên của phần tử trong danh sách
a.index(1)

#sắp xếp danh sách
a.sort(revere=True)

b =[[1,2,[4,5,6]],"abc",[3,"rts",5]]
print(b[0][2][1])

# bài tập xử lý ma trận
matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
n = 8
#Nhân ma trận a với n
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n

print(matrix_a)

#yêu cầu về nhà:
#Thực hiện các phép tính cơ bản của ma trận với ma trận

#yêu cầu về nhà
#Thực hiện các phép tính cơ bản của ma trận với số và của ma trận với ma trận
#xử lý ma trận
matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
n = 8
#nhân ma trận a với n
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n

print(matrix_a)
#cộng hai ma trận
ma_tran_a = [[0, 5, 8],
             [8, 6, 9],
             [1, 1, 2],]

ma_tran_b = [[0, 7, 1],
             [8, 6, 5],
             [1, 2, 2],]
ket_qua = [[0, 0, 0],
           [0, 0, 0],            
           [0, 0, 0],]     
for h in range(len(ma_tran_a)):
    for c in range(len(ma_tran_a[0])):
        ket_qua[h][c] = ma_tran_a[h][c] + ma_tran_b[h][c]
    
print(f"nhan hai ma tran: {ket_qua}")

#trừ 2 ma trận
ma_tran_1 = [[2, 4, 5, 6],
             [3, 5, 6, 1],
             [4, 9, 0, 3],
             [2, 2, 8, 6],]
ma_tran_2 =  [[2, 4, 5, 6],
              [5, 4, 6, 1],
              [4, 7, 0, 3],
              [1, 2, 8, 6],]
ket_qua = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],]
for hang in range(len(ma_tran_1)):
    for cot in range(len(ma_tran_1[0])):
        ket_qua[hang][cot]=ma_tran_1[hang][cot] - ma_tran_2[hang][cot]
        
for tru_hai_ma_tran in ket_qua:  # Dùng dấu gạch dưới nếu không cần tên biến
    print(f"tru hai ma tran; {tru_hai_ma_tran}")



#nhân 2 ma trận 
matrix_a = [[2, 4],
            [2, 7],]
matrix_b = [[3, 6],
           [2, 2],]
ket_qua = [[0, 0],
           [0, 0],]
for h in range(len(matrix_a)):
    for c in range(len(matrix_a[h])):
        ket_qua[h][c]= matrix_a[h][c] * ma_tran_b[h][c]
print(f"nhan hai ma tran {ket_qua}")
