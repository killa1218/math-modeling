import numpy as np

class DataLoader():
	def __init__(self, folder='data/'):
		self._folder = folder
		print 'Init DataLoader.'

	def load_genotype(self):
		with open('data/genotype.dat', 'r') as infile:
			lines = f.readlines()
		genotype = lines[0].split()
		genotable = []
		for line in lines[1:]:
			genotable.append(line.split())
		return (genotype, genotable)

	def load_phenotype(self):
		return np.loadtxt(self._folder + 'phenotype.txt')
	
	def load_multi_phenos(self):
		return np.loadtxt(self._folder + 'multi_phenos.txt')

	def load_gene_info(self):
		gene_info = []
		for i in range(1,301):
			with open(self._folder + 'gene_info/gene_%d.dat'%i, 'r') as infile:
				gene_info.append(infile.read().split())
		return gene_info

