MACHINE LEARNING LABORATORY
1817119_JAYANTHI T
✫ EXP 4 : Implementation of Find S Algorithm

Importing the necessary libraries
[ ]
import pandas as pd
import numpy as np
Reading the data in the csv file
[ ]
data = pd.read_csv('weather.csv')
print(data,"n")
      Time Weather Temperature Company Humidity    Wind Goes
0  Morning   Sunny        Warm     Yes     Mild  Strong  Yes
1  Evening   Rainy        Cold      No     Mild  Normal   No
2  Morning   Sunny    Moderate     Yes   Normal  Normal  Yes
3  Evening   Sunny        Cold     Yes     High  Strong  Yes n
Making an array of all the attributes
[ ]
d = np.array(data)[:,:-1]
print("n The attributes are: ",d)
n The attributes are:  [['Morning' 'Sunny' 'Warm' 'Yes' 'Mild' 'Strong']
 ['Evening' 'Rainy' 'Cold' 'No' 'Mild' 'Normal']
 ['Morning' 'Sunny' 'Moderate' 'Yes' 'Normal' 'Normal']
 ['Evening' 'Sunny' 'Cold' 'Yes' 'High' 'Strong']]
Segregating the target that has positive and negative examples
[ ]
target = np.array(data)[:,-1]
print("n The target is: ",target)
n The target is:  ['Yes' 'No' 'Yes' 'Yes']
Training function to implement find-s algorithm
[ ]
def train(c,t):
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            break
             
    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:

Obtaining the final hypothesis
[ ]
print("n The final hypothesis is:",train(d,target))
n The final hypothesis is: ['?' 'Sunny' '?' 'Yes' '?' '?']
