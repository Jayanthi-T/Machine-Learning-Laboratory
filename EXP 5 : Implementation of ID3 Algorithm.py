MACHINE LEARNING LABORATORY
1817119_JAYANTHI T
✫ EXP 5 : Implementation of ID3 Algorithm
[ ]
import pandas as pd
import math
import numpy as np
data = pd.read_csv("3-dataset.csv")
features = [feat for feat in data]
features.remove("answer")

class Node:

    def __init__(self):

outlook
	overcast ->  ['yes']

	rain
		wind
			strong ->  ['no']

			weak ->  ['yes']

	sunny
		humidity
			high ->  ['no']

			normal ->  ['yes']
