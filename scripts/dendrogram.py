import vcf

from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
import numpy as np
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt

import samples

# computes jacard index for two or mor sets
def jaccard_index(first, *others):
        return float( len( first.intersection(*others))) / float(len(first.union(*others)))


sets = {}

for path in samples.file_list:
    variants = vcf.Reader( open( path, 'r' ), compressed=True)

    sample   = path.replace('.vcf.gz', '')
    sets[sample] = []
    for v in variants:
        if v.is_snp:
            sets[sample].append((v.CHROM, 
                                 v.POS,
                                 str(v.alleles[0]),
                                 str(v.alleles[1])))

    sets[sample] = set(sets[sample])




# count intersections, place them in a table (rows are lists of cols)
keys = sorted(sets.keys())
rows = []
for i in keys:
    col = []
    for j in keys:
        if i==j:
            inter = 1
        else:
            inter = jaccard_index(sets[i], sets[j])
        col.append(inter)
    rows.append(col)


rows = np.array( rows )

# plot dendrograms
fig = plt.figure(figsize=(15,15))


fig.add_subplot()
linkage_matrix = linkage(rows,
                         "centroid")

a = dendrogram(linkage_matrix,
               color_threshold=1,
               labels=keys,
               show_leaf_counts=False,
               leaf_font_size=7,
               leaf_rotation=-90.0,
               orientation='top',
         )
plt.savefig('dendrogram_centroid.svg')
