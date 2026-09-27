import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class MyPerceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.lr = learning_rate
        self.epochs = n_iterations
        self.w = None

    def fit(self, X, y):
        self.w = np.zeros(X.shape[1] + 1)
        X_bias = np.insert(X, 0, 1, axis=1)
        for _ in range(self.epochs):
            for idx, x_i in enumerate(X_bias):
                linear_output = np.dot(x_i, self.w)
                y_pred = 1 if linear_output > 0 else -1
                if y[idx] != y_pred:
                    self.w += self.lr * y[idx] * x_i

    def predict(self, X):
        X_bias = np.insert(X, 0, 1, axis=1)
        linear_output = np.dot(X_bias, self.w)
        return np.where(linear_output > 0, 1, -1)

print("Đang huấn luyện mô hình...")
X, y = make_classification(n_samples=1000, n_features=4, n_classes=2, random_state=42)
y = np.where(y == 0, -1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MyPerceptron(learning_rate=0.1, n_iterations=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Kết quả đánh giá mô hình phân lớp Perceptron:")
print(f"- Accuracy  : {accuracy_score(y_test, y_pred):.4f}")
print(f"- Precision : {precision_score(y_test, y_pred):.4f}")
print(f"- Recall    : {recall_score(y_test, y_pred):.4f}")
print(f"- F1-Score  : {f1_score(y_test, y_pred):.4f}")