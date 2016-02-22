#!/usr/bin/python2
# coding: utf-8
"""
This script is used to plot the mapping_quality_across_reference obtained from
qualimap, (i.e. `qualimap bamqc -bam sorted.bam -outdir dir`).

"""
import argparse
from matplotlib import pyplot as plt


def parse():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-o', '--output', default='', help='Name for the output graph.')
    parser.add_argument('files', nargs='+', help='Path to `mapping_quality_across_reference.txt` files.')
    return parser.parse_args()

def plot_quals(filenames):
    quals = {}
    bins = []
    for path in filenames:
        quals[path] = []
        with open(path, 'r') as f:
            for l in f.readlines():
                if not l.startswith('#'):
                    (bin, qual) = l.split()
                    quals[path].append(qual)
                    if not bin in bins:
                        bins.append(bin)

    for q in quals:
        plt.plot(bins,quals[q], '-')
    plt.show()

if __name__ == "__main__":
    args = parse()
    plot_quals(args.files)
