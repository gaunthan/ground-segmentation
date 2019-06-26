# ground-segmentation
Learning a deep neural network for ground segmentation.

## Usage
### Clone project and install dependencies

```
git clone https://github.com/gaunthan/ground-segmentation.git
cd ground-segmentation
pip install -r requirements.txt
```

### Download dataset
Run `get_dataset.py` to download the dataset. We use cmu-corridor-dataset to train the model.

### Launch JupyterLab
Under ground-segmentation, run the following command to launch JupyterLab

```
jupyter-lab .
```

Model definition, training and inference are written in notebook **ground_segmentation.ipynb**.

you can open it in JupyterLab. 

## Evaluate The Model

![](./screenshot/learning-curve.png)

![](./screenshot/predictions-on-training-set.png)

![](./screenshot/predictions-on-test-set.png)
