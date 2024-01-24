# Devanagari-Character-Recognition
Devanagari Character Recognition Using Image Processing And Deep Learning

This work allows optical character recognition of the Devanagari script, handwritten or printed, written in a paragraph or a line. Image processing techniques enable word and character segmentation, i.e., splitting words from paragraphs and separating characters from a word. The segmented characters are then recognized using a convolutional neural network.

We have also used boosting technique over the neural network for achieving more significant outcomes. We trained five neural networks with different number and type of layers, filters and pool size in the convolutional layer, dropout rate and the number of neurons in the dense layer. Then, while performing recognition, each neural network is first used for prediction separately, and then voting among them is performed. The one which occurred more frequently is chosen as the final prediction, resulting in better precision.

Sample images used for character recognition can be found in the [Words] directory of the repository.

## Instructions To Use
To perform character recognition, accumulate the images in a directory and then provide the complete path to the directory in [Main.py].

## Model Performance

**Table 01.** Classification Report on Validation Data 

|  | accuracy_score | precision_score | recall_score | f1_score|
| --- | :---: | :---: | :---: | ---: |
| BestVal    |       0.9836    |       0.9838    |    0.9836  |  0.9836 |


**Table 02.** Classification Report on [Sample Images](https://github.com/milind-prajapat/Devanagari-Character-Recognition/tree/main/Words)

|  | accuracy_score | precision_score | recall_score | f1_score|
| BestVal      |     0.8095     |      0.9200    |    0.8095  |  0.8386


## Features
1. **Word segmentation** enables the character recognition of paragraphs, preserving the order of the words
2. **Character segmentation** enables the character recognition of a word
3. **Image processing** enables the segmentation of slanted words and characters, and *svar* having a *matra*
4. **Data augmentation** using image data generator class, rotated, shifted, sheared and zoomed
5. **Convolution neural network** helps in feature extraction

## Limitations
1. *vyanjans* having a *matra* cannot be segmented
2. Numerals and *matra* are not included in the dataset and hence can not be determined

## Dataset Used
* [Handwritten Devanagari Characters](https://drive.google.com/file/d/1kVn8-Cf1RnnePqfxpCnLSt1rxm2eSfh4/view?usp=sharing)
