#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import rep_transc as rt
import math

def representativeIsLongestAmount(representativesFile, longestFile):
    '''
    Count the number of "representative" sequences that are also the longest
    by checking if the respective sequences in the "representatives.fa" file
    are the same in the "longestTranscripts.fa" file in a simulation directory.
    
    Parameters
    ----------
    representativesFile : string.
        The name of the file with the representative sequences.
        
    longestFile : string.
        The name of the file with the longest sequences.
        
    Returns
    -------
    representativesAlsoLongest : integer.
        The number of representatives that are also the longest sequences.
    '''
    # Making two dictionaries containing the files' respective sequences.
    representatives = rt.makeGeneDictionary(rt.getSequences(representativesFile))
    longest = rt.makeGeneDictionary(rt.getSequences(longestFile))
    
    # make lists of their values.
    representatives = list(representatives.values())
    longest = list(longest.values())
    
    representativesAlsoLongest = 0 # number of representatives that are also the longest.
    for i in range(len(representatives)):
        if representatives[i] == longest[i]:
            representativesAlsoLongest += 1
            
    return representativesAlsoLongest

def gatherRepresentativeIsLongestData(directory):
    '''
    Iterates over the simulation files in "directory".

    Parameters
    ----------
    directory : string.
        The simulation directory.

    Returns
    -------
    values : list of integers.
        A list of integers whose values are the number of cases where there
        is/are:
            1 representative sequences that are also the longest,
            2 representative sequences that are also the longest,
            3 representative sequences that are also the longest,
            ...
            
        respectively. E.g. if there are 5 simulations (with 5 genes each) the
        returned list could look like [0, 0, 1, 1, 3], meaning there is one 
        case where 3 rep. sequences are also the longest, one case where 4 rep.
        sequences are also the longest, and 3 cases where 5 rep. sequences are
        also the longest.
    '''
    nrOfSimulations = 500
    values = [0,0,0,0,0] #length 5 for 5 genes.
    
    for simulationNr in range(1, nrOfSimulations+1):
        simulationString = (len(str(nrOfSimulations)) - len(str(simulationNr)))*'0' + str(simulationNr)
        path = directory + '/_iteration_' + simulationString + '_cds/'
        representativesFile = path + 'representatives.fa'
        longestFile = path + 'longestTranscripts.fa'
        
        index = representativeIsLongestAmount(representativesFile, longestFile)
        values[index-1] += 1
    
    return values

def getRepLongestLengthDifference(representativesFile, longestFile):
    '''
    Calculate the sequence length difference between the representatives and
    the longest sequences of a gene.

    Parameters
    ----------
    representativesFile : string.
        The name of the file with the representative sequences.
        
    longestFile : string.
        The name of the file with the longest sequences.

    Returns
    -------
    differenceList : list of integers.
        A list of the length differences between the representatives and the
        longest sequences of the gene.
    '''
    # Making two dictionaries containing the files' respective sequences.
    representatives = rt.makeGeneDictionary(rt.getSequences(representativesFile))
    longest = rt.makeGeneDictionary(rt.getSequences(longestFile))
    
    # make lists of their values.
    representatives = list(representatives.values())
    longest = list(longest.values())
    
    differenceList = []
    for i in range(len(representatives)):
        difference = abs(len(representatives[i]) - len(longest[i]))
        if difference != 0:
            differenceList.append(difference)
        
    return differenceList

def getRepLongestLengthDiffAvgOverall(directory):
    '''
    Calculates the average length difference between the representatives and
    the longest sequences for the cases where the representatives' MSAs scored
    higher or lower than those of the longest sequences depending on the
    condition in the if-statement (>= or <).

    Parameters
    ----------
    directory : String.
        The name of the simulation directory.

    Returns
    -------
    average : Integer.
    '''
    nrOfSimulations=500
    differencesList = []

    for simulationNr in range(1, nrOfSimulations+1):
        simulationString = (len(str(nrOfSimulations)) - len(str(simulationNr)))*"0" + str(simulationNr)
        path = directory + "/_iteration_" + simulationString + "_cds/"
        representativesFile = path + "representatives.fa"
        longestFile = path + "longestTranscripts.fa"
        
        try:
            sopScoreFile = path + "sop.txt"
            sopScores = getSopScores(sopScoreFile)
            scoreDifference = int(sopScores[0]) - int(sopScores[1])
            
            if scoreDifference < 0:
                differencesList += getRepLongestLengthDifference(representativesFile, longestFile)
                
        except:
            continue #skip simulations where there is no sop.txt file because all of its representatives are also the longest sequences.
    
    average = sum(differencesList) / len(differencesList)        
    return average

def getRepLongestLengthDifferenceAverage(directory):
    '''
    Get the length difference average between the representatives and the 
    longest sequences for each of the 'representatives = longest sequences'
    cases, e.g. one case being the one with one representative that's also the
    gene's longest sequence, another being the one with two representatives, etc.
    It calculates the average for the simulations where the sum-of-pairs score
    of the representatives' MSAs are higher or lower than those of the longest
    sequences depending on the condition in the if-statement (>= or <).

    Parameters
    ----------
    directory : string.
        The name of the simulation directory.

    Returns
    -------
    averageList : list of integers.
        A list of the lenght difference averages of the different cases.
    '''
    nrOfSimulations = 500
    casesList = [[],[],[],[],[]] #5 inner lists for the 5 cases, e.g. one with the 1st is for one representative = longest, the 2nd for two representatives = longest etc.
    
    for simulationNr in range(1, nrOfSimulations+1):
        simulationString = (len(str(nrOfSimulations)) - len(str(simulationNr)))*"0" + str(simulationNr)
        path = directory + "/_iteration_" + simulationString + "_cds/"
        representativesFile = path + "representatives.fa"
        longestFile = path + "longestTranscripts.fa"
        
        try:
            sopScoreFile = path + "sop.txt"
            sopScores = getSopScores(sopScoreFile)
            scoreDifference = int(sopScores[0]) - int(sopScores[1])
            
            if scoreDifference < 0:
                index = representativeIsLongestAmount(representativesFile, longestFile) - 1
                differenceList = getRepLongestLengthDifference(representativesFile, longestFile)
                casesList[index] += differenceList
                
        except:
            continue #skip simulations where there is no sop.txt file because all of its representatives are also the longest sequences.
        
    averageList = []
    for i in range(len(casesList)):
        if len(casesList[i]) != 0:
            average = sum(casesList[i]) / len(casesList[i])
            averageList.append(average)
        else:
            averageList.append(0)
            
    standardDeviations = getStdDeviations(casesList, averageList)
        
    return averageList, standardDeviations


def getSeqLengthDiffAvg(directory):
    '''
    Calculates the average difference in length between the sequences in a
    simulation for each the different cases (amounts) of longest sequences selected as
    representatives in a simulation.

    Parameters
    ----------
    directory : string.
        The name of the simulation directory.

    Returns
    -------
    avgDifferenceList : list of integers.
        A list of the average sequence differences for the different amounts of
        longest sequences selected as representatives in a simulation.
    '''
    nrOfSimulations = 500
    casesList = [[],[],[],[],[]] #5 inner lists for the 5 cases, e.g. one with the 1st is for one representative = longest, the 2nd for two representatives = longest etc.
    
    for simulationNr in range(1, nrOfSimulations+1):
        simulationString = (len(str(nrOfSimulations)) - len(str(simulationNr)))*"0" + str(simulationNr)
        path = directory + "/_iteration_" + simulationString + "_cds/"
        representativesFile = path + "representatives.fa"
        longestFile = path + "longestTranscripts.fa"
        casesListIndex = representativeIsLongestAmount(representativesFile, longestFile) - 1
        
        allSequencesFile = path + "_iteration_" + simulationString + "_cds.fasta"
        sequences = rt.getSequences(allSequencesFile)
        sequenceDict = rt.makeGeneDictionary(sequences)
        sequenceList = list(sequenceDict.values())
        
        for i in range(len(sequenceList)):
            j=i+1
            while j < len(sequenceList):
                difference = abs(len(sequenceList[i]) - len(sequenceList[j]))
                casesList[casesListIndex].append(difference)
                j+=1
        
    avgDifferenceList = []
    for i in range(len(casesList)):
        average = sum(casesList[i]) / len(casesList[i])
        avgDifferenceList.append(average)
        
    return avgDifferenceList

# testing
# a = getSeqLengthDiffAvg("small")
# print(a)
# plt.plot_date([1,2,3,4,5], a)

def getSopScores(f):
    '''
    Get the sum-of-pairs scores from the sop.txt files in the simulations.

    Parameters
    ----------
    f : string.
        The name of the sum-of-pairs score file, e.g. 'sop.txt'

    Returns
    -------
    scores : list of integers.
        A list of the scores.
    '''
    scoreFile = open(f, 'r')
    scores = []
    for line in scoreFile:
        scores.append(line[:-1])
        
    return scores
    

def getAverageScoreDifference(directory):
    '''
    Calculate the sum-of-pairs score difference average for each of the cases
    of representatives being equal to the longest sequences. It calculates the
    average for the simulations where the sum-of-pairs score of the
    representatives' MSAs are higher or lower than those of the longest
    sequences depending on the condition in the if-statement (>= or <).

    Parameters
    ----------
    directory : string.
        The name of the simulation directory.

    Returns
    -------
    averageList : list of integers.
        A list of the average scores for the different cases.
    '''
    nrOfSimulations = 500
    casesList = [[],[],[],[],[]] #5 inner lists for the 5 cases, e.g. one with the 1st is for one representative = longest, the 2nd for two representatives = longest etc.
    
    for simulationNr in range(1, nrOfSimulations+1):
        simulationString = (len(str(nrOfSimulations)) - len(str(simulationNr)))*"0" + str(simulationNr)
        path = directory + "/_iteration_" + simulationString + "_cds/"
        representativesFile = path + "representatives.fa"
        longestFile = path + "longestTranscripts.fa"
        
        try:
            sopScoreFile = path + "sop.txt"
        
            index = representativeIsLongestAmount(representativesFile, longestFile) - 1
            sopScores = getSopScores(sopScoreFile)
            scoreDifference = int(sopScores[0]) - int(sopScores[1])
            
            if scoreDifference < 0:
                casesList[index].append(scoreDifference*(-1))
                
        except:
            continue #skip simulations where there is no sop.txt file because all of its representatives are also the longest sequences.
    
    averageList = []
    for i in range(len(casesList)):
        if len(casesList[i]) != 0:
            average = sum(casesList[i]) / len(casesList[i])
            averageList.append(average)
        else:
            averageList.append(0)
            
    standardDeviations = getStdDeviations(casesList, averageList)
        
    return averageList, standardDeviations


def getStdDeviations(casesList,averageList):
    '''
    Calculates and returns the standard deviations for each case in casesList.

    Parameters
    ----------
    casesList : List of lists of integers.
        A list that contains 5 inner lists, each representing the amount of
        longest sequences selected as representatives in a simulation. An
        inner list must contain values (integer) of some sort for the
        simulations contained within it.
    
    averageList : List of integers.
        A list of averages for each of the inner lists in casesList.

    Returns
    -------
    standardDeviations : List of integers.
        A list of the standard deviations for each of the inner lists in
        casesList.
    '''
    standardDeviations = []
    for case, average in zip(casesList, averageList):
        squaredDeviations = 0
        for value in case:
            squaredDeviations += (value - average)**2
            
        try:
            stdDeviation = math.sqrt(squaredDeviations / len(case))
        except: #catch a 0-division error when a case has no values.
            stdDeviation = 0
            
        standardDeviations.append(stdDeviation)
        
    return standardDeviations

def getAverageScoreDifferenceOverall(directory):
    '''
    Get the average difference of sum-of-pairs scores between the
    representatives' and the longest sequences' respective MSAs of all the
    simulations in the directory. It calculates the
    average for the simulations where the sum-of-pairs score of the
    representatives' MSAs are higher or lower than those of the longest
    sequences depending on the condition in the if-statement (>= or <).

    Parameters
    ----------
    directory : string.
        the name of the simulation directory.

    Returns
    -------
    average : integer.
        The average score difference.
    '''
    nrOfSimulations = 500
    scoreDifferenceList = []
    
    for simulationNr in range(1, nrOfSimulations+1):
        simulationString = (len(str(nrOfSimulations)) - len(str(simulationNr)))*"0" + str(simulationNr)
        path = directory + "/_iteration_" + simulationString + "_cds/"
        
        try:
            sopScores = getSopScores(path + "sop.txt")
            scoreDifference = int(sopScores[0]) - int(sopScores[1])
            
            if scoreDifference < 0: #if the representatives' MSA scored higher than the longest sequences' MSA.
                scoreDifferenceList.append(scoreDifference)
        except:
            continue #skip simulations where there is no sop.txt file because all of its representatives are also the longest sequences.
            
    average = sum(scoreDifferenceList) / len(scoreDifferenceList)
    return average


def main():
    # simulationDirectory = input("Enter the simulation directory: ")
    simulationDirectory = "small"
    
    x = [1,2,3,4,5]
    # y = gatherRepresentativeIsLongestData(simulationDirectory)
    # y, e = getRepLongestLengthDifferenceAverage(simulationDirectory)
    y, e = getAverageScoreDifference(simulationDirectory)
    print(y)
    print(e)
    
    fig, ax = plt.subplots()
    
    # ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    ax.errorbar(x, y, e, linestyle="None", marker="o", ecolor="r")
    
    ax.set(xlim=(0.5,5.5), xticks=list(range(1,6)),
            # ylim=(0,220), yticks=np.arange(0,220,10))
            # ylim=(-10,240), yticks=np.arange(0,250,10))
            ylim=(-1000,10000), yticks=np.arange(0,11000,1000))
            
    # plt.errorbar(x, y, e, linestyle="None", marker="o")
    
    # plt.title('Amount of longest sequences selected\nas representatives in a simulation')
    # plt.title('Average difference in length\nbetween representatives and longest sequences')
    plt.title("Average difference in sum-of-pairs score\nbetween representatives and longest sequences")
    plt.xlabel("Number of longest sequences selected\nas representatives in a simulation")
    # plt.ylabel("Number of simulations")
    # plt.ylabel("Difference in number of symbols")
    plt.ylabel("Difference in points")
    
    # plt.savefig("plot1.png")
    plt.show()
    
# if __name__ == "__main__":
    # main()
