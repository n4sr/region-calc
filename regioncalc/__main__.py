import argparse
import re
from math import floor as f
from sys import argv


def run():
    args = parser.parse_args(argv[1:])
    if args.coords:
        print(get_output(args.coords, 'coords', avg=args.avg))
    elif args.region:
        print(get_output(args.region, 'region', avg=args.avg))
    elif args.file:
        for file in args.file:
            print(get_output(file, 'file', avg=args.avg))
    else:
        parser.print_usage()

def get_output(i, fmt, avg=False):
    if fmt == 'coords':
        region = region_from_coords(i)
        coords = coords_from_region(region)
        file = filename_from_region(region)
    elif fmt == 'file':
        region = region_from_filename(i)
        coords = coords_from_region(region)
        file = filename_from_region(region)
    elif fmt == 'region':
        coords = coords_from_region(i)
        region = region_from_coords(coords)
        file = filename_from_region(region)
    else:
        raise ValueError(fmt)
    pos1 = coords[0:2]
    pos2 = coords[2:4]
    if avg:
        return f'{file}\t{average_coords(pos1, pos2)}'
    else:
        return f'{file}\t{pos1} to {pos2}'

def average_coords(a, b):
    return f((a[0]+b[0])/2), f((a[1]+b[1])/2)

def region_from_coords(p):
    return f(p[0]/512), f(p[1]/512)

def coords_from_region(p):
    x = f(p[0])*512
    z = f(p[1])*512
    return x, z, x+511, z+511

def region_from_filename(s):
    pattern = re.compile(r'r\.(\-?\d+)\.(\-?\d+)\.mca')
    result = pattern.match(s)
    return int(result.group(1)), int(result.group(2))

def filename_from_region(p):
    return f'r.{p[0]}.{p[1]}.mca'


parser = argparse.ArgumentParser(prog='regioncalc')
parser.add_argument(
    '-a',
    action='store_true',
    dest='avg',
    help='average coords, prints center coords of region'
)
arggroup = parser.add_mutually_exclusive_group()
arggroup.add_argument(
    '-f',
    nargs='+',
    type=str,
    dest='file',
    help='input as filename'
)
arggroup.add_argument(
    '-r',
    nargs=2,
    type=int,
    dest='region',
    help='input as region'
)
arggroup.add_argument(
    '-c',
    nargs=2,
    type=int,
    dest='coords',
    help='input as pair of coords: x z'
)

if __name__ == '__main__':
    run()