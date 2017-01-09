#!/usr/bin/python

### NCBI NIH Hackathon
### parse PubTator to get a list of gene ids corresponing to each pubmed id
### author: felixfrancier@gmail.com

import pandas as pd
import re
import string

input_file = "test_file"



p_id_genes_dict = {}

with open (input_file, "r") as input_file:
    lines       =   input_file.readlines()
    for line in lines:
        if "Gene" in line:
            line = line.strip('\n')
            line = line.replace("(Tax:", '\t')
            line = re.split(r'\t+', line)
            print line

            p_id, gene = (line[0]), (line[5])
            print p_id, gene
            
            if p_id in p_id_genes_dict:
                p_id_genes_dict[p_id].append(gene)
            else:
                p_id_genes_dict[p_id] = [gene]

print p_id_genes_dict


