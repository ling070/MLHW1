import pandas as pd
import numpy as np
if __name__ == '__main__':
    # You should not modify this part.
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                        default='training_data.csv',
                        help='input training data file name')
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
    # The following part is an example.
    # You can modify it at will.
    training_data = pd.read_csv(args.training, sep=',', names=[
                                'Open', 'High', 'Low', 'Close'])


training_data.isnull().sum()
training_data = training_data.dropna()

testing_data = pd.read_csv(args.testing, sep=',', names=[
    'Open', 'High', 'Low', 'Close'])
testing_data = testing_data.iloc[:-1].copy()
prediction = []
action = [0] * len(testing_data)
for i in range(0, len(testing_data)):
    # daily = testing_data.loc[i]
    if i < 2:
        dailypredit = 0
        prediction.append(dailypredit)
    else:
        avgclose = (testing_data['Close'][i]+testing_data['Close']
                    [i-2]+testing_data['Close'][i-1])/3
        if (testing_data['Close'][i] < avgclose):
            dailypredit = 1
            prediction.append(dailypredit)
        else:
            dailypredit = -1
            prediction.append(dailypredit)

# print(prediction)
i = 0
for i in range(len(prediction)):
    if (prediction[i]+sum(action) >= -1 and prediction[i]+sum(action) <= 1):
        action[i] = prediction[i]
    else:
        prediction[i] = 0
        action[i] = prediction[i]


# 寫檔案
with open(args.output, 'w') as f:
    for a in range(len(action)):
        if (a != len(action)-1):
            f.write(str(action[a])+'\n')
        else:
            f.write(str(action[a]))
