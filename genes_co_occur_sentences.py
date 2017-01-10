#!/usr/bin/python

### NCBI NIH Hackathon
### quantify co-occurence of gene pairs in abstract sentences for hypergeom calculations
### author: felixfrancier@gmail.com

#import pandas as pd
import re
#import string

input_file = "test_file"



min_pid = 100
#max_pid = 100149
max_pid = 100027



### Abstract dictionary
abstract_dictionary = {}

with open (input_file, "r") as input_file1:
    lines       =   input_file1.readlines()
    for line in lines:
        line = line.strip('\n')
        if "|a|" in line and line[-3:] != "|a|":
            line = line.split('|a|')
            #abstract = line[1].split(". ")
            abstract = line[1]
            pid = line[0]
            if int(pid)>=min_pid and int(pid)<=max_pid:
                abstract_dictionary[pid] = abstract

#print abstract_dictionary


### Genes dictionary and list
#pid_genes_dict = {}
genes_list = []
with open (input_file, "r") as input_file2:
    lines       =   input_file2.readlines()
    for line in lines:
        if "Gene" in line and ("|a|" or "|t|") not in line :
            line = line.strip('\n')
            line = line.replace("(Tax:", '\t')
            line = re.split(r'\t+', line)
            #p_id, gene = (line[0]), (line[5])
            p_id, gene = (line[0]), (line[3])
            if int(p_id)>=min_pid and int(p_id)<=max_pid:
                genes_list.append(gene)
                #if p_id in pid_genes_dict:
                #    pid_genes_dict[p_id].append(gene)
                #else:
                #    pid_genes_dict[p_id] = [gene]

genes_list = list(set(genes_list))
#print pid_genes_dict
#print genes_list


### Get gene pairs
gene_pairs = []
for i in xrange(len(genes_list)-1):
    for j in xrange(len(genes_list)-(i+1)):
        #print genes_list[i], genes_list[i+j+1]
        gene_pairs.append([genes_list[i], genes_list[i+j+1]])
#print gene_pairs


### individual gene count & gene pair count
individual_gene_count = {}
for gene in genes_list:
    individual_gene_count[gene] = 0
    
gene_pair_count = {}
for gene_pair in gene_pairs:
    gene_pair_count[gene_pair[0] +"_" + gene_pair[1]] = 0
    
for p_id, abstract in abstract_dictionary.iteritems():
    for gene in genes_list:
        if gene in abstract:
            individual_gene_count[gene] = individual_gene_count[gene]+1
    for gene_pair in gene_pairs:
        if (gene_pair[0] in abstract) and (gene_pair[1] in abstract):
            gene_pair_count[gene_pair[0] +"_" + gene_pair[1]] = gene_pair_count[gene_pair[0] +"_" + gene_pair[1]] + 1

#print gene_pair_count

print individual_gene_count  


for gene_pair, value in gene_pair_count.iteritems():
    geneA, geneB = gene_pair.split('_')[0], gene_pair.split('_')[1]
    print geneA, individual_gene_count[geneA], geneB, individual_gene_count[geneB]


'''
### Abstract lines dictionary
abstract_dictionary = {}
with open (input_file, "r") as input_file1:
    lines       =   input_file1.readlines()
    for line in lines:
        line = line.strip('\n')
        if "|a|" in line and line[-3:] != "|a|":
            line = line.split('|a|')
            abstract = line[1].split(". ")
            pid = line[0]
            abstract_dictionary[pid] = abstract
print abstract_dictionary
'''

'''
### Gene pair dictionary
pid_genes_dict = {}
with open (input_file, "r") as input_file2:
    lines       =   input_file2.readlines()
    for line in lines:
        if "Gene" in line and ("|a|" or "|t|") not in line :
            line = line.strip('\n')
            line = line.replace("(Tax:", '\t')
            line = re.split(r'\t+', line)
            #p_id, gene = (line[0]), (line[5])
            p_id, gene = (line[0]), (line[3])
            if p_id in pid_genes_dict:
                pid_genes_dict[p_id].append(gene)
            else:
                pid_genes_dict[p_id] = [gene]

print pid_genes_dict
'''

'''
### Remove pid_genes_dict with one genes
list_keys_remove = []
for key, value in pid_genes_dict.iteritems():
    #print key, len(value)
    if len(value) <2:
        list_keys_remove.append(key)
        #del pid_genes_dict[key]
#print list_keys_remove
for key in list_keys_remove:
    del pid_genes_dict[key]
print pid_genes_dict
'''


'''
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
'''



