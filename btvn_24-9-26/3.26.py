def f(x):
    return x**2 - 4*x + 5

def f_prime(x):
    return 2*x - 4

x = 5
eta = 0.2

print("1. Đạo hàm f'(x) = 2x - 4")
print(f"   Khởi tạo: x0 = {x}, f(x0) = {f(x):.4f}\n")

print("Thực hiện cập nhật:")
for i in range(1, 5):
    x = x - eta * f_prime(x)
    print(f"Bước {i}: x{i} = {x:.4f}, f(x{i}) = {f(x):.4f}")

print("\n4. Nhận xét:")
print("Giá trị x giảm dần từ 5 xuống 2.3888 (tiến dần về nghiệm tối ưu x=2).")
print("Giá trị hàm số f(x) giảm liên tục từ 10 xuống 1.1512 (tiến về cực tiểu là 1).")
print("-> Thuật toán hoạt động đúng hướng và đang hội tụ ổn định.")