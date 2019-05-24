#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
决策树
CART分类树 算法
练习demo
"""


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris = load_iris()  # 准备数据
features = iris.data
labels = iris.target

# 随机抽取33%的测试数据集


train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33,
                                                                            random_state=0)

# 创建cart 树
clf = DecisionTreeClassifier(criterion='gini')

# 拟合构建分类树
clf = clf.fit(train_features, train_labels)
# 用cart  做分类预测额
test_predict = clf.predict(test_features)

# 预测结果与测试集做对比
score = accuracy_score(test_labels, test_predict)

print('CART分类树准确率 %.4lf' % score)
