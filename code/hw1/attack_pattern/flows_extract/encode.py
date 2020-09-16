# import numpy
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    portname = []
    # proc
    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows_rk")
    print(fileList)
    for file in fileList:
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows_rk/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_duration, fp_src, fp_src_p, fp_dst, fp_dst_p, protocol, c1, c2 = fp_line.strip(
                        '\n').split(',')
                if fp_src_p not in portname:
                    portname.append(fp_src_p)

    fp.close()


    l = len(portname)
    fp.close()
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/encode/portnamelist.txt", "a") as fp:
        fp.write(",".join(str(i) for i in portname))
    fp.close()

    # encode

    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows_rk")
    print(fileList)
    for file in fileList:
        encode_list = [0 for i in range(l)]
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows_rk/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_duration, fp_src, fp_src_p, fp_dst, fp_dst_p, protocol, c1, c2 = fp_line.strip(
                    '\n').split(',')
                k = portname.index(fp_src_p)
                encode_list[portname.index(fp_src_p)] = encode_list[portname.index(fp_src_p)] + 1
        fp.close()
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/encode/" + str(file), "a") as fp:
            fp.write(",".join(str(i) for i in encode_list))
        fp.close()
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/encode/portt.txt", "a") as fp:
            encode_list.insert(0, str(file)[:-4])
            fp.write(",".join(str(i) for i in encode_list))
            fp.write('\n')
        fp.close()






