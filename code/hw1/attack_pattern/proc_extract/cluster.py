import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
# from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import Birch
from sklearn.mixture import GaussianMixture

def tsne_dimensionality_reduction():
    """将多维数据降维2维"""
    label = []
    list = []
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/proct.txt", "r") as fp:
        for fp_line in fp.readlines():
            temp = fp_line[:-1].split(",")
            temp = [int(tt) for tt in temp]
            list.append(temp[1:])
            label.append(temp)
    fp.close()

    # 4个3维的数据
    x = np.array(list)
    # 嵌入空间的维度为2，即将数据降维成2维
    ts = TSNE(n_components=2)
    # 训练模型
    ts.fit_transform(x)
    # 打印结果
    ttttt = ts.embedding_
    print(ts.embedding_)

    fig = plt.figure()  # 创建图形实例
    ax = plt.subplot(111)  # 创建子图
    # 遍历所有样本
    l = len(ts.embedding_)
    x_min, x_max = np.min(ts.embedding_, 0), np.max(ts.embedding_, 0)
    data = (ts.embedding_ - x_min) / (x_max - x_min)  # 对数据进行归一化处理
    for i in range(len(ts.embedding_)):
        # 在图中为每个数据点画出标签
        aaa = data[i]
        plt.text(data[i][0], data[i][1], str(label[i][0]), color=plt.cm.Set1(label[i][0] / 1000),
                 fontdict={'weight': 'bold', 'size': 7})
    plt.xticks()  # 指定坐标的刻度
    plt.yticks()
    plt.title("title", fontsize=14)

    plt.show()

    """Britch Cluster"""
    y_pred = Birch(n_clusters=None).fit_predict(ts.embedding_)
    plt.scatter(ts.embedding_[:, 0], ts.embedding_[:, 1], c=y_pred)
    plt.show()
    from sklearn import metrics
    print("Brich", metrics.calinski_harabaz_score(ts.embedding_, y_pred))

    """GaussianMixture Cluster"""
    ##设置gmm函数
    gmm = GaussianMixture(n_components=8, covariance_type='full').fit(ts.embedding_)
    ##训练数据
    y_pred = gmm.predict(ts.embedding_)

    ##绘图
    plt.scatter(ts.embedding_[:, 0], ts.embedding_[:, 1], c=y_pred)
    plt.show()

    """写入文件"""
    for i in range(len(y_pred)):
        type = y_pred[i]
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/attack_pattern_proc/"+str(type)+".txt", "a") as fp:
            temp = []
            temp.append(label[i][0])
            temp.append(ts.embedding_[i, 0])
            temp.append(ts.embedding_[i, 1])
            fp.write(",".join(str(i) for i in temp))
            fp.write('\n')

        fp.close()

if __name__ == "__main__":
    tsne_dimensionality_reduction()