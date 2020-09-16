import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


def parse_line(s):
    # s = s.replace("u'", "").replace("'", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    print(s)
    s2 = s.split(",")
    s4 = s2[0]+","+s2[2]+","+s2[3]+","+s2[4]
    s3 = []
    s3.append(s2[0])
    s3.append(s2[1])
    s3.append(s2[6])
    s3.append(s2[7])
    s3.append(s2[8])
    dat = [float(_) for _ in s3[1:]]
    return (s4, dat)


def get_data():
    with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/flows_8.txt") as f:
      lines = f.readlines()
      return [parse_line(line) for line in lines]


def train(collected_data):
    input_data = [c[1] for c in collected_data]
    # scaler = StandardScaler().fit(input_data)
    # input_data = scaler.transform(input_data)


    # min_max_scaler = MinMaxScaler()
    # input_data = min_max_scaler.fit_transform(input_data)
    # print input_data

    rng = np.random.RandomState(42)
    # clf = IsolationForest(max_samples=10*2, random_state=rng)
    # clf = IsolationForest(max_features=5)
    clf = IsolationForest(max_samples="auto", random_state=rng)
    clf.fit(input_data)
    pred_y = clf.predict(input_data)

    # bad_domains = set()
    for i,y in enumerate(pred_y):
        if y == -1:
            print("bad flows:", collected_data[i])
            # bad_domains.add(collected_data[i][0])
            with open("E:/zyt/junior1/DDS/FINAL-PROJECT/dataset-eighthday/flows_8_bad.txt",'a') as fp:
                fp.write(collected_data[i].__str__())


if __name__ == "__main__":
    dat = get_data()
    train(dat)