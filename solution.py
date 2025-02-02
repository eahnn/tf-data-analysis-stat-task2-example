import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 784066571 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = (1 - p) / 2
    loc = 2 * x.mean()
    scale = 2 * np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * uniform.ppf(alpha), \
           loc - scale * uniform.ppf(1 - alpha)
