# import numpy
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":

    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
    redteam = open(filePath_redteam)

    redteam_list = []
    attack_time = []
    user_domain = []
    source_computer = []
    destination_computer = []

    attacker_dict = {}
    victim_for_each_attacker = {}

    count = 1

    for line in redteam.readlines():
        ts, host, src, dst = line.strip('\n').split(',')
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/rank_redteam.txt",
                  "a") as fp_write:
            fp_write.write(str(count) + "," + line)
        fp_write.close()
        count = count + 1

