# math-modeling
APEX Math Modeling Competetion

## cy
 - 直接全数据train不好评测是否过拟合，所以建议直接5 folder cross validation
 - 考虑10个症状每个0.1表示严重程度
 - http://www.jianshu.com/p/45968f4d5f86
- 基于学习模型的特征排序：
1.统计指标
precision/accuracy/f1
pearson/spearman
互信息和最大信息系数 Mutual information and maximal information coefficient (MIC)
距离相关系数 (Distance correlation)
2.分类模型
LogisticsRegression
SVM
决策树DecisionTree
随机森林RandomForest
3.回归模型
LinearRegression
Lasso（L1）/ Ridge（L2）
决策树DecisionTree
随机森林RandomForest
4.高级
递归特征消除 Recursive feature elimination (RFE)
5 folder cross validation
一二题都如此做

feature selection 之后是否要进行 combine modelling？
再跑个很高的综合模型出来
好像就是RFE

## cy
1.18日结果：
 - 对17日的结果中top16的位点联合训练（48维）LR的acc是0.707，
 - 尝试每次去掉一个留15个，求acc，降到0.68左右，有几个没下降，说明综合时没啥用

2.和蔡涵讨论结果：
 - 考虑直接用统计结果不用训LR
 - 第三题症状整体考虑 共享权值（卷积？RNN？双向RNN？创新点，但是数据量很少不一定行）

3.18号周日，基本代码都要写完
19号蔡全天课，晚上要把报告写完（latex，找个模板）
20号早上留着解决突发状况及改报告


## cy
1.17日结果：
 - 对全部位点训练的话3*9k>>1000肯定过拟合
 - 对每个位点单独做了onehot的3维feature，训了9k个逻辑回归，平均accuracy 0.515，最高0.583，调小l2的权重无变化。
表明，单个位点的影响性不是很明显
 - 对结果做了统计
 - 见图feature_score.png
 - 柱高分别为：2868/3936/1928/577/120/14/1/0/1
 - 看到少数（16）在0.55以上
 - 下一步考虑对这些点整合训练

2.和小明讨论的一些结果：
 - 其他分类器？我觉得这种线性分类器只能model某个维度单独的权重，二不能很好地model互相之间的关系
我们一致观点是还会存在一些feature间的and和or组合
 - 比如2维同时出现才产生的疾病，小明认为还是可以model的
-  - | +
- ————————
-  - | -
也能分开来
 - 然后在同一维上的or由于同一维永远只有一个是1，所以权重会体现在剩下那个上，所以也可以model
 - 但是不同维上的or关系感觉没法model出来，比如AorB，一半A，一半B的时候，A学出来0，B也是0
 - 从生物学上考虑感觉不太有不同维上or，所以可以先尝试忽略or
对16个的各种and组合进行model

3.考虑一些其他的指标
 - pearson相关系数（需要正态，貌似不合适）
 - spearman秩相关
 - pearson: -0.00175754845259（avg） 0.0222252143809（max）
 - spearman: -0.00175754799594 0.0222252157189
 - f1 score
 - cov 协方差

4.第一题是1对1，第二题是多对1，第三题是多对多
 - 第三题不是很理解，如何整体考虑10个病，0100010100这种怎么算
 - 本质是一个feature selection问题

ps:常用统计学习方法：参数检验、非参数检验、相关分析、回归分析、聚类分析、判别分析、主成份分析、因子分析、关联分析、决策树分析、贝叶斯、时间序列
