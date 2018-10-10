import numpy as np
import pandas as pd
import math
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
data = pd.read_csv("hcluster.csv")
dataset={}
choice=0;                  
for index, row in data.iterrows():
    dataset[row["Document"]]=(row["Term1"], row["Term2"], row["Term3"])

def distance(key,key2):
    global choice;
    summ=0
    s=np.empty(len(key)*len(key2))
    k=0;
    for p1 in key:
        for p2 in key2:
            summ=0;
            if(p1==p2):
                summ=0;
            else:
                for i in range(len(dataset[p1])):
                    summ+=math.pow((dataset[p2][i]-dataset[p1][i]),2);
                summ=math.sqrt(summ);
            s[k]=summ;
            k+=1;
    if(choice==1):
        return min(s);
    elif(choice==2):
        if(min(s)==0):
            return 0;
        av=0;
        for i in s:
            av+=i;
        av=av/len(s);
        return av;
    else:
        if(min(s)==0):
            return 0;
        else:
            return max(s);

def hcluster():
    global choice;
    choice=int(input('1) Single\n2) Average\n3) Complete\nEnter choice: '));
    c=[[i] for i in dataset.keys()]
    print('Initial Clusters: ',c,'\n')
    count=0;
    while(len(c)>2):
        i=0;
        x=np.empty([len(c),len(c)])
        for key1 in c:
            j=0;
            for key2 in c:
                x[i][j]=distance(key1,key2)
                j+=1;
            i+=1;
        minimum=min([min(y for y in r if y>0) for r in x])
        print('Distance Matrix: \n',x,'\n')
        t1,t2 = np.where(x==np.min(x[np.nonzero(x)]))
        c2=[]
        for i in range(len(c)):
            if i==min(t1):
                for o in c[max(t1)]:
                    c[i].append(o);
                c2.append(c[i]);
            elif i==max(t1):
                continue;
            else:
                c2.append(c[i]);
        c=c2;
        count+=1;
        print('Cluster after iteration ',count,': ',c,'\n')
    print('Final Cluster: ',c);
    X=data.values;
    X=X[:,1:]
    if(choice==1):
        linked = linkage(X, 'single');
    elif(choice==2):
        linked = linkage(X, 'average');
    else:
        linked = linkage(X, 'complete')
    labelList = range(1, 7)
    plt.figure(figsize=(10, 7))  
    dendrogram(linked,  
                orientation='top',
                labels=labelList,
                distance_sort='descending',
                show_leaf_counts=True)
    plt.show()
    plt.close('all')

hcluster()


