
# import numpy
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    users = ['sdhf','dhuf']
    G = nx.MultiDigraph()
    G.add_nodes_from(users)

    filePath_dns = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/dns.txt/dns.txt"
    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
    dns = open(filePath_dns)
    redteam = open(filePath_redteam)

    redteam_list = []
    attack_time = []
    for line in redteam.readlines():
        redteam_line = line[:-1]
        redteam_line = redteam_line.split(",")
        redteam_list.append(redteam_line)
        attack_time.append(redteam_line[0])

    dns_list = []
    users_source = []
    users_dst = []
    for line in dns.readlines():
        dns_line = line[:-1]
        dns_line = dns_line.split(",")
        dns_list.append(dns_line)
        users_source.append(dns_line[1])
        users_dst.append(dns_line[2])

    users = users_source + users_dst
    users = list(set(users))

    num_users = len(users)

    G = nx.MultiDigraph()
    G.add_nodes_from(users)
    for i in len(users_dst):
        G.add_edge(users_source[i], users_dst[i])

    nx.draw(G)
    plt.show()



