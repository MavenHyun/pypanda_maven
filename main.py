import panda

expression_data = "data/GeneExpression/retrospective_breast_rna_seq_sort_common_gene_15115.txt"
grn_data = "data/GeneRegulatoryNetwork/TRRUST/trrust_rawdata_geneSymbol.human.txt"
ppi_data = "data/PPI/ppi_biogrid.txt"
output_file = 'C:/Users/Arthur Keonwoo Kim/Desktop/PyPanda/output/result_breast_rna.tsv'

p = panda.Panda(expression_data, grn_data, ppi_data, remove_missing=False)
p.save_panda_results(file=output_file)

