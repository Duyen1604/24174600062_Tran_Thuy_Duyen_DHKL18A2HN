#set - Tập hợp trong python
#Tính chất của tập hợp 
#- không có sắp xép, không có thức tự
#- những phần tử trong tập hợp là đặc hiệu (unique)
#- các giá trị trong set có thể thay đổi được tuy nhiên nó chỉ có thể chứa các phần tử 
#mang giá trị không đổi

list_a = ["fol", "baa", "baal"]

set_a = {1,2,3,"abc"}
set_b = set(list_a) #=>  {"fol", "baa", "baal"}

#Kiểm tra số phần tử trong tập hợp 
len(set_a)
#kiểm tra phần tử có tông tại trong tập hợp không
2 in set_a #=> trả về kiểu dữ liệu boolean: True

if 2 in set_a:
    print("2 co trong tap hop")

2 not in set_a

if 2 not in set_a:
    print("2 khong co trong tap hop")

#kiểm tra so sánh 2 tập hợp 
# tập hợp A
tap_hop_a = {"a", "b", "c", "d"}
#tập hợp B
tap_hop_b = {1, 2, 3, "a", "b"}

#kiểm tra tập hợp A có phải tập hợp con của tập hợp B hay không?
tap_hop_a.issubset(tap_hop_b) #=> trả về kiểu dữ liệu boolean
tap_hop_a < tap_hop_b
tap_hop_a <= tap_hop_b

#kiểm tra tập hợp A có phải tập cha của tập hợp B hay không?
tap_hop_a.issuperset(tap_hop_b)
tap_hop_a > tap_hop_b
tap_hop_a >= tap_hop_b

#kiểm tra xem 2 tập hợp có giao nhau hay không?
tap_hop_a.isdisjoint(tap_hop_b) #=> trả về True nếu không có phần tử chung và False nếu có

#các tính toán trong tập hợp
# tập hợp A
tap_hop_a = {"a", "b", "c", "d"}
#tập hợp B
tap_hop_b = {1, 2, 3, "a", "b"}
#tập hợp C
tap_hop_c = {1,2,3,4,5,6}

#phép hợp tập hợp
tap_hop_tong = tap_hop_a.union(tap_hop_b)
tap_hop_tong = tap_hop_a.union(tap_hop_b).union(tap_hop_c)
tap_hop_tong = tap_hop_a | tap_hop_b | tap_hop_c

#phép lấy phần giao giữa các tập hợp 
tap_hop_giao = tap_hop_a.intersection(tap_hop_b)
tap_hop_giao = tap_hop_a.intersection(tap_hop_b).intersection(tap_hop_c)
tap_hop_giao = tap_hop_a & tap_hop_b & tap_hop_c
#phép lấy phần tử trong một tập hợp mà không có không các tập hợp còn lại
tap_hop_khac = tap_hop_a.difference(tap_hop_b)
tap_hop_khac = tap_hop_a.difference(tap_hop_b).difference(tap_hop_c)
tap_hop_khac = tap_hop_a - tap_hop_b - tap_hop_c
#phép lấy hợp của phần có trong tập hợp này mà không có trong tập hợp kia
tap_hop_khac_giao = tap_hop_a.symmetric_difference(tap_hop_b)
tap_hop_khac_giao = tap_hop_a.symmetric_difference(tap_hop_b).symmetric_difference(tap_hop_c)
tap_hop_khac_giao = tap_hop_a ^ tap_hop_b ^ tap_hop_c

#chỉnh sửa tập hợp
tap_hop_a = {1, 2, 3}
#thêm phần tử vào a
tap_hop_a.add(9)
tap_hop_a.update([4,5,6]) #tương tự với việc hợp 2 tập hợp
# a = 1
# b = 2
# a += b
# a = a + b
tap_hop_a = tap_hop_a | tap_hop_b
tap_hop_a |= tap_hop_b


#giữ lại các phần tử là giao của hai tập hợp
tap_hop_a.intersection_update(tap_hop_b)
tap_hop_a = tap_hop_a & tap_hop_b
tap_hop_a &= tap_hop_b

#giữ lại các phần tử có trong tập xét mà không có trong tập còn lại
tap_hop_a.difference_update(tap_hop_b)
tap_hop_a = tap_hop_a - tap_hop_b
tap_hop_a -= tap_hop_b

#giữ lại các phần tử không tồn tại trong cả hai tập hợp
tap_hop_a.symmetric_difference_update(tap_hop_b)
tap_hop_a = tap_hop_a ^ tap_hop_b
tap_hop_a ^= tap_hop_b

#xóa phần tử trong tập hợp
#xóa 1 phàn tử
tap_hop_a.remove(2)
#xÓa nhiều phần tử trong một tập hợp
tap_hop_a.difference_update({1,2})
#xóa phần tử không gây lỗi
tap_hop_a.discard(2)
#lấy 1 phần tử bất kỳ ra để sử dụng và xóa phần tử này khỏi tập hợp
tap_hop_a.pop()
#xóa toàn bộ tập hợp
tap_hop_a.clear()

tap_hop = {"a","b","c", "d", "e"}
while tap_hop:
    a = tap_hop.pop()
    print(a)
    




