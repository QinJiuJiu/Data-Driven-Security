import matplotlib.pyplot as plt
import numpy as np

import random
def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return "#"+color


filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
with open(filePath_redteam, "r") as f:
    most_active_attacker_dict = {}
    most_poor_victim_for_each_attacker = {}
    most_poor_victim_for_all_attackers = {}

    for line in f:
        ts, host, src, dst = line.strip('\n').split(',')

        if src not in most_active_attacker_dict:
            most_active_attacker_dict[src] = 0
            most_poor_victim_for_each_attacker[src] = {}
        most_active_attacker_dict[src] += 1
        if dst not in most_poor_victim_for_each_attacker[src]:
            most_poor_victim_for_each_attacker[src][dst] = 0
        most_poor_victim_for_each_attacker[src][dst] += 1

        if dst not in most_poor_victim_for_all_attackers:
            most_poor_victim_for_all_attackers[dst] = 0
        most_poor_victim_for_all_attackers[dst] += 1

    for a in sorted(most_active_attacker_dict.items(), key=lambda s: s[1], reverse=True):
        print("attacker => count: %4d | src: %s | number of victims: %4d"
              % (a[1], a[0], len(most_poor_victim_for_each_attacker[a[0]])))
        # print("number of victims: " + str(len(most_poor_victim_for_each_attacker[a[0]])))
        for v in sorted(most_poor_victim_for_each_attacker[a[0]].items(), key=lambda s: s[1], reverse=True):
            if v[1] < most_poor_victim_for_all_attackers[v[0]]:
                print("  victim => count: %4d | dst: %6s   << total: %4d" % (
                    v[1], v[0], most_poor_victim_for_all_attackers[v[0]]))
            else:
                print("  victim => count: %4d | dst: %6s" % (v[1], v[0]))
        print("\n")

    # plot

    # 构建数据
    x_data = []
    y_data = []
    for a in sorted(most_active_attacker_dict.items(), key=lambda s: s[1], reverse=True):
        x_data.append(a[0])

    for all in sorted(most_poor_victim_for_all_attackers.items(), key=lambda s: s[1], reverse=True):
        # print(all[0])
        temp_list = []
        for a in sorted(most_active_attacker_dict.items(), key=lambda s: s[1], reverse=True):
            if all[0] in most_poor_victim_for_each_attacker[a[0]]:
                num = most_poor_victim_for_each_attacker[a[0]][all[0]]
                print(num)
                temp_list.append(num)

            else:
                temp_list.append(0)

        y_data.append(temp_list)

    # 绘图
    l = len(y_data)
    for i in range(l-1):
        y_data[i + 1][0] = y_data[i][0]+y_data[i + 1][0]
        y_data[i + 1][1] = y_data[i][1]+y_data[i + 1][1]
        y_data[i + 1][2] = y_data[i][2]+y_data[i + 1][2]
        y_data[i + 1][3] = y_data[i][3]+y_data[i + 1][3]
    count = 0
    y_data.reverse()
    for all in sorted(most_poor_victim_for_all_attackers.items(), key=lambda s: s[1], reverse=False):
        ttt = y_data[0]
        plt.bar(x=x_data, height=y_data[count], label=all[0], color=randomcolor(), alpha=0.8)
        # plt.bar(x=x_data, height=y_data[count], color='steelblue', alpha=0.8)
        count = count + 1
    # 设置标题
    plt.title("Distribution of attack frequency")
    # 为两条坐标轴设置名称
    plt.xlabel("Attacker")
    plt.ylabel("Number of attack items")
    # 显示图例
    # plt.legend()
    plt.show()

# with open("./data/dns.txt", "r") as f:
#     for line in f:
#         time, src, resolved = line.split(',')
#         print(time, src, resolved)
