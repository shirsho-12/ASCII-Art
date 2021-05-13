import funcs
import argparse
from PIL import Image


def cli():
    desc_str = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=desc_str)

    parser.add_argument('--file', dest='img_file', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='out_file', required=False)
    parser.add_argument('--cols', dest='columns', required=False)
    parser.add_argument('--morelevels', dest='more_levels', action='store_true')
    parser.add_argument('--reverse', dest='reverse', action='store_true')
    parser.add_argument('--map', dest='map', required=False)

    return parser.parse_args()


if __name__ == '__main__':
    args = cli()
    img_file = args.img_file
    out_file = str(img_file) + '.txt'
    if args.out_file:
        out_file = args.out_file

    scale = 0.43
    if args.scale:
        scale = float(args.scale)

    columns = 80
    if args.columns:
        columns = int(args.columns)

    reverse = False
    if args.reverse:
        reverse = True

    if args.map:
        ascii_img = funcs.convert_to_ascii(img_file, columns, scale, args.more_levels, reverse, args.map)
    else:
        ascii_img = funcs.convert_to_ascii(img_file, columns, scale, args.more_levels, reverse)

    with open(out_file, 'w') as file:
        for row in ascii_img:
            file.write(row + '\n')

    print("ASCII art written to ", out_file)
