"""
Main Module

This is the main module to be used when we want to call the compression algorithm LZ78
to a certain file. This is a CLI code.
"""

from lz78 import LZ78
from argparse import ArgumentParser

# Creating argument parser to handle automatically with the arguments of entry.
parser = ArgumentParser(description='Compression and Descompression LZ78 algorithm with Python')

# Defining each argument
group = parser.add_mutually_exclusive_group(required=True)
# Compression argument
group.add_argument(
    '-c', '--c',
    type=str,
    default=None,
    action='store',
    metavar='',
    help='The Input file path parameter to be compressed.'
)
# Descompression argument
group.add_argument(
    '-x', '--x',
    type=str,
    default=None,
    action='store',
    metavar='',
    help='The Input file path parameter to be descompressed.'
)
# Output argument
parser.add_argument(
    '-o', '--o',
    type=str,
    default=None,
    required=False,
    metavar='',
    help='This should be the output file path, but it is optional.'
)

if __name__ == '__main__':
    # constants to be used on the program
    default_base:int = 36 # default base of numerical encoding
    lz_extension:str = '.lz78' # default extension to output compression
    txt_extension:str = '.txt' # default extension to output descompression

    # Algorithm Instanciation
    lz_alg:LZ78 = LZ78()

    # reading arguments.
    args = parser.parse_args()
    # print(args)

    if args.c:
        # Compression Case
        output_file:str = ''
        if args.o:
            # Using output file path when it is parsed.
            output_file = args.o
        else:
            dot_position:int = args.c[::-1].find('.')
            if dot_position > -1:
                output_file= args.c[:-(dot_position+1)]+ lz_extension
            else:
                output_file= args.c+ lz_extension
        lz_alg.encode(input_file_path=args.c, output_file_path=output_file, base=default_base)

    elif args.x:
        # Descompression Case
        output_file:str = ''
        if args.o:
            # Using output file path when it is parsed.
            output_file = args.o
        else:
            dot_position:int = args.x[::-1].find('.')
            if dot_position > -1:
                output_file= args.x[:-(dot_position+1)]+ txt_extension
            else:
                output_file= args.x+ txt_extension
        lz_alg.decode(input_file_path=args.x, output_file_path=output_file, base=default_base)
