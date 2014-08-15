import vcf
import pprint

import numpy as np
import matplotlib
matplotlib.use('agg')
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

column_labels = keys
row_labels = keys
data = np.array( rows )

fig, ax = plt.subplots()

heatmap = ax.pcolor(data, cmap='summer', picker=True)


# Format
fig = plt.gcf()
fig.set_size_inches(16, 13)

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(row_labels, minor=False, fontsize=8)
ax.set_yticklabels(column_labels, minor=False, fontsize=8)
# plt.show()

plt.xticks(rotation=90)

plt.colorbar(heatmap, orientation="vertical")

plt.savefig('heatmap.png')



# pprint.pprint(sets)
# print "solid i ion",len(set(key_solid).intersection(set(key_ion)))
# print "solid i complete",len(set(key_solid).intersection(set(key_complete)))
# print "ion i complete",len(set(key_complete).intersection(set(key_ion)))
