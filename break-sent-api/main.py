from tqdm import tqdm

res = [[0 for i in range(2)] for i in range(2)]

with open('eval.1955582.output', 'rb') as f:
    n = 0
    lines = f.readlines()
    for i in tqdm(range(len(lines))):
        line = lines[i]
        if len(line) == 1 or n == 49:
            n = 0
            continue
        temp = (line.decode('utf-8').strip('\n')).split(' ')
        act = temp[1]
        pred = temp[2]
        if act == 'B' and pred == 'B': res[0][0] += 1
        elif act == 'B' and pred != 'B': res[0][1] += 1
        elif act != 'B' and pred == 'B': res[1][0] += 1
        else: res[1][1] += 1

        n += 1

# print(res)
TP = res[0][0]
FN = res[0][1]
FP = res[1][0]
TN = res[1][1]

sum = TP + FN + FP + TN

acu = (TP + TN) / sum
print('acu', acu)
P = TP / (TP + FP)
print('p', P)
R = TP / (TP + FN)
print('r', R)
F1 = (2 * TP) / (sum + TP - TN)
print('f1', F1)
