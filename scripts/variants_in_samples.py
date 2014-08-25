import json
import samples
import collections

conseq_per_sample = {}
for path in samples.json_list:
    sample = path.replace('../vep/','').replace('_list.json','')
    consequences =json.load( open(path, 'r'))
    
    for c in consequences:
        if c['id'] in conseq_per_sample:
            conseq_per_sample[c['id']].append(sample)
        else:
            conseq_per_sample[c['id']] = [sample, ]
        


cps = {}
for s in conseq_per_sample:
    cps[s]=len(conseq_per_sample[s])



for id in cps:
    print ",".join([str(id), str(cps[id]),";".join([str(n) for n in conseq_per_sample[id]])])
