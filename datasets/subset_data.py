import pickle
import random
import os

# Функция для загрузки данных из pickle файла
def load_pickle_data(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

# Функция для сохранения данных в pickle файл
def save_pickle_data(data, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

# Функция для выборки 10% данных случайным образом
def take_subset(data, percentage=10):
    subset_size = int(len(data) * (percentage / 100))
    if subset_size == 0:  # Если выборка слишком мала
        raise ValueError("Размер выборки слишком мал, данные не могут быть выбраны.")
    return random.sample(data, subset_size)

# Заданные пути к исходным и сохраненным файлам
base_path = r'C:\Users\lisa\python_practice\GC-SAN_master\datasets\diginetica'
train_file = base_path + r'\train.txt'
test_file = base_path + r'\test.txt'

# Загружаем данные
train_data = load_pickle_data(train_file)
test_data = load_pickle_data(test_file)

# Проверяем, что данные не пустые
if len(train_data) == 0:
    raise ValueError("Данные для тренировки пусты!")
if len(test_data) == 0:
    raise ValueError("Данные для тестирования пусты!")

# Берем 10% данных
train_data_subset = take_subset(train_data, 10)  # 10% данных для обучения
test_data_subset = take_subset(test_data, 10)    # 10% данных для тестирования

# Сохраняем новые файлы
save_pickle_data(train_data_subset, base_path + r'\train_10.txt')
save_pickle_data(test_data_subset, base_path + r'\test_10.txt')

print("Процесс завершен. Выборка 10% данных сохранена в 'train_10.txt' и 'test_10.txt'.")