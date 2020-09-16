if __name__ == "__main__":
    filePath_auth = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/auth.txt/auth.txt"
    auth = open(filePath_auth)

    while True:
        line = auth.readline()
        if line:
            auth_list = line[:-1]
            auth_list = auth_list.split(",")
            print(auth_list)
            if auth_list[0] >= "691200" and auth_list[0] < "777600" and len(auth_list[0])==6:

                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/auth_8.txt", "a") as attack_auth:
                    flag = 0
                    for l in auth_list:
                        if flag == 0:
                            attack_auth.write(l)
                            flag = 1
                        else:
                            attack_auth.write(',' + l)
                    attack_auth.write('\n')
                    attack_auth.close()
            elif auth_list[0] == "777600":
                break

        else:
            break
