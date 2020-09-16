if __name__ == "__main__":
    filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/redteam.txt/redteam.txt"
    redteam = open(filePath_redteam)

    while True:
        line = redteam.readline()
        if line:
            redteam_list = line[:-1]
            redteam_list = redteam_list.split(",")
            print(redteam_list)
            if redteam_list[0] >= "691200" and redteam_list[0] < "777600":

                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/redteam_8.txt", "a") as attack_redteam:
                    flag = 0
                    for l in redteam_list:
                        if flag == 0:
                            attack_redteam.write(l)
                            flag = 1
                        else:
                            attack_redteam.write(',' + l)
                    attack_redteam.write('\n')
                    attack_redteam.close()
            elif redteam_list[0] >= "777600":
                break

        else:
            break
