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
    
    # convert them into lists.
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

def main():
    simulationDirectory = input("Enter the simulation directory: ")
    
    x = [1,2,3,4,5]
    y = gatherRepresentativeIsLongestData(simulationDirectory)
    
    fig, ax = plt.subplots()
    
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    
    ax.set(xlim=(0.5,5.5), xticks=list(range(1,6)),
            ylim=(0,220), yticks=np.arange(10,210,10))
    
    plt.xlabel("Number of representative transcripts that are also the longest")
    plt.ylabel("Number of simulations")
    
    plt.savefig("plot1.png")
    plt.show()
    
if __name__ == "__main__":
    main()