"""
This program loads the predictions from the pickle file.
After setting the start and end index, it plots the probability curve.
To execute this set the required start and end index. Accepted Range 29160498 to 29162498.
This is a sample prediction data file and the full file is available on request.
"""


import pickle
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class PlotProbCuves:

    def __init__(self,startIndex,endIndex,fullFilePath,outputFileName):
        self.stInd = startIndex
        self.endInd = endIndex
        self.filePath = fullFilePath
        self.outputFile = outputFileName

    def loadJsonFile(self):
        self.predictionDictionary = pickle.load(open(self.filePath,'rb'))

    def plotCurve(self):
        keyList=[]
        class0Prob=[]
        class1Prob=[]
        class2Prob=[]
        class3Prob=[]
        class4Prob=[]
        roundCount=0
        labelPredictions={}
        for key in range(self.stInd-1, self.endInd+1):
            if key not in self.predictionDictionary:
                continue
            keyList.append(key)
            class0Prob.append(self.predictionDictionary[key][0][0][0])
            class1Prob.append(self.predictionDictionary[key][0][0][1])
            class2Prob.append(self.predictionDictionary[key][0][0][2])
            class3Prob.append(self.predictionDictionary[key][0][0][3])
            class4Prob.append(self.predictionDictionary[key][0][0][4])
            classLabel=np.argmax(self.predictionDictionary[key][0][0])
        fig = plt.figure(figsize=(11,8))
        ax1 = fig.add_subplot(111)
        plt.xticks(rotation=90)
        ax1.plot(keyList, class0Prob, label='Correct Match', color='c')#, marker='o')
        ax1.plot(keyList, class1Prob, label='Correct Gap', color='g')#, marker='o')
        ax1.plot(keyList, class2Prob, label='Overalignment', color='r')#, marker='o')
        ax1.plot(keyList, class3Prob, label='Underalignment', color='b')#, marker='o')
        ax1.plot(keyList, class4Prob, label='Misalignment', color='y')#, marker='o')
        plt.xticks(np.arange(min(keyList),max(keyList)+1,len(keyList)/15))
        plt.xlabel('Human Index Position')
        plt.ylabel('Probability')
        ax1.legend(loc=2)
        print "Saving file to",self.outputFile
        plt.savefig(self.outputFile)

if __name__=="__main__":    
    startIndex = 29160498
    endIndex = 29162498
    filePath = "predictionsSampleData.p"
    outputFileName = "plot.png"
    obj = PlotProbCuves(startIndex,endIndex,filePath,outputFileName)
    print "Start load of data file."
    obj.loadJsonFile()
    print "Start plotting curve"
    obj.plotCurve()
