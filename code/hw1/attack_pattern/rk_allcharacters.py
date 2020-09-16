import os
# flows
fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/relate_C17693")
print(fileList)
for file in fileList:
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/relate_C17693/" + str(file), "r") as fp:
        for fp_line in fp.readlines():
            print(fp_line)
            fp_rk, fp_ts, fp_duration, fp_src, fp_src_p, fp_dst, fp_dst_p, protocol, c1, c2 = fp_line.strip(
                '\n').split(',')
            with open(
                    "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/flows.txt/flows_rk/" + fp_rk + ".txt",
                    "a") as fp_write:
                fp_write.write(fp_line)
            fp_write.close()

fp.close()

#proc
fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/relate_C17693")
print(fileList)
for file in fileList:
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/relate_C17693/" + str(file), "r") as fp:
        for fp_line in fp.readlines():
            print(fp_line)
            rk, fp_ts, domain, fp_src, fp_proc, fp_state = fp_line.strip('\n').split(',')
            with open(
                    "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C17693/" + rk + ".txt",
                    "a") as fp_write:
                fp_write.write(fp_line)
            fp_write.close()

fp.close()

fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/relate_C18025")
print(fileList)
for file in fileList:
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/relate_C18025/" + str(file), "r") as fp:
        for fp_line in fp.readlines():
            print(fp_line)
            rk, fp_ts, domain, fp_src, fp_proc, fp_state = fp_line.strip('\n').split(',')
            with open(
                    "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C18025/" + rk + ".txt",
                    "a") as fp_write:
                fp_write.write(fp_line)
            fp_write.close()

fp.close()

fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/relate_C19932")
print(fileList)
for file in fileList:
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/relate_C19932/" + str(file), "r") as fp:
        for fp_line in fp.readlines():
            print(fp_line)
            rk, fp_ts, domain, fp_src, fp_proc, fp_state = fp_line.strip('\n').split(',')
            with open(
                    "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C19932/" + rk + ".txt",
                    "a") as fp_write:
                fp_write.write(fp_line)
            fp_write.close()

fp.close()

fileList = os.listdir("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/relate_C22409")
print(fileList)
for file in fileList:
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/relate_C22409/" + str(file), "r") as fp:
        for fp_line in fp.readlines():
            print(fp_line)
            rk, fp_ts, domain, fp_src, fp_proc, fp_state = fp_line.strip('\n').split(',')
            with open(
                    "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset/proc.txt/proc_rk_C22409/" + rk + ".txt",
                    "a") as fp_write:
                fp_write.write(fp_line)
            fp_write.close()

fp.close()

