import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

if __name__ == "__main__":

    filePath_proc = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/proc_8.txt"
    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
    filePath_procnamelist = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/procnamelist.txt"
    proc = open(filePath_proc)
    redteam = open(filePath_redteam)
    pnlist = open(filePath_procnamelist)

    procnamelist = []
    for line in pnlist.readlines():
        procnamelist = line.strip('\n').split(',')

    l = len(procnamelist)
    count = 1
    src_c = []
    pnl = []

    while True:
        line = proc.readline()
        if line:
            proc_line = line[:-1]
            fp_ts, fp_d, fp_src, pn, pstate = line.strip('\n').split(',')
            print(line)

            # t = int(fp_ts) - 691200 * count

            if int(fp_ts) - 691200  <= 3600*count:
                if fp_src not in src_c:
                    src_c.append(fp_src)
                    encodel = [0 for i in range(len(procnamelist))]
                    if pn in procnamelist:
                        encodel[procnamelist.index(pn)] = encodel[procnamelist.index(pn)] + 1
                    pnl.append(encodel)
                else:
                    index = src_c.index(fp_src)
                    if pn in procnamelist:
                        pnl[index][procnamelist.index(pn)] = pnl[index][procnamelist.index(pn)] + 1
            else:
                # 4个3维的数据
                x = np.array(pnl)
                # 嵌入空间的维度为2，即将数据降维成2维
                ts = TSNE(n_components=2)
                # 训练模型
                ts.fit_transform(x)
                # 打印结果
                ttttt = ts.embedding_
                print(ts.embedding_)

                # fig = plt.figure()  # 创建图形实例
                # ax = plt.subplot(111)  # 创建子图
                # # 遍历所有样本
                # l = len(ts.embedding_)
                # x_min, x_max = np.min(ts.embedding_, 0), np.max(ts.embedding_, 0)
                # data = (ts.embedding_ - x_min) / (x_max - x_min)  # 对数据进行归一化处理
                # for i in range(len(ts.embedding_)):
                #     # 在图中为每个数据点画出标签
                #     aaa = data[i]
                #     plt.text(data[i][0], data[i][1], str(src_c[i]), color=plt.cm.Set1(int(src_c[i][1:]) / 10000),
                #              fontdict={'weight': 'bold', 'size': 7})
                # plt.xticks()  # 指定坐标的刻度
                # plt.yticks()
                # plt.title("feature distribution "+ str(count), fontsize=14)
                #
                # plt.show()

                for i in range(len(src_c)):
                    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/proc/" + str(count) +".txt", "a") as fp:
                        fp.write(src_c[i]+",")
                        fp.write(",".join(str(i) for i in ts.embedding_[i]))
                        fp.write('\n')
                    fp.close()

                count = count + 1
                src_c.clear()
                pnl.clear()

                if fp_src not in src_c:
                    src_c.append(fp_src)
                    encodel = [0 for i in range(len(procnamelist))]
                    if pn in procnamelist:
                        encodel[procnamelist.index(pn)] = encodel[procnamelist.index(pn)] + 1
                    pnl.append(encodel)
                else:
                    index = src_c.index(fp_src)
                    if pn in procnamelist:
                        pnl[index][procnamelist.index(pn)] = pnl[index][procnamelist.index(pn)] + 1



        else:
            break