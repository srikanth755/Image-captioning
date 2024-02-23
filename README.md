# Image-captioning
Image Captioning with visual Attention

First Download the dataset_flikr30k.json file from the link https://www.kaggle.com/datasets/shtvkumar/karpathy-splits?select=dataset_flickr30k.json.

Next Download the flikr30k dataset which consists of the images and the corresponding captions, from the kaggle at https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset, using opendatasets.

Now, Run the create_input_files.py which creates the train, validation and test data. Make sure to create empty folders naming output_folders and trained_models before hand, the input files created by create_input_files.py will get stored in the output_folders.

Here you can now run the train.ipynb each cell ensuring the correct paths in the notebook, and you will get your trained model saved in the best checkpoint path.
This will take long time if using the flikr30k dataset. You can also use the flikr8k dataset.

After training the model, you can now use the trained model for evaluation on the test data by running the eval.ipynb file and observe the performance of the model.

