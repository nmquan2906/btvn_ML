import numpy as np

w = np.array([1, 2, -10])
x = np.array([3, 4, 1])
y_true = -1

wTx = np.dot(w, x)
print(f"1. Giá trị w^T*x = {wTx}")

y_pred = 1 if wTx > 0 else -1
print(f"2. Nhãn dự đoán = {y_pred}")

is_misclassified = (y_pred != y_true)
print(f"3. Nhãn thực tế y = {y_true}. Điểm dữ liệu bị phân lớp sai? -> {'CÓ' if is_misclassified else 'KHÔNG'}")