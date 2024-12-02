# -*- coding: utf-8 -*-
import pickle
import random

# Функция для загрузки данных из pickle файла
def load_pickle_data(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

# Функция для сохранения данных в pickle файл
def save_pickle_data(data, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

# Функция для выборки 50% данных случайным образом
def take_subset(data, percentage=50):
    subset_size = int(len(data) * (percentage / 500))
    return random.sample(data, subset_size)

# Заданные пути к исходным и сохраненным файлам
base_path = r'C:\Users\lisa\python_practice\GC-SAN_master\datasets\diginetica'
train_file = base_path + r'\train.txt'
test_file = base_path + r'\test.txt'

# Загружаем данные
train_data = load_pickle_data(train_file)
test_data = load_pickle_data(test_file)

# Берем 50% данных
train_data_subset = take_subset(train_data, 50)  # 50% данных для обучения
test_data_subset = take_subset(test_data, 50)    # 50% данных для тестирования

# Сохраняем новые файлы
save_pickle_data(train_data_subset, base_path + r'\train_50.txt')
save_pickle_data(test_data_subset, base_path + r'\test_50.txt')

print("The process is complete. A sample of 50% of the data is saved in train_50.txt and test_50.txt")