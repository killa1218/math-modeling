import numpy as np

class DataLoader():
	def __init__(self, folder='../data/'):
		self._folder = folder
		print 'Init DataLoader Done.'

	def load_genotype(self):
		with open(self._folder + 'genotype.dat', 'r') as infile:
			lines = infile.readlines()
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

if __name__=='__main__':
	print 'Testing DataLoader...'
	data_loader = DataLoader()
	
	genotype, genotable = data_loader.load_genotype() 
	print 'genotype:\n', '\tshape:', len(genotype), 'sample:', genotype[0]
	print 'genotable:\n', '\tshape:', len(genotable), len(genotable[0]), 'sample:', genotable[0][0]

	phenotype = data_loader.load_phenotype()
	print 'phenotype:\n', '\tshape:', phenotype.shape, 'sample:', phenotype[0]

	multi_phenos = data_loader.load_multi_phenos()
	print 'multi_phenos:\n', '\tshape:', multi_phenos.shape, 'sample:', multi_phenos[0]

	gene_info = data_loader.load_gene_info()
	print 'gene_info:\n', '\tshape:', len(gene_info), 'sample:', gene_info[0]