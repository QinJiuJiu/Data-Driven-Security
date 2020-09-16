import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    label = []
    list = []
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/encode/portt.txt", "r") as fp:
        for fp_line in fp.readlines():
            temp = fp_line[:-1].split(",")
            a = len(temp)
            temp = [int(tt) for tt in temp]
            list.append(temp[1:])
            label.append(temp)
    fp.close()

    port_name = []
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/encode/portnamelist.txt", "r") as fp:
        for fp_line in fp.readlines():
            port_name = fp_line[:-1].split(",")
    fp.close()

    fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows_rk")
    print(fileList)
    count = [0 for i in range(len(port_name))]
    for file in fileList:
        with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows_rk/" + str(file), "r") as fp:
            for fp_line in fp.readlines():
                print(fp_line)
                fp_rk, fp_ts, fp_duration, fp_src, fp_src_p, fp_dst, fp_dst_p, protocol, c1, c2 = fp_line.strip(
                    '\n').split(',')
                if fp_src_p in port_name:
                    k = port_name.index(fp_src_p)
                    count[port_name.index(fp_src_p)] = count[port_name.index(fp_src_p)] + 1
        fp.close()

    i = 0
    len = len(port_name)
    while True:
        if count[i] < 100:
            count.pop(i)
            port_name.pop(i)
            len = len -1
        else:
            i = i + 1
        if i >= len:
            break


    # 保证圆形


    plt.axes(aspect=1)
    patches,l_text,p_text = plt.pie(x=count, labels=port_name, autopct='%3.1f %%')
    for t in l_text:
        t.set_size = (5)
    for t in p_text:
        t.set_size = (5)

    plt.show()

    print(count)
    print(port_name)

    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/attack_pattern_flows/portlist.txt", "a") as fp:
        fp.write(",".join(str(j) for j in port_name))
    fp.close()


