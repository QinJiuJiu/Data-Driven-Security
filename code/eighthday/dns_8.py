if __name__ == "__main__":
    filePath_dns = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/dns.txt/dns.txt"
    dns = open(filePath_dns)

    while True:
        line = dns.readline()
        if line:
            dns_list = line[:-1]
            dns_list = dns_list.split(",")
            print(dns_list)
            if dns_list[0] >= "691200" and dns_list[0] < "777600" and len(dns_list[0])==6:

                with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/dns_8.txt", "a") as attack_dns:
                    flag = 0
                    for l in dns_list:
                        if flag == 0:
                            attack_dns.write(l)
                            flag = 1
                        else:
                            attack_dns.write(',' + l)
                    attack_dns.write('\n')
                    attack_dns.close()
            elif dns_list[0] == "777600":
                break

        else:
            break
