#!/usr/bin/env python3

from path import Path
import numpy as np
import scipy.io
import cv2
import glob
from tqdm import tqdm


def load_cmu_corridor_dataset(dataset_path='./dataset/cmu_corridor_dataset',
                              train_test_split=True,
                              image_size=(240, 320),
                              gray=False,
                              scaling=True,
                              verbose=False):
    """Load CMU Corridor Dataset as numpy array.

    Parameters
    ----------
    dataset_path : path to dataset folder
    train_test_split : decide whether split the dataset or not 
    image_size : (height, width) of image
    gray : decide whether read image as grayscale or not
    scaleing : decide whether scale data or not
    verbose : decide whether show debug info or not

    Returns
    -------
    images : ndarray
    labels : ndarray

    Or if split dataset 
    -------
    X_train : ndarray
    X_test : ndarray
    y_train : ndarray
    y_test : ndarray

    """
    dataset_path = Path(dataset_path)
    # Load images
    image_filenames = glob.glob(dataset_path / 'raw_image/*.png')
    image_filenames = sorted(image_filenames)
    images = np.empty((len(image_filenames), *image_size, 1 if gray else 3), dtype=np.float)
    for i, image_filename in enumerate(tqdm(image_filenames, total=len(image_filenames), desc="Loading images", disable=not verbose)):
        if gray:
            image = cv2.imread(image_filename, cv2.IMREAD_GRAYSCALE)
            image = np.expand_dims(image, -1)
        else:
            image = cv2.imread(image_filename, cv2.IMREAD_COLOR)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if scaling: image = image / 255.0 # Normalization
        images[i, ...] = image

    # Load labels
    label_filenames = glob.glob(dataset_path / 'ground_truth/*bw.png')
    label_filenames = sorted(label_filenames)
    labels = np.empty((len(label_filenames), *image_size, 1), dtype=np.float)
    for i, label_filename in enumerate(tqdm(label_filenames, total=len(label_filenames), desc="Loading labels", disable=not verbose)):
        label = cv2.imread(label_filename, cv2.IMREAD_GRAYSCALE)
        label = np.expand_dims(label, -1)
        if scaling: label = label / 255.0 # Normalization
        labels[i, ...] = label

    assert len(images) == len(labels)

    # If not split, return the whole dataset
    if not train_test_split: return images, labels

    # Load split mat
    split_mat = scipy.io.loadmat(dataset_path / 'train_test_split.mat')
    train_index = split_mat['train_index'].ravel()
    test_index = split_mat['test_index'].ravel()

    train_index, test_index = sorted(train_index), sorted(test_index)

    X_train, y_train = images[train_index], labels[train_index]
    X_test, y_test = images[test_index], labels[test_index]

    return X_train, X_test, y_train, y_test


if __name__ == '__main__':
    print("Running test unit...")

    X, y = load_cmu_corridor_dataset(dataset_path='./dataset/cmu_corridor_dataset',
                                     train_test_split=False,
                                     image_size=(240, 320),
                                     gray=False,
                                     verbose=True)
    assert X.shape[1:] == (240, 320, 3) and y.shape[1:] == (240, 320, 1)
    
    X_train, X_test, y_train, y_test = load_cmu_corridor_dataset(dataset_path='./dataset/cmu_corridor_dataset',
                                                                 train_test_split=True,
                                                                 image_size=(240, 320),
                                                                 gray=True,
                                                                 verbose=False)
    assert X_train.shape[1:] == (240, 320, 1) and y_train.shape[1:] == (240, 320, 1)
    assert X_test.shape[1:] == (240, 320, 1) and y_test.shape[1:] == (240, 320, 1)

    print("Congrats! All test passed!")