# import numpy
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":

    filePath_flows = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows.txt"
    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/rank_redteam.txt"
    flows = open(filePath_flows)
    redteam = open(filePath_redteam)

    redteam_list = []
    attack_time = []
    user_domain = []
    source_computer = []
    destination_computer = []

    attacker_dict = {}
    victim_for_each_attacker = {}

    for line in redteam.readlines():
        rk, ts, host, src, dst = line.strip('\n').split(',')
        flows_file_temp = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/" + src + "/" + dst + ".txt"
        if os.path.exists(flows_file_temp):
            with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/" + src + "/" + dst + ".txt", "r") as fp:
                for fp_line in fp.readlines():
                    fp_ts, fp_duration, fp_src, fp_src_p, fp_dst, fp_dst_p, protocol, c1, c2 = fp_line.strip(
                        '\n').split(',')
                    if abs(int(fp_ts) - int(ts)) <= 3600:
                        with open(
                                "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/relate_" + src + "/" + dst + ".txt",
                                "a") as fp_write:
                            fp_write.write(rk + "," + fp_line)
                        fp_write.close()

            fp.close()
