import numpy as np
import cPickle
from load_data import DataLoader
from sklearn.linear_model import LogisticRegression
from scipy.stats import pearsonr, spearmanr


data_loader = DataLoader()

genotype, genotable = data_loader.load_genotype() 
phenotype = data_loader.load_phenotype()
feature_shape = len(genotype)
sample_size = len(phenotype)

#locus importance
feature_score = []
feature_param = []
for feature_idx in range(feature_shape):
	#get code ref
	sample_code = []
	for sample_idx in range(sample_size):
		sample_code.append(genotable[sample_idx][feature_idx])
	code_ref = set(sample_code)
	code2idx = {}
	for code in code_ref:
		code2idx[code] = len(code2idx)
	
	#feature
	sample_feature = np.zeros((sample_size, len(code_ref)), dtype = np.float32)
	for sample_idx, code in enumerate(sample_code):
		sample_feature[sample_idx][code2idx[code]] = 1.

	#statistic
	pearson = []
	spearman = []
	for i in range(len(code_ref)):
		pr, pp = pearsonr(sample_feature[:, i], phenotype)
		pearson.append(pr)
		sr, sp = spearmanr(sample_feature[:, i], phenotype)
		spearman.append(sr)

	'''#modelling
	LR_model = LogisticRegression(penalty = 'l2', C = 1.0)
	LR_model.fit(sample_feature, phenotype)
	feature_score.append(LR_model.score(sample_feature, phenotype))
	feature_param.append((LR_model.coef_, LR_model.intercept_))
	print feature_idx, genotype[feature_idx]
	print '\tAccuracy:', feature_score[-1]
	print '\tParam:', feature_param[-1]
	'''
	#raw_input('pause')

#print 'Avg Accuracy:', np.mean(feature_score)
#print 'Top Accuracy:', np.max(feature_score)

print 'pearson:', np.mean(pearson), np.max(pearson)
print 'spearman:', np.mean(spearman), np.max(spearman)
#save
#with open('one_locus_modelling.result', 'w') as outfile:
#	cPickle.dump((feature_score, feature_param), outfile)


