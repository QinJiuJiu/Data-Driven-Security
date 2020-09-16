# import numpy
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":

    filePath_proc = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc.txt"
    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
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
        ts, host, src, dst = line.strip('\n').split(',')
        if src not in attacker_dict:
            attacker_dict[src] = 0
            victim_for_each_attacker[src] = {}
        attacker_dict[src] += 1
        if dst not in victim_for_each_attacker[src]:
            victim_for_each_attacker[src][dst] = 0
        victim_for_each_attacker[src][dst] += 1

    # Fp = open('E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_redteam.txt', 'a')

    while True:
        line = proc.readline()
        if line:
            proc_line = line[:-1]
            proc_line = proc_line.split(",")
            print(proc_line)

            if proc_line[2] == "C17693":
                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/C17693.txt", "a") as fp:
                    fp.write(line)
                fp.close()

            if proc_line[2] == "C18025":
                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/C18025.txt", "a") as fp:
                    fp.write(line)
                fp.close()

            if proc_line[2] == "C19932":
                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/C19932.txt", "a") as fp:
                    fp.write(line)
                fp.close()

            if proc_line[2] == "C22409":
                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/C22409.txt", "a") as fp:
                    fp.write(line)
                fp.close()

            if proc_line[2] in victim_for_each_attacker["C17693"]:
                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/C17693/" + proc_line[2] + ".txt", "a") as fp:
                    fp.write(line)
                fp.close()

            if proc_line[2] in victim_for_each_attacker["C18025"]:
                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/C18025/" + proc_line[2] + ".txt", "a") as fp:
                    fp.write(line)
                fp.close()

            if proc_line[2] in victim_for_each_attacker["C19932"]:
                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/C19932/" + proc_line[2] + ".txt", "a") as fp:
                    fp.write(line)
                fp.close()

            if proc_line[2] in victim_for_each_attacker["C22409"]:
                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/C22409/" + proc_line[2] + ".txt", "a") as fp:
                    fp.write(line)
                fp.close()

