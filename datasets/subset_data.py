import pickle
import random
import os

# ������� ��� �������� ������ �� pickle �����
def load_pickle_data(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

# ������� ��� ���������� ������ � pickle ����
def save_pickle_data(data, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

# ������� ��� ������� 10% ������ ��������� �������
def take_subset(data, percentage=10):
    subset_size = int(len(data) * (percentage / 100))
    if subset_size == 0:  # ���� ������� ������� ����
        raise ValueError("������ ������� ������� ���, ������ �� ����� ���� �������.")
    return random.sample(data, subset_size)

# �������� ���� � �������� � ����������� ������
base_path = r'C:\Users\lisa\python_practice\GC-SAN_master\datasets\diginetica'
train_file = base_path + r'\train.txt'
test_file = base_path + r'\test.txt'

# ��������� ������
train_data = load_pickle_data(train_file)
test_data = load_pickle_data(test_file)

# ���������, ��� ������ �� ������
if len(train_data) == 0:
    raise ValueError("������ ��� ���������� �����!")
if len(test_data) == 0:
    raise ValueError("������ ��� ������������ �����!")

# ����� 10% ������
train_data_subset = take_subset(train_data, 10)  # 10% ������ ��� ��������
test_data_subset = take_subset(test_data, 10)    # 10% ������ ��� ������������

# ��������� ����� �����
save_pickle_data(train_data_subset, base_path + r'\train_10.txt')
save_pickle_data(test_data_subset, base_path + r'\test_10.txt')

print("������� ��������. ������� 10% ������ ��������� � 'train_10.txt' � 'test_10.txt'.")