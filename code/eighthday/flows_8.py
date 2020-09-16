if __name__ == "__main__":
    filePath_flows = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows.txt"
    flows = open(filePath_flows)

    while True:
        line = flows.readline()
        if line:
            flows_list = line[:-1]
            flows_list = flows_list.split(",")
            print(flows_list)
            if flows_list[0] >= "691200" and flows_list[0] < "777600" and len(flows_list[0])==6:

                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/flows_8.txt", "a") as attack_flows:
                    flag = 0
                    for l in flows_list:
                        if flag == 0:
                            attack_flows.write(l)
                            flag = 1
                        else:
                            attack_flows.write(',' + l)
                    attack_flows.write('\n')
                    attack_flows.close()
            elif flows_list[0] == "777600":
                break

        else:
            break
