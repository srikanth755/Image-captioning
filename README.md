# Image-Captioning with visual Attention.

The model addresses the task of automatically generating captions for images by attending to different regions of the image while generating each word of the caption.

Resnet model is used for encoding the images.

LSTM cells with attention are used as decoder for generating the caption of the image.

# Model
![Image-Captioning with visual Attention model.](https://github.com/srikanth755/Image-captioning/blob/main/model.png?raw=true)

# Requirements needed
The code was ran at RTX 3090 GPU and the using the python==3.9.18.  
Install the requirements.txt before hand using (python -r requirements.txt) in the command prompt.

# Image-captioning
First Download the dataset_flikr30k.json/flickr8k.json file from the link https://www.kaggle.com/datasets/shtvkumar/karpathy-splits?select=dataset_flickr30k.json.

Next Download the flikr30k/flickr8k dataset which consists of the images and the corresponding captions, from the kaggle at https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset, using opendatasets.

Now, Run the create_input_files.py which creates the train, validation and test data. Make sure to create empty folders naming output_folders and trained_models before hand, the input files created by create_input_files.py will get stored in the output_folders.

Here you can now run the train.ipynb each cell ensuring the correct paths in the notebook, and you will get your trained model saved in the best checkpoint path. This will take long time if using the flikr30k dataset. You can also use the flikr8k dataset.

After training the model, you can now use the trained model for evaluation on the test data by running the eval.ipynb file and observe the performance of the model.

And also the attention weights (alphas) can be visualized using the file test_single_img_no_beam_search.ipynb.

To know the performance of the model here the BLEU2 score is used and it is 0.45 on the test set.

