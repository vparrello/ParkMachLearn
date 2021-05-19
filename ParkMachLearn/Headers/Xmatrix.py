'''
Created on May 1, 2021

@author: fig
'''
parkcon = float()
samplelist = []
finallist = {}
textdoc = open('binReport.txt', 'rt')
binSdoc = open('ParkSBins.tbl', 'rt')
binCdoc = open('ParkCBins.tbl', 'rt')
taxonbins = set()
bindict = {}

#Run numbers in a dictionary with floats for 1 = park and 0 = control
def definedruns(textdoc):
    for sample in textdoc:
        sample = sample.rstrip('\n')
        runs = sample.split('\t') 
        samplelist.append(runs[0]) 
        if runs[3] == 'parkinsons':
            finallist[runs[0]] = '1.0'
        elif runs[0] != 'sample':
            finallist[runs[0]] = '0.0'
#finds all the taxon ids of the bins in both samples and controls
def taxonids(bindoc):
    #breaking apart the lines of the document and cleaning them
    for sample in bindoc:
        sample = sample.rstrip('\n')
        collum = sample.split('\t') 
        #take the last collum and split apart the taxon bin ids
        if collum[0] != 'sample':
            binlines = collum[3]
            binids = binlines.split(', ')
            binset = set()
            #take the bin ids and truncate them at the decimal
            for binid in binids:
                part = binid
                #ignore empty sets
                if binid != '':
                    #put the bin ids as values in a dictionary connected to the sample ids as keys
                    binset.add(part)
                    taxonbins.add(part)                 
            bindict[collum[0]] = binset 
#create a table based on if the taxonids are used by that run            
def unionbinsample():
    with open('Xmatrix', 'x') as outtable:
        #headers
        headerrow = 'sample\t' + '\t'.join(taxonbins) + '\tparkinsons\n'
        outtable.write(headerrow)
        #matching the values in the samples to the values in the collums
        for key in bindict:
            binset = bindict[key]
            #empty list to put the 1s and 0s in
            presencelist = []
            #checks for the headers
            for header in taxonbins:
                #is the header in the current sample's good bins
                if header in binset:
                    presencelist.append('1.0')
                else:
                    presencelist.append('0.0')
            outtable.write(key + '\t' + '\t'.join(presencelist) + '\t' + finallist[key] + '\n') 
        
taxonids(binSdoc)
taxonids(binCdoc)
definedruns(textdoc) 
unionbinsample()       
if __name__ == '__main__':
    pass