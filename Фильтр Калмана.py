import numpy as np

def kalman_filter(data):
    # Определение начального состояния и ковариационной матрицы
    x = np.mean(data)
    P = np.var(data)
    # Определение матриц для модели системы и измерений
    A = np.array([1])
    H = np.array([1])
    Q = np.array([np.var(data)])
    R = np.array([[np.var(data)]])
    # Применение фильтра Калмана для сглаживания временного ряда
    smoothed = [x]
    for i in range(1, len(data)):
        # Предсказание следующего состояния
        x_pred = A * x
        P_pred = A * P * A.T + Q
        # Обновление состояния на основе новых измерений
        K = P_pred * H.T * np.linalg.inv(H * P_pred * H.T + R)
        x = x_pred + K * (data[i] - H * x_pred)
        P = (np.eye(len(K)) - K * H) * P_pred
        smoothed.append(x.tolist()[0])
    return smoothed

data = [10, 13, 15, 12, 16, 18, 19, 20, 22, 25]
data = np.array(data).reshape(-1, 1)  # преобразование одномерного массива в двумерный
smoothed = kalman_filter(data)
print(smoothed)