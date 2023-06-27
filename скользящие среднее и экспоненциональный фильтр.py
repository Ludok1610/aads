# временной ряд
data = [10, 13, 15, 12, 16, 18, 19, 20, 22, 25]

# скользящие среднее
def moving_average(data, window_size):
    smoothed = []
    for i in range(len(data)):
        if i < window_size:
            smoothed.append(sum(data[:i+1]) / len(data[:i+1]))
        else:
            smoothed.append(sum(data[i-window_size+1:i+1]) / window_size)
    return smoothed

window_size = 3
smoothed = moving_average(data, window_size)
print(smoothed)

# Экспоненциональный фильтр
def exponential_filter(data, alpha):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(alpha * data[i] + (1 - alpha) * smoothed[i-1])
    return smoothed

alpha = 0.5
smoothed = exponential_filter(data, alpha)
print(smoothed)

