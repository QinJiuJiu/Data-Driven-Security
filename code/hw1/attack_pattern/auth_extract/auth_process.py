# import numpy
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 从auth文件中提取攻击事件包含的验证信息

if __name__ == "__main__":

    filePath_auth = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/auth.txt/auth.txt"
    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
    auth = open(filePath_auth)
    redteam = open(filePath_redteam)

    redteam_list = []
    attack_time = []
    user_domain = []
    source_computer = []
    destination_computer = []

    for line in redteam.readlines():
        redteam_line = line[:-1]
        redteam_line = redteam_line.split(",")
        redteam_list.append(redteam_line)
        attack_time.append(redteam_line[0])
        user_domain.append(redteam_line[1])
        source_computer.append(redteam_line[2])
        destination_computer.append(redteam_line[3])

    count = 0
    # Fp = open('E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/auth.txt/auth_redteam.txt', 'a')

    while True:
        line = auth.readline()
        if line:
            auth_line = line[:-1]
            auth_line = auth_line.split(",")
            print(count)
            print(auth_line)

            if len(auth_line[0]) < 6:
                continue
            if len(auth_line[0]) == 6:
                if auth_line[0] < "150885":
                    continue

            with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/auth.txt/auth_redteam.txt", "a") as fp:
                for i in range(len(attack_time)):
                    if auth_line[0] == attack_time[i]:
                        if auth_line[1] == user_domain[i] or auth_line[2] == user_domain[i]:
                            if auth_line[3] == source_computer[i]:
                                if auth_line[4] == destination_computer[i]:
                                    fp.write(line)
                                    count = count + 1
            fp.close()
        elif auth_line[0] == "2557048":
            break
