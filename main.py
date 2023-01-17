import os
import cv2
import argparse
import time


def copy_files(input_folder, output_folder):
    """Copy files from input folder to output folder"""
    for file in os.listdir(input_folder):
        input_file = os.path.join(input_folder, file)
        output_file = os.path.join(output_folder, file)
        # copy input file to output file
        with open(input_file, 'rb') as f:
            data = f.read()
        with open(output_file, 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    # argument parser that takes in an image and an output directory
    parser = argparse.ArgumentParser(
        description='Copy files from input folder to output folder')
    parser.add_argument('image_dir', type=str, help='Path to input directory')
    parser.add_argument('output_dir', type=str,
                        help='Path to output directory')
    args = parser.parse_args()

    copy_files(args.image_dir, args.output_dir)
