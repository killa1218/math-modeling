import cPickle as pickle
import tensorflow as tf


seeds = [0x0123, 0x4567, 0x3210, 0x7654, 0x89AB, 0xCDEF, 0xBA98, 0xFEDC,
			0x0246, 0x1357, 0x6420, 0x7531, 0x8ACE, 0x9BDF, 0xECA8, 0xFDB9,
		 	0x0369, 0x147A, 0x9630, 0xA741, 0x258B, 0x369C, 0xB852, 0xC963]


def init_var_map(init_path, _vars):
	if init_path:
		var_map = pickle.load(open(init_path, "rb"))
	else:
		var_map = {}

	for i in range(len(_vars)):
		key, shape, init_method, init_argv = _vars[i]
		if key not in var_map.keys():
			if init_method == "normal":
				mean, dev, seed = init_argv
				var_map[key] = tf.random_normal(shape, mean, dev, seed=seed)
			elif init_method == "uniform":
				min_val, max_val, seed = init_argv
				var_map[key] = tf.random_uniform(shape, min_val, max_val, seed=seed)
			else:
				var_map[key] = tf.zeros(shape)

	return var_map


def regression_lr(x_id, W_lr):
	theta_gather_weights = tf.gather(W_lr, x_id)
	theta_regression = tf.reduce_sum(theta_gather_weights, 1, keep_dims=True)
	return theta_regression


def build_optimizer(opt_argv, loss):
	opt_method = opt_argv[0]
	if opt_method == 'adam':
		_learning_rate, _epsilon = opt_argv[1:3]
		opt = tf.train.AdamOptimizer(learning_rate=_learning_rate, epsilon=_epsilon).minimize(loss)
	elif opt_method == 'ftrl':
		_learning_rate = opt_argv[1]
		opt = tf.train.FtrlOptimizer(learning_rate=_learning_rate).minimize(loss)
	else:
		_learning_rate = opt_argv[1]
		opt = tf.train.GradientDescentOptimizer(learning_rate=_learning_rate).minimize(loss)
	return opt


def str_list2float_list(str_list):
	res = []
	for _str in str_list:
		res.append(float(_str))
	return res