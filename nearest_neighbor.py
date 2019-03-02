import math

def knn_loocv(data):
    print ("that data set has ", len(data), " instances")
    print ("with ", len(data[0]) - 1, " features")
    i = 0
    num_correct = 0
    for i in range(len(data)):
        curr_best = 0 #stores the j value that has the smallest distance
        curr_distance = 10000000 #arbitrary large number
        j = 0
        for j in range(len(data)):
            if j != i:
                eu_dist = 0
                k = 1
                for k in range(len(data[0])):
                    eu_dist = eu_dist + math.pow((data[i][k] - data[j][k]), 2) #equation to calculate euclidian distance
                eu_dist = math.sqrt(eu_dist)
                if eu_dist < curr_distance:
                    curr_distance = eu_dist
                    curr_best = j #store the location of the feature
        if data[curr_best][0] == data[i][0]:
            num_correct = num_correct + 1
    accuracy = float(num_correct)/len(data) *100
    return accuracy

def loocv(data, features, x):
    i = 0
    num_correct = 0
    for i in range(len(data)):
        curr_best = 0 #stores the j value that has the smallest distance
        curr_distance = 10000000 #arbitrary large number
        j = 0
        for j in range(len(data)):
            if j != i:
                dist = 0
                k = 0
                if len(features) == 0:
                    dist = 1
                elif len(features) == 1:
                    dist = dist + math.pow(data[i][(features[0])]-data[j][(features[0])], 2)
                else:
                    for k in range(len(features)):
                        dist = dist + math.pow(data[i][(features[k])]-data[j][(features[k])], 2)
                if x == 0:
                    dist = math.sqrt(dist)
                elif dist == 0:
                    pass
                else:
                    dist = dist + math.pow(data[i][x]-data[j][x], 2)
                    dist = math.sqrt(dist)
                if dist < curr_distance:
                    curr_distance = dist
                    curr_best = j #store the location of the feature
        if data[i][0] == data[curr_best][0]:
            num_correct = num_correct + 1
    accuracy = float(num_correct)/len(data) *100
    return accuracy

def forward_elim(data):
    print('beginning forward elimination')
    best_features = []
    features = []
    best_acc = 0
    for i in range(1, len(data)):
        curr_best_acc = 0
        curr_best_feature = 0
        if best_features == []:
            for k in range(1, len(data[0])):
                feature = [k]
                accuracy = loocv(data, feature, 0)
                print('using feature', k, 'accuracy is', accuracy)
                if accuracy > best_acc:
                    best_acc = accuracy
                    best_feature = k
        else:
            for k in range(1, len(data[0])):
                if k not in features:
                    accuracy = loocv(data, features, k)
                    print('using features',features, k, 'accuracy is', accuracy)
                    if accuracy > best_acc:
                        best_acc = accuracy
                        best_feature = k
                    elif accuracy > curr_best_acc:
                        curr_best_acc = accuracy
                        curr_best_feature = k
        if best_feature not in best_features:
            best_features.append(best_feature)
            features.append(best_feature)
        else:
            features.append(curr_best_feature)
    print('finished search best feature subset is', best_features, 'which has an accuracy of', best_acc)

def backward_elim(data):
    print('beginning Backward Elimination')
    best_features = []
    features = []
    best_acc = 1000
    for i in range (1, len(data[0])):
        features.append(i)
    print('using features',features,'accuracy is',knn_loocv(data))
    for j in range(1, len(data)):
        curr_best_acc = best_acc
        curr_worst_acc = 0
        #curr_best_feature = 0
        curr_worst_feature = 0
        for k in range(1, len(data[0])):
            if k in features:
                features.remove(k)
                print('using features',features)
                accuracy = loocv(data, features, 0)
                print('accuracy is', accuracy)
                if accuracy < curr_best_acc:
                    curr_best_acc = accuracy
                    #curr_best_feature = k
                elif accuracy > curr_worst_acc:
                    curr_worst_feature = k
                    curr_worst_acc = accuracy #actually gives curr_best Accuracy because its the accuracy without the worst feature, had difficulty trying to change the names
                    a = []
                    for i in range(0,len(features)):
                        a.append(features[i])
                    best_features.append((a,curr_worst_acc))
                else:
                    pass
                features.append(k)
        if curr_worst_feature in features:
            features.remove(curr_worst_feature)
        best_acc = curr_worst_acc
    best = max(best_features, key=lambda x: x[1])
    print("running the backward elimination algorithm, we get the set and accuracy:", best)

def num_correct_loocv(data, features, x, num):
    i = 0
    num_correct = 0
    num_incorrect = 0
    if num == 0:
        for i in range(len(data)):
            curr_best = 0 #stores the j value that has the smallest distance
            curr_distance = 10000000 #arbitrary large number
            j = 0
            for j in range(len(data)):
                if j != i:
                    dist = 0
                    k = 0
                    if len(features) == 0:
                        dist = 1
                    elif len(features) == 1:
                        dist = dist + math.pow(data[i][(features[0])]-data[j][(features[0])], 2)
                    else:
                        for k in range(len(features)):
                            dist = dist + math.pow(data[i][(features[k])]-data[j][(features[k])], 2)
                    if x == 0:
                        dist = math.sqrt(dist)
                    elif dist == 0:
                        pass
                    else:
                        dist = dist + math.pow(data[i][x]-data[j][x], 2)
                        dist = math.sqrt(dist)
                    if dist < curr_distance:
                        curr_distance = dist
                        curr_best = j #store the location of the feature
            if data[i][0] == data[curr_best][0]:
                num_correct = num_correct + 1
        return num_correct

    else:
        for i in range(len(data)):        
            curr_best = 0 #stores the j value that has the smallest distance
            curr_distance = 10000000 #arbitrary large number
            j = 0
            for j in range(len(data)):
                if j != i:
                    dist = 0
                    k = 0
                    if len(features) == 0:
                        dist = 1
                    elif len(features) == 1:
                        dist = dist + math.pow(data[i][(features[0])]-data[j][(features[0])], 2)
                    else:
                        for k in range(len(features)):
                            dist = dist + math.pow(data[i][(features[k])]-data[j][(features[k])], 2)
                    if x == 0:
                        dist = math.sqrt(dist)
                    elif dist == 0:
                        pass
                    else:
                        dist = dist + math.pow(data[i][x]-data[j][x], 2)
                        dist = math.sqrt(dist)
                    if dist < curr_distance:
                        curr_distance = dist
                        curr_best = j #store the location of the feature
            if data[i][0] == data[curr_best][0]:
                # print(data[i][0])
                # print(data[curr_best][0])
                # print(i, 'next correct')
                num_correct = num_correct + 1
            else:
                num_incorrect = num_incorrect + 1
            if len(data)-num < num_incorrect:
                return 0
    return num_correct

def best_so_far(data):
    print('beginning Shafiqs algorithm')
    best_features = []
    best_acc = 0 #which is the number correct
    for i in range(1, len(data)):
        curr_best_acc = 0
        if best_features == []:
            for k in range(1, len(data[0])):
                feature = [k]
                accuracy = num_correct_loocv(data, feature, 0, best_acc)
                print('using feature', k, 'num correct is', accuracy)
                if accuracy > best_acc:
                    best_acc = accuracy
                    best_feature = k
        else:
            for k in range(1, len(data[0])):
                if k not in best_features:
                    accuracy = num_correct_loocv(data, best_features, k, best_acc)
                    if accuracy != 0:
                        print('using features',best_features, k, 'num correct is', accuracy)
                    if accuracy > best_acc:
                        best_acc = accuracy
                        best_feature = k
                    elif accuracy > curr_best_acc:
                        curr_best_acc = accuracy
        if best_feature not in best_features:
            best_features.append(best_feature)
        else:
           break
    print('finished search best feature subset is', best_features, 'which has an accuracy of', (best_acc/len(data))*100)

print('Welcome to Shafiq Goslas Feature Selection Algorithm.','\n')
f_name = input('Type in the name of the file to test exactly how it appears')

text = open(f_name+".txt", "r")
data = [ ]
for line in text:
    data.append( [float(num) for num in line.strip().split()] )

print('Type the number of the algorithm you want to run')
alg = int(input('1) forward Selection, 2) backward elimination, 3) Shafiqs Special Algorithm'))
if alg == 1:
    print("running nearest neighbor with leave one out evaluation, i get an accuracy of ", knn_loocv(data))
    print(forward_elim(data))
elif alg == 2:
    print("running nearest neighbor with leave one out evaluation, i get an accuracy of ", knn_loocv(data))
    print(backward_elim(data))
elif alg == 3:
    print("running nearest neighbor with leave one out evaluation, i get an accuracy of ", knn_loocv(data))
    print(best_so_far(data))
