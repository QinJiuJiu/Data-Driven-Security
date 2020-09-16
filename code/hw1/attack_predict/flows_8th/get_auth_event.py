import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":

    timelist = [[] for i in range(25)]

    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/flows")
    print(fileList)
    for file in fileList:
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/flows/flow_attack.txt", "r") as fp:
            for fp_line in fp.readlines():
                src, dst, ts = fp_line.strip('\n').split(',')
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
                    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth/auth_attacker_flows.txt", "a") as ff:
                        ff.write(line)

    fp.close()




