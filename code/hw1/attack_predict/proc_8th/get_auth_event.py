import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # filePath_proc = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/proc/proc_8.txt"
    # filePath_procnamelist = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/procnamelist.txt"
    # proc = open(filePath_proc)
    # pnlist = open(filePath_procnamelist)
    timelist = [[] for i in range(25)]

    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/proc_tags")
    print(fileList)
    for file in fileList:
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/proc_tags/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                src, ts = fp_line.strip('\n').split(',')
                timelist[int(ts)].append(src)

    l = timelist[1]
    fp = open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth_8.txt", "r")
    while True:
        line = fp.readline()
        print(line)
        if line:
            ts, ud, sd, src1, src2, au, a1, a2, a3 = line[:-1].split(",")
            ttt = np.math.floor((int(ts) - 691200) / 3600)
            for i in range(len(timelist[ttt])):
                if timelist[ttt][i] == src2:
                    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth/auth_attacker.txt", "a") as ff:
                        ff.write(line)

    fp.close()




