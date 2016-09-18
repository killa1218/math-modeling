# -*- coding: utf-8 -*-
# 单位点与疾病关系统计: F1 Score 计算
#   某位点某碱基对precision = 该位点患病样本中某碱基对数量 / 所有患病样本数量
#   某位点某碱基对recall = 该位点患病样本中某碱基对数量 / 所有样本该位点此碱基对数量
#   f1 = precision * recall / (precision + recall)
#
# 输出: 三个 json 文件, 每个文件格式: {'位点名称如:rs2340587': {'位点第一个值如:TC': float, '位点第二个值如:TT': float, '位点第三个值如:CC': float}}
#
# author tyd
#
# 2016-9-17

from load_data import DataLoader;
from copy import deepcopy;
from json import dumps as json_dump;

if __name__ == '__main__':
    dl = DataLoader();

    locus_info = dl.load_genotype();    # 位点文件读取
    locus_names = locus_info[0];        # 位点名字数组
    locus = locus_info[1];              # 位点二维数组, 纵向索引是样本索引, 横向是位点索引
    locus_num = len(locus_names);       # 位点数量

    sample_num = len(locus);            # 总样本数量, 患病样本数为总样本数量的一半

    data_dict = {};                     # 用于储存所有样本每个位点每个碱基对出现的次数
    data_dict_not_sick = {};            # 用于储存患病样本每个位点每个碱基对出现的次数

    for i in range(locus_num):                                  # 统计未患病样本的位点数据
        cur_locus_name = locus_names[i];
        data_dict[cur_locus_name] = {};

        for j in range(sample_num / 2):
            cur_locus = locus[j][i];

            if cur_locus in data_dict[cur_locus_name].keys():
                data_dict[cur_locus_name][cur_locus] += 1;
            else:
                data_dict[cur_locus_name][cur_locus] = 0;

    data_dict_not_sick = deepcopy(data_dict);                   # 将当前统计到的未患病样本的位点数据另存

    for i in range(locus_num):                                  # 统计患病样本的位点数据
        cur_locus_name = locus_names[i];

        for j in range(sample_num / 2, sample_num):
            cur_locus = locus[j][i];

            if cur_locus in data_dict[cur_locus_name].keys():
                data_dict[cur_locus_name][cur_locus] += 1;
            else:
                data_dict[cur_locus_name][cur_locus] = 0;

    recall_dict = data_dict;                    # 保存 recall 值的字典, 实际与 data_dict 共用
    precision_dict = data_dict_not_sick;        # 保存 precision 值的字典, 实际与 data_dict_not_sick 共用

    for locus_key in data_dict:                                                     # 计算 recall 和 precision
        for basic_group_key in data_dict[locus_key]:
            total_num = data_dict[locus_key][basic_group_key];
            basic_group_num = float(total_num);

            if basic_group_key in data_dict_not_sick.keys():
                basic_group_num = float(total_num - data_dict_not_sick[locus_key][basic_group_key]);

            recall_dict[locus_key][basic_group_key] = basic_group_num / total_num;
            precision_dict[locus_key][basic_group_key] = basic_group_num / sample_num / 2;

    file = open('../data/generated/locus.recall.json', 'w');
    file.write(json_dump(recall_dict));
    file.close();

    file = open('../data/generated/locus.precision.json', 'w');
    file.write(json_dump(precision_dict));
    file.close();

    f1_dict = data_dict;                        # 保存 f1 值的字典, 实际与 data_dict 共用

    for locus_key in data_dict:                                                     # 计算 f1
        for basic_group_key in data_dict[locus_key]:
            f1_dict[locus_key][basic_group_key] = precision_dict[locus_key][basic_group_key] * recall_dict[locus_key][basic_group_key] / (precision_dict[locus_key][basic_group_key] + recall_dict[locus_key][basic_group_key]) * 2;

    file = open('../data/generated/locus.f1.json', 'w');
    file.write(json_dump(f1_dict));
    file.close();
