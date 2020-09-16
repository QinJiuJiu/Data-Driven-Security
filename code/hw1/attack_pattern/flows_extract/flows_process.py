# import numpy
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":

    filePath_flows = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows.txt"
    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
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
        ts, host, src, dst = line.strip('\n').split(',')
        if src not in attacker_dict:
            attacker_dict[src] = 0
            victim_for_each_attacker[src] = {}
        attacker_dict[src] += 1
        if dst not in victim_for_each_attacker[src]:
            victim_for_each_attacker[src][dst] = 0
        victim_for_each_attacker[src][dst] += 1

    # Fp = open('E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows_redteam.txt', 'a')
    print(attacker_dict)

    while True:
        line = flows.readline()
        if line:
            flows_line = line[:-1]
            flows_line = flows_line.split(",")
            print(flows_line)

            if flows_line[2] in attacker_dict:
                if flows_line[4] in victim_for_each_attacker[flows_line[2]]:
                    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/" + flows_line[2]+"/"+ flows_line[4]+ ".txt", "a") as fp:
                        fp.write(line)
                    fp.close()

            if flows_line[4] in attacker_dict:
                if flows_line[2] in victim_for_each_attacker[flows_line[4]]:
                    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/" + flows_line[4]+"/"+ flows_line[2]+ ".txt", "a") as fp:
                        fp.write(line)
                    fp.close()


