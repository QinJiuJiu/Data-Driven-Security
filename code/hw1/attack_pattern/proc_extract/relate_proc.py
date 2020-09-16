# import numpy
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":

    filePath_proc = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc.txt"
    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/rank_redteam.txt"
    proc = open(filePath_proc)
    redteam = open(filePath_redteam)

    redteam_list = []
    attack_time = []
    user_domain = []
    source_computer = []
    destination_computer = []

    attacker_dict = {}
    victim_for_each_attacker = {}

    for line in redteam.readlines():
        print(line)
        rk, ts, host, src, dst = line.strip('\n').split(',')
        proc_file_temp = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/" + src + "/" + dst + ".txt"
        if os.path.exists(proc_file_temp):
            with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/" + src + "/" + dst + ".txt", "r") as fp:
                for fp_line in fp.readlines():
                    fp_ts, domain, fp_src, fp_proc, fp_state = fp_line.strip('\n').split(',')
                    if abs(int(fp_ts) - int(ts)) <= 3600:
                        with open(
                                "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/relate_" + src + "/" + dst + ".txt",
                                "a") as fp_write:
                            fp_write.write(rk + "," + fp_line)
                        fp_write.close()

            fp.close()

        proc_file_src = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/" + src + ".txt"
        if os.path.exists(proc_file_src):
            with open(proc_file_src, "r") as fp:
                for fp_line in fp.readlines():
                    fp_ts, domain, fp_src, fp_proc, fp_state = fp_line.strip('\n').split(',')
                    if abs(int(fp_ts) - int(ts)) <= 3600:
                        with open(
                                "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/relate_" + src + ".txt",
                                "a") as fp_write:
                            fp_write.write(rk + "," + fp_line)
                        fp_write.close()

            fp.close()
