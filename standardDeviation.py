from os import stat
import pandas as pd
import plotly.figure_factory as pf
import statistics
import plotly.graph_objects as go
import random

df = pd.read_csv('medium_data.csv')
clapList = df['claps'].to_list()

mean = statistics.mean(clapList)
sd = statistics.stdev(clapList)

graph = pf.create_distplot([clapList], ['Temp'], show_hist= False)
graph.add_trace(go.Scatter(x = [mean,sd], y = [0,0.1], 
    mode = "lines", name = "Claps Mean"))
#graph.show()

print("Mean: ", mean)
print("St Dev: ", sd)


def getSample(count):
    sampleData = []
    for i in range(0,count):
        index = random.randint(0, len(clapList)-1)
        value = clapList[index]
        sampleData.append(value)
    
    sampleMean = statistics.mean(sampleData)
    #sampleSD = statistics.stdev(sampleData)
    return sampleMean

meanList = []
for i in range(0,100):
    randomMean = getSample(30)
    meanList.append(randomMean)

meanOfMeans = statistics.mean(meanList)
sdOfMeans = statistics.stdev(meanList)


graph = pf.create_distplot([meanList], ['Mean Data'], show_hist= False)
graph.add_trace(go.Scatter(x = [meanOfMeans,meanOfMeans], y = [0,0.01], 
    mode = "lines", name = "Claps Mean"))
graph.show()

#Mean remains almost the same in the sample data
print('Mean of Means: ', meanOfMeans)
#new SD becomes 1/10th of the orignal sd
print('SD of Means  ', sdOfMeans)
