#Đệ quy - recursion - sự tái lặp

#ví dụ: dãy fibonacci
#0 + 1 = 1
#1 + 1 = 2
#1 + 2 = 3
#2 + 3 = 5
#3 + 5 = 8
#5 + 8 =13
#......
#Số tiếp theo = số hiện tại + số trước đó
#F1 = 2
#F2 = 2
#F3 = F1 + F2 = 2 + 3 = 5
#F(n) = F(n-1) + F(n-2) => đẹ quy trên toán học

#Đệ quy trong lập trình là các hàm có lời gọi chính nó trong nội hàm
def f():
    f()
#=> hàm đẹ quy hoạt động không khác gì vòng lặp

f()

import sys
#xem giới hạn số vòng đệ quy
sys.getrecursionlimit()
#điều chỉnh giới hạn vòng đệ quy
sys.getrecursionlimit(10000)

#yêu cầu khi viết đệ quy:
#1. Thâm số của hàm đệ quy cần thay đổi sau mỗi lần lặp đệ quy
#2. cần có điểm dừng cho lặp đệ quy

n = 10
While True:
    n = n + 1




n = 10
def f(x):
    if x == 20:
        return x
    
    return f(x + 1)

#Lần 1: x = 10 if False -> f(x+1) x = 11
#Lân 2: x = 11 if False -> f(x+1) x = 12
#Lần 3: x = 12 if False -> f(X+1) x = 13
#...
#Lần 9: x = 19 if False => f(x+1) x = 20
#lần 10: x = 20 if True -> 20 trả về cho lần 9, hủy lần 10
#Lần 9: nhận f(x + 1) = 20 -> 20 trả về cho lần 8, hủy lần 9
#...
#Lần 2: nhận f(x + 1)


#Bài tập Finonacci
#in ra n số Fibonacci
n = int(input("Nhap vao so nguyen duong n: "))
#F(n) = F(n - 1) + F(n - 2)
def fibonacci(n):
    #n = 2 => F_2 = 1
    if n == 2:
        return 1
    #n = 1 => F_1 = 1
    elif n == 1:
        return 1
    #n = 0 => F_0 = 0
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(n):
    print(fibonacci(i), end=" ")


#bài tập giai thừa n!

    







