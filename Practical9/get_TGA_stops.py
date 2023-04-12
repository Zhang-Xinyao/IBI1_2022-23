import re
gene_name_pattern=re.compile(r'>(\S+)')
stop_codon_pattern=re.compile(r'TGA$')
#define the pattern that give the conditions that can be matched
new_gene_name=''
new_gene=''
#define the string that would be wirtten into the output file
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as ip,open('TGA_genes.fa','w') as op:
    for line in ip:
        if line.startswith('>'):
            new_gene_name=gene_name_pattern.search(line).group()
            new_gene=''
            #for the line starting with ">", get the string matching with gene_name_pattern 
        else:
            new_gene+=line.strip()
            #combine the DNA sequence together without putting the bases in different lines
            if stop_codon_pattern.search(new_gene):
                op.write('{}\n{}\n\n'.format(new_gene_name,new_gene))
                #only write the DNA sequences that end with "TGA" and the gene name into the file
