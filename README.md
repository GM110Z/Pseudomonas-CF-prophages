**Padloc-output-parser.py** Parses padloc output to replace seqid with the filename that also includes the prophages coordinates

**download-seqs.sh** Download sequences from Pseudomonas.com database. Needs a list of genome-urls extracted from the table that can be downloaded from Pseudomonas.com

**PARSEC.sh** Uses PhiSpy.py to predict prophages, then groups them by ANICluster
Dependencies: \
1)fastANI and ANIClustermap(https://github.com/moshi4/ANIclustermap/tree/main) \
2)fastani-to-clusters.py -- arguments are Threshold ID, ANICluster matrix, filename of output \

**padloc-output-parser.py** Process the padloc output that was run on prophages to specify which region of the seqid was considered (and then extracts it to use it further)
