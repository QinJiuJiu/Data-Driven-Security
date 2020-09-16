import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

G = nx.MultiDiGraph()

filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
redteam = open(filePath_redteam)

redteam_list = []
users_source = []
users_dst = []

redteam_users = []
redteam_dict = {}
for line in redteam.readlines():
    redteam_line = line[:-1]
    redteam_line = redteam_line.split(",")
    redteam_list.append(redteam_line)
    users_source.append(redteam_line[2])
    users_dst.append(redteam_line[3])
    redteam_users_temp = redteam_line[2] + redteam_line[3]
    if redteam_users_temp not in redteam_dict:
        redteam_dict[redteam_users_temp] = 0
    else:
        redteam_dict[redteam_users_temp] += 1

    # print(line)

users = users_source + users_dst
users = list(set(users))
num_users = len(users)

G.add_nodes_from(users)

node_list = []

for i in redteam_dict:
    str = i.split("C")
    str = str[1:]
    str[0] = "C" + str[0]
    str[1] = "C" + str[1]
    G.add_edge(str[0], str[1], weight = redteam_dict[i])
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
