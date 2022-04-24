from sklearn.ensemble import RandomForestClassifier
import math
def initData(name):
    length = len(name)
    entropy = 0
    nums = 0
    for i in name:
        if i.isdigit():
            nums += 1
    count = 26 * [0]
    sum = 0
    for i in name:
        if i.isalpha():
            i = i.lower()
            count[ord(i) - ord('a')] += 1
            sum += 1
    for i in range(26):
        p = 1.0 * count[i] / sum
        if p > 0:
            entropy += -(p * math.log(p, 2))
    return [length,nums,entropy]
def main():
    featureMatrix = []
    labelList = []
    with open("train.txt") as f:
        for line in f:
            line = line.strip()
            tokens = line.split(",")
            name = tokens[0]
            label = 1
            if tokens[1] == "dga":
                label = 0
            featureMatrix.append(initData(name))
            labelList.append(label)
    clf = RandomForestClassifier(random_state=0)
    clf.fit(featureMatrix, labelList)
    with open("test.txt") as a, open('result.txt','w') as b:
        for line in a:
            line = line.strip()
            if clf.predict([initData(line)]):
                label = ",notdga\n"
            else:
                label=",dga\n"
            line = line + label
            b.write(line)
main()
