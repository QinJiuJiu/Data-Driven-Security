# import numpy
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    procname = []
    # proc
    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C17693")
    print(fileList)
    for file in fileList:
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C17693/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_d, fp_src, pn, pstate = fp_line.strip(
                    '\n').split(',')
                if pn not in procname:
                    procname.append(pn)

    fp.close()

    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C18025")
    print(fileList)
    for file in fileList:
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C18025/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_d, fp_src, pn, pstate = fp_line.strip(
                    '\n').split(',')
                if pn not in procname:
                    procname.append(pn)

    fp.close()

    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C19932")
    print(fileList)
    for file in fileList:
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C19932/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_d, fp_src, pn, pstate = fp_line.strip(
                    '\n').split(',')
                if pn not in procname:
                    procname.append(pn)

    fp.close()

    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C22409")
    print(fileList)
    for file in fileList:
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C22409/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_d, fp_src, pn, pstate = fp_line.strip(
                    '\n').split(',')
                if pn not in procname:
                    procname.append(pn)

    l = len(procname)
    fp.close()
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/procnamelist.txt", "a") as fp:
        fp.write(",".join(str(i) for i in procname))
    fp.close()

    # encode

    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C17693")
    print(fileList)
    for file in fileList:
        encode_list = [0 for i in range(l)]
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C17693/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_d, fp_src, pn, pstate = fp_line.strip(
                    '\n').split(',')
                k = procname.index(pn)
                encode_list[procname.index(pn)] = encode_list[procname.index(pn)] + 1
        fp.close()
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/C17693/" + str(file), "a") as fp:
            fp.write(",".join(str(i) for i in encode_list))
        fp.close()
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/proct.txt", "a") as fp:
            encode_list.insert(0, str(file)[:-4])
            fp.write(",".join(str(i) for i in encode_list))
            fp.write('\n')
        fp.close()


    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C18025")
    print(fileList)
    for file in fileList:
        encode_list = [0 for i in range(l)]
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C18025/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_d, fp_src, pn, pstate = fp_line.strip(
                    '\n').split(',')
                encode_list[procname.index(pn)] = encode_list[procname.index(pn)] + 1
        fp.close()
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/C18025/" + str(file), "a") as fp:
            fp.write(",".join(str(i) for i in encode_list))
        fp.close()
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/proct.txt", "a") as fp:
            encode_list.insert(0, str(file)[:-4])
            fp.write(",".join(str(i) for i in encode_list))
            fp.write('\n')
        fp.close()


    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C19932")
    print(fileList)
    for file in fileList:
        encode_list = [0 for i in range(l)]
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C19932/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_d, fp_src, pn, pstate = fp_line.strip(
                    '\n').split(',')
                encode_list[procname.index(pn)] = encode_list[procname.index(pn)] + 1
        fp.close()
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/C19932/" + str(file), "a") as fp:
            fp.write(",".join(str(i) for i in encode_list))
        fp.close()
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/proct.txt", "a") as fp:
            encode_list.insert(0, str(file)[:-4])
            fp.write(",".join(str(i) for i in encode_list))
            fp.write('\n')
        fp.close()


    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C22409")
    print(fileList)
    for file in fileList:
        encode_list = [0 for i in range(l)]
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C22409/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_d, fp_src, pn, pstate = fp_line.strip(
                    '\n').split(',')
                encode_list[procname.index(pn)] = encode_list[procname.index(pn)] + 1
        fp.close()
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/C22409/" + str(file), "a") as fp:
            fp.write(",".join(str(i) for i in encode_list))
        fp.close()
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/proct.txt", "a") as fp:
            encode_list.insert(0, str(file)[:-4])
            fp.write(",".join(str(i) for i in encode_list))
            fp.write('\n')
        fp.close()





