# -*- coding: utf-8 -*-
import pickle
import random

# ������� ��� �������� ������ �� pickle �����
def load_pickle_data(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

# ������� ��� ���������� ������ � pickle ����
def save_pickle_data(data, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

# ������� ��� ������� 50% ������ ��������� �������
def take_subset(data, percentage=50):
    subset_size = int(len(data) * (percentage / 500))
    return random.sample(data, subset_size)

# �������� ���� � �������� � ����������� ������
base_path = r'C:\Users\lisa\python_practice\GC-SAN_master\datasets\diginetica'
train_file = base_path + r'\train.txt'
test_file = base_path + r'\test.txt'

# ��������� ������
train_data = load_pickle_data(train_file)
test_data = load_pickle_data(test_file)

# ����� 50% ������
train_data_subset = take_subset(train_data, 50)  # 50% ������ ��� ��������
test_data_subset = take_subset(test_data, 50)    # 50% ������ ��� ������������

# ��������� ����� �����
save_pickle_data(train_data_subset, base_path + r'\train_50.txt')
save_pickle_data(test_data_subset, base_path + r'\test_50.txt')

print("The process is complete. A sample of 50% of the data is saved in train_50.txt and test_50.txt")