#!/bin/bash
#fasta
curl ftp://ftp.ncbi.nih.gov/genomes/Bacteria/Streptomyces_scabiei_87_22_uid46531/NC_013929.fna -o NC_013929.fasta
curl ftp://ftp.ncbi.nih.gov/genomes/Bacteria/Amycolatopsis_mediterranei_U32_uid50565/NC_014318.fna -o NC_014318.fasta
curl ftp://ftp.ncbi.nih.gov/genomes/Bacteria/Streptosporangium_roseum_DSM_43021_uid42521/NC_013595.fna -o NC_013595.fasta
curl ftp://ftp.ncbi.nih.gov/genomes/Bacteria/Catenulispora_acidiphila_DSM_44928_uid59077/NC_013131.fna -o NC_013131.fasta
curl ftp://ftp.ncbi.nih.gov/genomes/Bacteria/Sorangium_cellulosum__So_ce_56__uid61629/NC_010162.fna -o NC_010162.fasta

curl https://www.arabidopsis.org/download_files/Genes/TAIR8_genome_release/tair8.at.chromosomes.fas -o tair8.fasta
curl https://www.arabidopsis.org/download_files/Genes/TAIR9_genome_release/TAIR9_chr_all.fas -o tair9.fasta
curl https://www.arabidopsis.org/download_files/Genes/TAIR10_genome_release/TAIR10_chromosome_files/TAIR10_chr_all.fas -o tair10.fasta


