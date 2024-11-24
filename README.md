# Bone Fracture Classification Model 99%!

## Overview

This repository contains a high-performance machine learning model for classifying bone fractures in medical images. The model achieves an impressive 99% accuracy, making it a valuable tool for assisting medical professionals in diagnosing bone fractures quickly and accurately.

you can run the gui by running the model on your local machine and then running:

``` python gui.py ```

![image](https://github.com/user-attachments/assets/877abe98-03eb-45a1-ab8b-1638ba979701)


## Features

- High accuracy (99%) in classifying bone fractures
- includes model confidence percentages
- Fast inference time for real-time applications
- Supports multiple image formats (DICOM, JPEG, PNG)

## Model Architecture

The model uses a deep convolutional neural network, fine-tuned on a large dataset of bone X-ray images.

## Dataset

The model was trained on over a thousand images of different fractures consisting of 10 classes in total.
## Requirements

- Python 3.7+
- PyTorch 1.7+
- NumPy

## Installation

1. Clone this repository:
``` git clone https://github.com/cam-cc/bone-fracture-classification.git ```

2. Install the required packages:
``` pip install -r requirements.txt ```

3. The script will output the classification result and confidence score.

## Performance

- Accuracy: 99%
```
Test accuracy: 0.9941
Test loss: 0.0399
```
![image](https://github.com/user-attachments/assets/b13c71dd-a82b-42fb-942a-b36d07199084)

## Limitations

The model's performance may vary for pediatric patients or rare types of fractures not well-represented in the training data.

## Future Work

- Expand the dataset to include A LOT more images
- add more robust data augmentations

## Contributors

Cameron (myself)

## License

MIT
