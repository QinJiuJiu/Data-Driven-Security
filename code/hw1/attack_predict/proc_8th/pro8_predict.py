import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # filePath_proc = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/proc/proc_8.txt"
    # filePath_procnamelist = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/encode/procnamelist.txt"
    # proc = open(filePath_proc)
    # pnlist = open(filePath_procnamelist)

    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/proc")
    print(fileList)
    for file in fileList:
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/proc/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                flag = -1
                print(fp_line)
                src, f1, f2 = fp_line.strip('\n').split(',')
                fileLists = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/attack_pattern_proc")
                print(fileLists)
                for files in fileLists:
                    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/attack_pattern_proc/" + str(files),
                              "r") as fps:
                        for fp_lines in fps.readlines():
                            print(fp_lines)
                            fsrc, ff1, ff2 = fp_lines.strip('\n').split(',')
                            if pow(float(ff1) - float(f1), 2) + pow(float(ff2) - float(f2), 2) < 10:
                                flag = files[:-4]

                if flag != -1:
                    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/proc_tags/" + str(flag) + ".txt",
                          "a") as fps:
                        fps.write(src+","+file[:-4]+"\n")

    fp.close()


