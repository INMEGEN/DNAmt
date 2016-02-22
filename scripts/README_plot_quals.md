To get the old behavior, you could use find:

    find /home/rgarcia/mt/DNAmt/coverage_et_qual/ -name 'mapping_quality_across_reference.txt' -exec python2 plot_quals.py {} +