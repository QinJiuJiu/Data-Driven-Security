# import numpy
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":

    filePath_dns = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/dns.txt/dns.txt"
    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
    dns = open(filePath_dns)
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

    # Fp = open('E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/dns.txt/dns_redteam.txt', 'a')
    print(attacker_dict)

    while True:
        line = dns.readline()
        if line:
            dns_line = line[:-1]
            dns_line = dns_line.split(",")
            print(dns_line)

            if dns_line[1] in attacker_dict:
                if dns_line[2] in victim_for_each_attacker[dns_line[1]]:
                    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/dns.txt/" + dns_line[1]+"/"+ dns_line[2]+ ".txt", "a") as fp:
                        fp.write(line)
                    fp.close()

            if dns_line[2] in attacker_dict:
                if dns_line[1] in victim_for_each_attacker[dns_line[2]]:
                    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/dns.txt/" + dns_line[2]+"/"+ dns_line[1]+ ".txt", "a") as fp:
                        fp.write(line)
                    fp.close()


