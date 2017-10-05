import panda

expression_data = "./retrospective_breast_rna_seq_sort_common_gene_15115.txt"
grn_data = "./trrust_rawdata_geneSymbol_duplicateEliminated.human.txt"
ppi_data = "./ppi_biogrid.txt"
output_file = './result_breast_rna.tsv'

p = panda.Panda(expression_data, grn_data, ppi_data, remove_missing=False)
p.save_panda_results(file=output_file)

