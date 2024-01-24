# Devanagari-Character-Recognition
Devanagari Character Recognition Using Image Processing And Deep Learning

This work allows optical character recognition of the Devanagari script, handwritten or printed, written in a paragraph or a line. Image processing techniques enable word and character segmentation, i.e., splitting words from paragraphs and separating characters from a word. The segmented characters are then recognized using a convolutional neural network.

We have also used boosting technique over the neural network for achieving more significant outcomes. We trained five neural networks with different number and type of layers, filters and pool size in the convolutional layer, dropout rate and the number of neurons in the dense layer. Then, while performing recognition, each neural network is first used for prediction separately, and then voting among them is performed. The one which occurred more frequently is chosen as the final prediction, resulting in better precision.


