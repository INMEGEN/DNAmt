import samples

for code in samples.ethnicity:
    try:
        lines = open( "vep/%s.tsv" % code, 'r').readlines()
    except IOError:
        lines = []

    for l in lines:
        if not l.startswith('#'):
            fields = l.split()
            fields.append(code)
            fields.append(samples.ethnicity[code])
            print "\t".join(fields)
