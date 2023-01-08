import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

#Set random seet
np.random.seed(42)

#Create dummy data
dummy_data={
    'defects':np.random.randint(0,5,10).tolist(), #10 Random Integers between 0 and 5
    'group_size':np.repeat(10,10).tolist() #10 Arrays of size 10
}

#Convert data to data frame
data_frame = pd.DataFrame(dummy_data)

#Plot c-chart
plt.figure(figsize=(15,7.5))
plt.plot(
    data_frame['defects'],
    linestyle='-',
    marker='o',
    color='black')

plt.axhline(
    statistics.mean(
        data_frame['defects']) + 3 * np.sqrt(statistics.mean(data_frame['defects'])),
        color='red',
        linestyle='dashed'
)

plt.axhline(
    statistics.mean(
        data_frame['defects']) - 3 * np.sqrt(statistics.mean(data_frame['defects'])),
        color='red',
        linestyle='dashed'
)

plt.axhline(
    statistics.mean(
        data_frame['defects']),
        color='blue'
)

plt.ylim(bottom=0)

plt.title('c Chart')
plt.xlabel('Group')
plt.ylabel('Defect Count')

#Validate points out of control limits

i = 0
control = True

positive_average = statistics.mean(data_frame['defects']) + 3 * np.sqrt(statistics.mean(data_frame['defects']))
negative_average = statistics.mean(data_frame['defects']) - 3 * np.sqrt(statistics.mean(data_frame['defects']))

for group in data_frame['defects']:
    if group > positive_average or group < negative_average:
        print(f'Group {i} out of defects control limits!')
        control = False
    i += 1

if control == True:
    print('All points within control limits.')

plt.show()