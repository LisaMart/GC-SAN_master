import pickle
import random
import os

# Function to load data from a pickle file
def load_pickle_data(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

# Function to save data to a pickle file
def save_pickle_data(data, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

# Function to select a subset of data based on the percentage
def take_subset(data, percentage=50):  # Change percentage to 50
    subset_size = int(len(data) * (percentage / 100))

    # If the subset size is too small (less than 1), raise an error or take all data
    if subset_size == 0:
        print(f"Warning: Dataset is too small. Selecting all {len(data)} elements.")
        subset_size = len(data)  # Take all data if the subset size is too small
    return random.sample(data, subset_size)

# Paths to the original and output files
base_path = r'C:\Users\lisa\python_practice\GC-SAN_master\datasets\diginetica'
train_file = base_path + r'\train.txt'
test_file = base_path + r'\test.txt'

# Load data
train_data = load_pickle_data(train_file)
test_data = load_pickle_data(test_file)

# Check if the data is empty
if len(train_data) == 0:
    raise ValueError("Training data is empty!")
if len(test_data) == 0:
    raise ValueError("Test data is empty!")

# Check the size of the data
print(f"Size of training data: {len(train_data)}")
print(f"Size of test data: {len(test_data)}")

# Take 50% of the data
train_data_subset = take_subset(train_data, 50)  # 50% of the training data
test_data_subset = take_subset(test_data, 50)    # 50% of the test data

# Save the new files
save_pickle_data(train_data_subset, base_path + r'\train_50.txt')
save_pickle_data(test_data_subset, base_path + r'\test_50.txt')

print("Process completed. 50% sample data saved to 'train_50.txt' and 'test_50.txt'.")