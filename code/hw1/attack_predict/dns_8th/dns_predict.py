import matplotlib.pyplot as plt
import numpy as np

filePath_redteam = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/redteam_8.txt"
most_active_attacker_dict = {}
most_poor_victim_for_each_attacker = {}
most_poor_victim_for_all_attackers = {}
with open(filePath_redteam, "r") as f:
    for line in f:
        ts, host, src, dst = line.strip('\n').split(',')

        if src not in most_active_attacker_dict:
            most_active_attacker_dict[src] = 0
            most_poor_victim_for_each_attacker[src] = {}
        most_active_attacker_dict[src] += 1
        if dst not in most_poor_victim_for_each_attacker[src]:
            most_poor_victim_for_each_attacker[src][dst] = 0
        most_poor_victim_for_each_attacker[src][dst] += 1

        if dst not in most_poor_victim_for_all_attackers:
            most_poor_victim_for_all_attackers[dst] = 0
        most_poor_victim_for_all_attackers[dst] += 1

    for a in sorted(most_active_attacker_dict.items(), key=lambda s: s[1], reverse=True):
        print("attacker => count: %4d | src: %s | number of victims: %4d"
              % (a[1], a[0], len(most_poor_victim_for_each_attacker[a[0]])))
        # print("number of victims: " + str(len(most_poor_victim_for_each_attacker[a[0]])))
        for v in sorted(most_poor_victim_for_each_attacker[a[0]].items(), key=lambda s: s[1], reverse=True):
            if v[1] < most_poor_victim_for_all_attackers[v[0]]:
                print("  victim => count: %4d | dst: %6s   << total: %4d" % (
                    v[1], v[0], most_poor_victim_for_all_attackers[v[0]]))
            else:
                print("  victim => count: %4d | dst: %6s" % (v[1], v[0]))
        print("\n")

filePath = "E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/dns_8.txt"
src = {}
dst = {}
all_dst = {}
with open(filePath, "r") as f:
    for line in f:
        fts, fsrc, fdst = line.strip('\n').split(',')

        if fsrc not in src:
            src[fsrc] = 0
            dst[fsrc] = {}
        src[fsrc] += 1
        if fdst not in dst[fsrc]:
            dst[fsrc][fdst] = 0
        dst[fsrc][fdst] += 1

        if fdst not in all_dst:
            all_dst[fdst] = 0
        all_dst[fdst] += 1

    for a in sorted(src.items(), key=lambda s: s[1], reverse=True):
        # if a[0] == "19932" or a[0] == "22409" or a[0] == "17693":
        print(" DNS request => count: %4d | src: %s | number of DNS received: %4d"
              % (a[1], a[0], len(dst[a[0]])))
        # print("number of victims: " + str(len(most_poor_victim_for_each_attacker[a[0]])))
        for v in sorted(dst[a[0]].items(), key=lambda s: s[1], reverse=True):
            if v[1] < all_dst[v[0]]:
                print("DNS received => count: %4d | dst: %6s   << total: %4d" % (
                    v[1], v[0], all_dst[v[0]]))
            else:
                print("DNS received => count: %4d | dst: %6s" % (v[1], v[0]))
        print("\n")

after = dict(sorted(all_dst.items(), key=lambda e: e[1]))
# 取出前几个， 也可以在sorted返回的list中取前几个
required_cnt = 1000
cnt = 0

dnslist = []
for key, value in after.items():
    cnt += 1
    if cnt > required_cnt:
        break
    if key not in dnslist:
        dnslist.append(key)

viclist = []
for key, value in most_poor_victim_for_all_attackers.items():
    if key not in viclist:
        viclist.append(key)

right = 0

for i in range(len(dnslist)):
    if dnslist[i] in viclist:
        right += 1
        print(dnslist[i])

print("Number of victims in redteam: " + str(len(viclist)))
# print("Number of victims in dnslist: " + str(len(dnslist)))
print("Number of same victims in both lists: " + str(right))

