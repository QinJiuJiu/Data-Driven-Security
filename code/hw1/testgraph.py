import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

G = nx.MultiDiGraph()

filePath_dns = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/dns.txt/attack_dns.txt"
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

dns_users = []
dns_dict = {}
for line in dns.readlines():
    dns_line = line[:-1]
    dns_line = dns_line.split(",")
    dns_list.append(dns_line)
    users_source.append(dns_line[1])
    users_dst.append(dns_line[2])
    dns_users_temp = dns_line[1] + dns_line[2]
    if dns_users_temp not in dns_dict:
        dns_dict[dns_users_temp] = 0
    else:
        dns_dict[dns_users_temp] += 1

    # print(line)

users = users_source + users_dst
users = list(set(users))
num_users = len(users)

G.add_nodes_from(users)

node_list = []

for i in dns_dict:
    str = i.split("C")
    str = str[1:]
    str[0] = "C" + str[0]
    str[1] = "C" + str[1]
    G.add_edge(str[0], str[1], weight = dns_dict[i])
    node_list.append(str[0])

pos=nx.spring_layout(G)
node_list = set(node_list)


edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])

nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)


# G.add_edges_from(dns_users)


nx.draw(G,pos, with_labels=True, node_size=2000)
nx.draw_networkx_nodes(G,pos,
                       nodelist=node_list,
                       node_color='r',
                       node_size=2000,
                   alpha=0.7)
plt.show()
plt.savefig("path.png")
