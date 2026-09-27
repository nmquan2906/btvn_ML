import numpy as np

# BÀI 3.28
w_old = np.array([-2, 1, 0])
x = np.array([2, 3, 1])
y_true = 1

wTx_old = np.dot(w_old, x)
y_pred = 1 if wTx_old > 0 else -1
print(f"1. w^T*x ban đầu = {wTx_old} -> Nhãn dự đoán = {y_pred}.")
print(f"   Mẫu bị phân lớp sai? -> {'CÓ' if y_pred != y_true else 'KHÔNG'} (Vì nhãn thực tế là 1)")

if y_pred != y_true:
    w_new = w_old + 1 * y_true * x
    print(f"\n2. Trọng số w mới sau cập nhật = {w_new}")

    wTx_new = np.dot(w_new, x)
    print(f"3. Giá trị w^T*x sau cập nhật = {wTx_new}")
    print(f"   (Lúc này w^T*x > 0 nên mô hình sẽ dự đoán đúng nhãn là 1)")