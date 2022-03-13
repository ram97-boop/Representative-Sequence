#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import rep_transc as rt

def representativeIsLongestAmount(representativesFile, longestFile):
    '''
    Count the number of "representative" sequences that are also the longest
    by checking if the respective sequences in the "representatives.fa" file
    are the same in the "longestTranscripts.fa" file in a simulation directory.
    
    Parameters
    ----------
    representativesFile : (str)
        The name of the file with the representative sequences.
        
    longestFile : (str)
        The name of the file with the longest sequences.
        
    Returns
    -------
    representativesAlsoLongest : (int)
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
    directory : (str)
        The simulation directory.

    Returns
    -------
    values : (list)
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
    representativesFile : (str)
        The name of the file with the representative sequences.
        
    longestFile : (str)
        The name of the file with the longest sequences.

    Returns
    -------
    differenceList : (list)
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

def getRepLongestLengthDifferenceAverage(directory):
    '''
    Get the length difference average between the representatives and the 
    longest sequences for each of the 'representatives = longest sequences'
    cases, e.g. one case being the one with one representative that's also the
    gene's longest sequence, another being the one with two representatives, etc.

    Parameters
    ----------
    directory : (str)
        The name of the simulation directory.

    Returns
    -------
    averageList : (list)
        A list of the lenght difference averages of the different cases.
    '''
    nrOfSimulations = 500
    casesList = [[],[],[],[],[]] #5 inner lists for the 5 cases, e.g. one with the 1st is for one representative = longest, the 2nd for two representatives = longest etc.
    
    for simulationNr in range(1, nrOfSimulations+1):
        simulationString = (len(str(nrOfSimulations)) - len(str(simulationNr)))*"0" + str(simulationNr)
        path = directory + "/_iteration_" + simulationString + "_cds/"
        representativesFile = path + "representatives.fa"
        longestFile = path + "longestTranscripts.fa"
        
        index = representativeIsLongestAmount(representativesFile, longestFile) - 1
        differenceList = getRepLongestLengthDifference(representativesFile, longestFile)
        casesList[index] += differenceList
        
    averageList = []
    for i in range(len(casesList)):
        if len(casesList[i]) != 0:
            average = sum(casesList[i]) / len(casesList[i])
            averageList.append(average)
        else:
            averageList.append(0)
        
    return averageList

def getSeqLengthDiffAvg(directory):
    nrOfSimulations = 500
    casesList = [[],[],[],[],[]] #5 inner lists for the 5 cases, e.g. one with the 1st is for one representative = longest, the 2nd for two representatives = longest etc.
    
    for simulationNr in range(1, nrOfSimulations+1):
        simulationString = (len(str(nrOfSimulations)) - len(str(simulationNr)))*"0" + str(simulationNr)
        path = directory + "/_iteration_" + simulationString + "_cds/"
        representativesFile = path + "representatives.fa"
        longestFile = path + "longestTranscripts.fa"
        casesListIndex = representativeIsLongestAmount(representativesFile, longestFile) - 1
        
        allSequencesFile = path + "_iteration_" + simulationString + "cds.fasta"
        sequences = rt.getSequences(allSequencesFile)
        sequenceDict = rt.makeGeneDictionary(sequences)
        sequenceList = list(sequenceDict.values())
        
        for i in range(len(sequenceList)):
            j=i+1
            while j < len(sequenceList):
                difference = abs(sequenceList[i] - sequenceList[j])
                casesList[casesListIndex].append(difference)
                
    for

def getSopScores(f):
    '''
    Get the sum-of-pairs scores from the sop.txt files in the simulations.

    Parameters
    ----------
    f : (str)
        The name of the sum-of-pairs score file, e.g. 'sop.txt'

    Returns
    -------
    scores : (list)
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
    of representatives being equal to the longest sequences.

    Parameters
    ----------
    directory : (str)
        The name of the simulation directory.

    Returns
    -------
    averageList : (list)
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
            
            if scoreDifference >= 0:
                casesList[index].append(scoreDifference*(1))
                
        except:
            continue #skip simulations where there is no sop.txt file because all of its representatives are also the longest sequences.
    
    averageList = []
    for i in range(len(casesList)):
        if len(casesList[i]) != 0:
            average = sum(casesList[i]) / len(casesList[i])
            averageList.append(average)
        else:
            averageList.append(0)
        
    return averageList

def getAverageScoreDifferenceOverall(directory):
    '''
    Get the average difference of sum-of-pairs scores between the
    representatives' and the longest sequences' respective MSAs of all the
    simulations in the directory.

    Parameters
    ----------
    directory : (str)
        the name of the simulation directory.

    Returns
    -------
    average : (int)
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
    y = gatherRepresentativeIsLongestData(simulationDirectory)
    # y = getRepLongestLengthDifferenceAverage(simulationDirectory)
    # y = getAverageScoreDifference(simulationDirectory)
    print(y)
    
    fig, ax = plt.subplots()
    
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    
    ax.set(xlim=(0.5,5.5), xticks=list(range(1,6)),
            ylim=(0,220), yticks=np.arange(0,220,10))
            # ylim=(0,200), yticks=np.arange(0,200,10))
            # ylim=(0,9500), yticks=np.arange(0,9100,1000))
    
    plt.title('Amount of longest sequences selected\nas representatives in a simulation')
    # plt.title('Average difference in length\nbetween representatives and longest sequences')
    # plt.title("Average difference in sum-of-pairs score\nbetween representatives and longest sequences")
    plt.xlabel("Number of longest sequences selected\nas representatives in a simulation")
    plt.ylabel("Number of simulations")
    # plt.ylabel("Difference in number of symbols")
    # plt.ylabel("Difference in points")
    
    # plt.savefig("plot1.png")
    plt.show()
    
if __name__ == "__main__":
    main()
