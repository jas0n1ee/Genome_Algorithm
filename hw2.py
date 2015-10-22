import tools
from kmer_index import Index
genome = tools.readGenome('chr1.GRCh38.excerpt.fasta')
t_ind = Index(genome, 8)
