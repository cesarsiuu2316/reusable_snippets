from zlib import crc32
import numpy as np

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

