from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr30k',
                       karpathy_json_path=r'C:\Users\Admin\placements\Image Captioning with attention\dataset_flickr30k.json\dataset_flickr30k.json',
                       image_folder=r'C:\Users\Admin\placements\Image Captioning with attention\flickr30k\Images',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder=r'C:\Users\Admin\placements\Image Captioning with attention\output_folder',
                       max_len=50)