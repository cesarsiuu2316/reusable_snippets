from zlib import crc32
import numpy as np
from sklearn.model_selection import train_test_split

# Splitting data with a hash ensures data is always split the same way, even if you add new data later or shuffle the data. This is particularly useful when you have a unique identifier for each instance in your dataset, such as an ID column. By using the hash of the identifier, you can determine whether an instance should be in the training set or the test set based on a specified test ratio. This method is more robust than random splitting, which can lead to different splits each time you run it, especially if you add new data to your dataset.

def is_id_in_test_set(identifier, test_ratio):
    """
    This function checks if a given identifier should be in the test set based on its hash value.
    It uses the crc32 function to compute a hash of the identifier and compares it to the test ratio to determine if it should be in the test set or not. This method ensures that the same identifier will always be in the same set, even if the data is shuffled or new data is added.
    Parameters:
    - identifier: the identifier to check
    - test_ratio: the proportion of the dataset to include in the test set
    Returns:
    - True if the identifier should be in the test set, False otherwise
    """
    return crc32(np.int64(identifier)) < test_ratio * 2**32


def split_data_with_id_hash(data, test_ratio, id_column):
    """
    This function splits the data into a training set and a test set based on the hash of an identifier column.
    It ensures that the same identifier will always be in the same set, even if the data is shuffled or new data is added.
    Parameters:
    - data: the dataset to split
    - test_ratio: the proportion of the dataset to include in the test set
    - id_column: the name of the column that contains the identifier
    Returns:
    - train_set: the training set
    - test_set: the test set
    """
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


def random_split_data(data, test_size=0.2, random_state=42):
    """
    This function splits the data into a training set and a test set randomly.
    It uses the train_test_split function from scikit-learn to perform the split.
    Parameters:
    - data: the dataset to split
    - test_size: the proportion of the dataset to include in the test set
    - random_state: controls the randomness of the split (optional)
    Returns:
    - train_set: the training set
    - test_set: the test set
    """
    return train_test_split(data, test_size=test_size, random_state=random_state)