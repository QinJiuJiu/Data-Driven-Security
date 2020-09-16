import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # fp = open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth/auth_attacker.txt", "r")
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth/auth_attacker.txt", "r") as fp:
        for line in fp.readlines():
            print(line)
            if line:
                ts, ud, sd, src1, src2, au, a1, a2, a3 = line[:-1].split(",")
                if au == "NTLM" and a1 == "Network" and a2 == "LogOn":
                    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth/auth_attacker_final.txt", "a") as ff:
                        ff.write(line)

    fp.close()
