# InceptionV3 Bone Fracture Detection
This repository contains a convolutional neural network (CNN) model using InceptionV3 for classifying bone X-ray images as fractured or not fractured.

# Installation
To use this notebook, please follow these steps:

Download the dataset from [Here](https://www.kaggle.com/datasets/vuppalaadithyasairam/bone-fracture-detection-using-xrays).

Extract the contents of the downloaded file to the root directory of this project.

Create two new directories in the root directory: fractured and not fractured. You can do this by running the following command:

```bash
Copy code
mkdir -p ./dataset/{fractured,"not fractured"}
```
Move the fractured and not fractured images to their respective directories using the following commands:
```bash
mv ./dataset/{val,train}/"not fractured"/*.jpg ./dataset/"not fractured"/
mv ./dataset/{val,train}/fractured/*.jpg ./dataset/fractured/
```
Remove the train and val directories along with their contents using the following command:
```bash
rm -rf dataset/train && rm -rf dataset/val
```
Split the folders into Train / Test / Validation sets (currently 80/10/10)
```
python3 split-folders.py
```
Finally, run the ipynb notebook to train and evaluate the model.

Note: You will need to have Jupyter Notebook installed to run the .ipynb file.

Credits
The dataset used in this project was obtained from Kaggle (insert Kaggle dataset link here). The InceptionV3 model used for this project was pre-trained on the ImageNet dataset, and the implementation of the CNN was inspired by various online tutorials and resources.
