#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import argparse
import os
import random 
import string
import sys
import uuid

# GLOBALS
FOREST_GREEN = (64, 107, 76)
SEA_BLUE = (0, 87, 128)
DARK_INDIGO = (0, 3, 82)
PINK = (191, 0, 255)
LIGHT_GREEN = (72, 189, 0)
ORANGE = (189, 107, 0)
RED = (189, 41, 0)
DARK_BLUE = (0, 3, 82)
POINT_COLORS = ['black', 'red', 'blue', 'green', FOREST_GREEN, SEA_BLUE, DARK_BLUE]
LINE_POINT_COLORS = [FOREST_GREEN, SEA_BLUE, DARK_INDIGO, PINK, LIGHT_GREEN, ORANGE, RED]

IMAGE_WIDTH = 100
IMAGE_LENGTH = 100

FONT_NAME = ''
DESTINATION_DIRECTORY = 'datasets/vgg-16-data/'

FONTS = [r'fonts/DejaVuSans.ttf',
         r'fonts/DejaVuSerif.ttf',
         r'fonts/OpenSans-Bold.ttf',
         r'fonts/OpenSans-Light.ttf',
         r'fonts/System San Francisco Display Regular.ttf',
         r'fonts/MesloLGS-NF-Italic.ttf'
        ]

# Get two random locations on the CAPTCHA image
get_image_location = lambda : (random.randrange(0, IMAGE_WIDTH),
                               random.randrange(0, IMAGE_LENGTH))

# Get a random font
get_font = lambda : (random.choice(FONTS)) 




def main():

    print('Saving to: ' + DESTINATION_DIRECTORY)
    os.makedirs(DESTINATION_DIRECTORY, exist_ok=True)
    print('Generating CAPTCHA images')

    i = 0
    while (i < 10000):
        generate_numeric_captcha_image(i)
        i += 1




def parse_commandline_argument():
    """ 
        Parse the arguments from the command-line.

        If no arguments are passed, the help screen will
        be shown and the program will be terminated.

    Returns:
        the parser with the command-line argument
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--font', nargs=1, required=True, 
                        help='The font file with extension ".ttf" to use \
                              (example: "DejaVuSansMono.ttf")')
    
    # if no arguments were passed, show the help screen
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()




def generate_numeric_captcha_image(number):
    # create a colored image with white background
    captcha_image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_LENGTH), color="white")
    illustrator = ImageDraw.Draw(captcha_image)

    # generate the colored number
    captcha_text = str(number)
    captcha_text = captcha_text.zfill(4)
    get_colored_text(illustrator, captcha_text)

    # draw some random lines
    for _ in range(5,random.randrange(6, 10)):
        illustrator.line((get_image_location(), get_image_location()), fill=random.choice(LINE_POINT_COLORS), width=random.randrange(1,3))

    # draw some random points
    for _ in range(10,random.randrange(11, 20)):
        illustrator.point((get_image_location(), get_image_location(), get_image_location(), get_image_location(), 
                           get_image_location(), get_image_location(), get_image_location(), 
                           get_image_location(), get_image_location(), get_image_location()), 
                           fill=random.choice(POINT_COLORS))

    # save the newly generate CAPTCHA image
    captcha_image.save(DESTINATION_DIRECTORY + '/' + captcha_text + '_' +
                       str(uuid.uuid4()) + '.png')




def generate_captcha_image():
    
    # create a colored image with white background
    captcha_image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_LENGTH), color="white")
    illustrator = ImageDraw.Draw(captcha_image)

    # generate a randomly colored string
    captcha_string = generate_random_string(4, 'numeric')
    get_colored_text(illustrator, captcha_string)

    # draw some random lines
    for _ in range(5,random.randrange(6, 10)):
        illustrator.line((get_image_location(), get_image_location()), fill=random.choice(LINE_POINT_COLORS), width=random.randrange(1,3))

    # draw some random points
    for _ in range(10,random.randrange(11, 20)):
        illustrator.point((get_image_location(), get_image_location(), get_image_location(), get_image_location(), 
                           get_image_location(), get_image_location(), get_image_location(), 
                           get_image_location(), get_image_location(), get_image_location()), 
                           fill=random.choice(POINT_COLORS))

    # save the newly generate CAPTCHA image
    captcha_image.save(DESTINATION_DIRECTORY + '/' + str(captcha_string) + '_' +
                       str(uuid.uuid4()) + '.png')




def generate_random_string(captcha_length: int, character_set: str) -> str:

    captcha_string = None

    if character_set == 'alphanumeric':
        captcha_string += (string.ascii_lowercase + string.ascii_uppercase)
    elif character_set == 'alphabet':
        captcha_string += (string.ascii_lowercase + string.ascii_uppercase)
    else:
        captcha_string = string.digits

    generate_random_string = ''.join(random.choices(captcha_string, k=captcha_length))
    return generate_random_string




def get_colored_text(illustrator, captcha_string):
    x_position = IMAGE_WIDTH / 6
    y_position = IMAGE_LENGTH / 3
    font_size = int(IMAGE_LENGTH * 0.3)

    for i in range(len(captcha_string)):
        text_color = random.choice(POINT_COLORS)
        character = captcha_string[i]
        font = ImageFont.truetype(get_font(), font_size)
        illustrator.text((x_position, y_position), character, fill=text_color, font=font)
        x_position = x_position + (IMAGE_WIDTH / 5)




main()
