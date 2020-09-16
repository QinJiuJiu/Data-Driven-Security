import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":
    count = 0
    tttt = 0
    # fp = open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth/auth_attacker.txt", "r")
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth/auth_attacker_final.txt", "r") as fp:
        for line in fp.readlines():
            # print(line)
            if line:
                tttt = 0
                ts, ud, sd, src1, src2, au, a1, a2, a3 = line[:-1].split(",")
                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/redteam_8.txt", "r") as fps:
                    for lines in fps.readlines():
                        lts, lud, src, dst = lines[:-1].split(",")
                        tttt = tttt + 1
                        if src1 == src and src2 == dst:
                            print(lines)
                            count = count + 1
                            with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/predict_redteam/proc.txt",
                                      "a") as fff:
                                fff.write(lines)


    print("Number of correct predict by proc: " + str(count))
    fp.close()

    temp = count

    count = 0
    # fp = open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth/auth_attacker.txt", "r")
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth/auth_attacker_flows_final.txt", "r") as fp:
        for line in fp.readlines():
            # print(line)
            if line:
                ts, ud, sd, src1, src2, au, a1, a2, a3 = line[:-1].split(",")
                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/redteam_8.txt", "r") as fps:
                    for lines in fps.readlines():
                        lts, lud, src, dst = lines[:-1].split(",")
                        if src1 == src and src2 == dst:
                            # print(lines)
                            count = count + 1
                            with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/predict_redteam/flows.txt",
                                      "a") as fff:
                                fff.write(lines)

    print("Number of correct predict by flows: " + str(count))
    print("The number of correct predict by all features: " + str(round((count + temp) / 222, 2) * 100) + "%")

    fp.close()
