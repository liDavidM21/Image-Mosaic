
import sys
import argparse
import cv2 as cv



def parse_arguments(argv, prog=''):
    # Initialize the command-line parser
    parser = argparse.ArgumentParser(prog,
                                     description='Script for patch match.')

    #
    # Main input/output arguments
    #

    parser.add_argument('--source',
                        type=str,
                        help='Path to source image',
                        required=True)
    parser.add_argument('--radius',
                        type=int,
                        help='The radius of the image patch',
                        required=True)
    parser.add_argument('--output',
                        type=str,
                        help='Path to save the results',
                        default='output',
                        required=False)

    # Run the python argument-parsing routine, leaving any
    #  unrecognized arguments intact
    args, unprocessed_argv = parser.parse_known_args(argv)

    success = True
    msg = ''

    # return any arguments that were not recognized by the parser
    return success, args, unprocessed_argv, msg  #

def read_image(location):
    img = cv.imread(location, cv.IMREAD_COLOR)
    return img


def main(argv, prog=''):

    # Parse the command line arguments
    success, args, unprocessed_argv, msg = parse_arguments(argv, prog)

    source = read_image(args.source)
    radius = args.radius
    for i in range(0, source.shape[0], radius):
        for j in range(0, source.shape[1], radius):
            #check for boundary case
            end_row = i+radius
            end_col = j+radius
            if(end_row >= source.shape[0]):
                end_row = source.shape[0]-1
            if(end_col >= source.shape[1]):
                end_col = source.shape[1]-1
            sum_r = 0
            sum_g = 0
            sum_b = 0
            for a in range(i, end_row):
                for b in range(j, end_col):
                    sum_r += source[a][b][0]
                    sum_g += source[a][b][1]
                    sum_b += source[a][b][2]
            sum_r /= radius*radius
            sum_g /= radius*radius
            sum_b /= radius*radius
            for a in range(i, end_row):
                for b in range(j, end_col):
                    source[a][b] = [sum_r, sum_g, sum_b]

    cv.imwrite(args.output, source)




# Include these lines so we can run the script from the command line
if __name__ == '__main__':
    main(sys.argv[1:], sys.argv[0])
