from sklearn.naive_bayes import GaussianNB
import csv

# 从CSV文件中加载数据
with open('iris-change.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

# 将数据拆分为特征和标签
features = []
labels = []
for row in data:
    features.append([float(row[i]) for i in range(4)])
    labels.append(row[4])

# 将数据拆分成训练集和测试集
train_size = 0.9
split_index = int(len(features) * train_size)
train_features, train_labels = features[:split_index], labels[:split_index]
test_features, test_labels = features[split_index:], labels[split_index:]

# 训练模型
gnb = GaussianNB()
gnb.fit(train_features, train_labels)

# 对测试集进行预测
predictions = gnb.predict(test_features)

# 计算模型的准确度
correct_count = sum(pred == true for pred, true in zip(predictions, test_labels))
accuracy = correct_count / len(test_labels)

# 打印准确度
print(f"Model accuracy: {accuracy:.2%}")