
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
