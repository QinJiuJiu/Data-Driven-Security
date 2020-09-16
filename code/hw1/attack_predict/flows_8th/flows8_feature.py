import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

if __name__ == "__main__":

    filePath_flows = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/flows_8.txt"
    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
    filePath_portlist = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/attack_pattern_flows/portlist.txt"
    flows = open(filePath_flows)
    redteam = open(filePath_redteam)
    pnlist = open(filePath_portlist)

    portlist = []
    for line in pnlist.readlines():
        portlist = line.strip('\n').split(',')

    l = len(portlist)
    count = 1
    src_c = []
    pnl = []

    while True:
        line = flows.readline()
        if line:
            proc_line = line[:-1]
            print(line)
            fp_ts, fp_d, fp_src, src_pn, fp_dst, dst_pn, p1, p2, p3 = line.strip('\n').split(',')


            # t = int(fp_ts) - 691200 * count
            t = fp_src+","+fp_dst
            if int(fp_ts) - 691200 <= 3600 * count:
                if t not in src_c:
                    src_c.append(t)
                    encodel = [0 for i in range(len(portlist))]
                    if src_pn in portlist:
                        encodel[portlist.index(src_pn)] = encodel[portlist.index(src_pn)] + 1
                    pnl.append(encodel)
                else:
                    index = src_c.index(t)
                    if src_pn in portlist:
                        pnl[index][portlist.index(src_pn)] = pnl[index][portlist.index(src_pn)] + 1
            else:

                for i in range(len(src_c)):
                    if np.sum(pnl[i]) > 10:
                        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/flows/flow_attack.txt",
                              "a") as fp:
                            fp.write(src_c[i] + ","+str(count))
                            fp.write('\n')
                        fp.close()

                count = count + 1
                src_c.clear()
                pnl.clear()

                if t not in src_c:
                    src_c.append(t)
                    encodel = [0 for i in range(len(portlist))]
                    if src_pn in portlist:
                        encodel[portlist.index(src_pn)] = encodel[portlist.index(src_pn)] + 1
                    pnl.append(encodel)
                else:
                    index = src_c.index(t)
                    if src_pn in portlist:
                        pnl[index][portlist.index(src_pn)] = pnl[index][portlist.index(src_pn)] + 1



        else:
            break
