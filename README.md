# Bone Fracture Classification Model

## Overview

This repository contains a high-performance machine learning model for classifying bone fractures in medical images. The model achieves an impressive 98% accuracy, making it a valuable tool for assisting medical professionals in diagnosing bone fractures quickly and accurately.

## Features

- High accuracy (98%) in classifying bone fractures
- Fast inference time for real-time applications
- Easy to integrate into existing medical imaging systems
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

- Accuracy: 98%

## Limitations

The model's performance may vary for pediatric patients or rare types of fractures not well-represented in the training data.

## Future Work

- Expand the model to classify more specific types of fractures
- Integrate the model into a user-friendly web application
- Conduct clinical trials to validate the model's performance in real-world settings

## Contributors

Cameron (myself)

## License

MIT
