
import numpy as np              # linear algebra
import pandas as pd             # data processing
import matplotlib.pyplot as plt # data visualizations

plt.style.use('ggplot')

train_df = pd.read_csv('titanic/train.csv') # load training data
test_df = pd.read_csv('titanic/test.csv')   # load ground truth data

train_cp = train_df.copy() # copy train data
test_cp = test_df.copy()   # copy test data








