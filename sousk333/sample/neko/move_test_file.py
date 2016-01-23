import sys
from random import sample
from shutil import move
from glob import glob


def main():
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    sample_num = int(sys.argv[3])

    image_list = glob('%s/*.png' % input_dir)
    for file in sample(image_list, sample_num):
        move(file, output_dir)


if __name__ == "__main__":
    main()
