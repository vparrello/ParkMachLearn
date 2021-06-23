'''
Created on Jun 23, 2021

@author: fig
'''

#creates co-occurence value for each repgen set in the samples. 

def readheader(inputfile):
    """Reads the header of the file and returns an array of repgen ids."""
    header = next(inputfile)
    row = header.rstrip('\n')
    column = row.split('\t')
    repgens = column[1: -1]
    return repgens

def emptydict(repgenarray):
    """Creates an empty set as a value in a dictionary for each of the repgenids as keys."""
    empdict = {}
    for genomes in repgenarray:
        empdict[genomes] = set()
    return empdict

def fillset(inputfile, repgenarray, dictpark, dictcont):
    """Fills the empty sets in the dictionaries for parkinsons and controls with the samples where they are present. """
    for row in inputfile:
        row = row.rstrip('\n')
        column = row.split('\t')
        if column[-1] == '1.0':
            for i in range(0, len(repgenarray)):
                if column[i+1] == '1.0':
                    dictpark[repgenarray[i]].append(column[0])
        else:
            for i in range(0, len(repgenarray)):
                if column[i+1] == '1.0':
                    dictcont[repgenarray[i]].append(column[0])
            
def occurencevalues(repgenarray, dictpark, dictcont, outfile):
    """Computes the occurence values for each repgenid."""
    headerrow = 'genome1\t' + 'genome2\t' + 'Parkinsons Occurrence\t' + 'Control Occurrence\n'
    outfile.write(headerrow)
    for i in range(0, len(repgenarray)):
        repgeni = repgenarray[i]
        setipark = dictpark[repgeni]
        seticont = dictcont[repgeni]
        for j in range(i+1, len(repgenarray)):
            repgenj = repgenarray[j]
            setjpark = dictpark[repgenj]
            setjcont = dictcont[repgenj]
            intpark = setipark.intersection(setjpark)
            intcont = seticont.intersection(setjcont)
            copark = len(intpark)* 200.0 / (len(setipark) + len(setjpark))
            cocont = len(intcont)* 200.0 / (len(seticont) + len(setjcont))
            if copark >= 50.0 or cocont >= 50.0:
                outfile.write(f"{repgeni}\t {repgenj}\t {copark}\t {cocont}\n")

with open('data.tbl') as inputs:
    repgenarray = readheader(inputs)
    repgenspark = emptydict(repgenarray)
    repgenscont = emptydict(repgenarray)
    fillset(inputs, repgenarray, repgenspark, repgenscont)
with open('CoOccurence.tbl', 'w') as outfile:
    occurencevalues(repgenarray, repgenspark, repgenscont, outfile)