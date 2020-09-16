
if __name__ == "__main__":
    filePath_proc = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc.txt"
    proc = open(filePath_proc)

    while True:
        line = proc.readline()
        if line:
            proc_list = line[:-1]
            proc_list = proc_list.split(",")
            print(proc_list)
            if proc_list[0] >= "691200" and proc_list[0] < "777600" and len(proc_list[0])==6:

                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/proc_8.txt", "a") as attack_proc:
                    flag = 0
                    for l in proc_list:
                        if flag == 0:
                            attack_proc.write(l)
                            flag = 1
                        else:
                            attack_proc.write(',' + l)
                    attack_proc.write('\n')
                    attack_proc.close()
            elif proc_list[0] == "777600":
                break

        else:
            break

