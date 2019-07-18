#!/usr/bin/env python3

import random
from matplotlib import pyplot as plt
import numpy as np

def plot_sample(X, y, preds, ix=None, prob=0.5, seed=None):
    """Function to plot the results"""
    if ix is None:
        random.seed(seed)
        ix = random.randint(0, len(X)-1)

    if y is not None:
        fig, ax = plt.subplots(1, 4, figsize=(20, 10))
    else:
        fig, ax = plt.subplots(1, 3, figsize=(20, 10))
        
    axis_index = 0
    if X[ix].shape[-1] == 1:
        ax[axis_index].imshow(X[ix, ..., 0], cmap='gray')
    else:
        ax[axis_index].imshow(X[ix])
    ax[axis_index].set_title('Raw Input')
    ax[axis_index].axis('off')
    axis_index += 1

    if y is not None:
        ax[axis_index].imshow(y[ix].squeeze(), cmap='gray')
        ax[axis_index].set_title('Ground Truth')
        ax[axis_index].axis('off')
        axis_index += 1
    
    ax[axis_index].imshow(preds[ix].squeeze(), cmap='gray')
    ax[axis_index].set_title('Predicted Probability Map')
    ax[axis_index].axis('off')
    axis_index += 1

    binary_preds = (preds > prob).astype(np.uint8)
    ax[axis_index].imshow(binary_preds[ix].squeeze(), cmap='gray')
    ax[axis_index].set_title('Predicted Binary Map (Prob > %.2f)' % (prob))
    ax[axis_index].axis('off')
    
def plot_samples(X, y, preds, indexs=None, num_samples=1, prob=0.5, seed=None):
    """Function to plot the results"""
    if indexs is None:
        random.seed(seed)
        indexs = [random.randint(0, len(X)-1) for _ in range(num_samples)]
    else:
        num_samples = len(indexs)
        
    if y is not None:
        fig, ax = plt.subplots(num_samples, 4, figsize=(20, 10))
    else:
        fig, ax = plt.subplots(num_samples, 3, figsize=(20, 10))
    plt.subplots_adjust(hspace=0.1, wspace=0.1)    
    
    for i, ix in enumerate(indexs):
        axis_index = 0
        if X[ix].shape[-1] == 1:
            ax[i, axis_index].imshow(X[ix, ..., 0], cmap='gray')
        else:
            ax[i, axis_index].imshow(X[ix])
        ax[i, axis_index].axis('off')
        if i == 0: ax[i, axis_index].set_title('Raw Input')
        axis_index += 1
        
        if y is not None:
            ax[i, axis_index].imshow(y[ix].squeeze(), cmap='gray')     
            ax[i, axis_index].axis('off')
            if i == 0: ax[i, axis_index].set_title('Ground Truth')
            axis_index += 1
        
        ax[i, axis_index].imshow(preds[ix].squeeze(), cmap='gray')     
        ax[i, axis_index].axis('off')
        if i == 0: ax[i, axis_index].set_title('Predicted Probability Map')
        axis_index += 1
        
        binary_preds = (preds > prob).astype(np.uint8)
        ax[i, axis_index].imshow(binary_preds[ix].squeeze(), cmap='gray')
        ax[i, axis_index].axis('off')        
        if i == 0: ax[i, axis_index].set_title('Predicted Binary Map (Prob > %.2f)' % (prob))