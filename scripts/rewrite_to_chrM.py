import vcf

import samples


for path in samples.file_list:
    variants  = vcf.Reader( open( path, 'r' ), compressed=True)
    path_chrM = path.replace('.vcf.gz', '_chrM.vcf.gz')
    vars_out  = vcf.Writer( open( path_chrM, 'w' ), variants)
    for v in variants:
        v.CHROM = 'MT'
        vars_out.write_record(v)
    vars_out.close()

