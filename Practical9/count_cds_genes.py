input="TAA"
#input the stop codon, here use "TAA" as an example
import re
gene_name_pattern=re.compile(r'>(\S+)')
#define the pattern that give the conditions that can be matched
new_gene_name=''
new_gene=''
#define the string that would be wirtten into the output file
count1=0
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as ip,open ('{}_stop_gene.fa'.format(input),'w') as op:
    for line in ip:
        if line.startswith('>'):
            new_gene_name=gene_name_pattern.search(line).group()
            new_gene=''
            #for the line starting with ">", get the string matching with gene_name_pattern
        else:
            new_gene+=line.strip()
            #combine the DNA sequence together without putting the bases in different lines for line in op
            if re.compile(r'{}$'.format(input)).search(new_gene):
                #find sequence end with given stop codon and extract these lines and count the coding sequence in this sequence 
                count1=len(re.findall(r'{}'.format(input),new_gene))
                op.write('{}\n{}\n{}\n'.format(new_gene_name,new_gene,count1))
