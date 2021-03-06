'''
Created on May 1, 2021

@author: fig
'''
parkcon = float()
samplelist = []
finallist = {}
taxonbins = set()
bindict = {}
conversion = {}

#create a dictionary connecting genomeids to repgenids
def repgendict(filename):
    #open the file
    with open(filename, 'rt') as repgendoc:
        for line in repgendoc:
            line = line.rstrip('\n')
            repgen = line.split('\t')
            #first column is the genomes and the third column is the repgenset
            #take the genome and make it a key for the repgen value in the dictionary
            conversion[repgen[0]] = repgen[2]
#Run numbers in a dictionary with floats for 1 = park and 0 = control
def definedruns(filename, kind):
    #opens file
    with open(filename,'rt') as textdoc:
        #runs through the runs and strips each line and separates by tabs
        for sample in textdoc:
            sample = sample.rstrip('\n')
            runs = sample.split('\t') 
            #creates the keys for the dictionary as the ERR#s
            samplelist.append(runs[0]) 
            #checking for the header first 
            if runs[0] != 'sample':
                #Defines parkinsons or control based on the file type
                finallist[runs[0]] = kind
#finds all the taxon ids of the bins in both samples and controls
def taxonids(filename):
    #open the file!
    with open(filename, 'rt') as bindoc:
        #breaking apart the lines of the document and cleaning them
        for sample in bindoc:
            sample = sample.rstrip('\n')
            collum = sample.split('\t') 
            #take the last collum and split apart the taxon bin ids
            if collum[0] != 'sample':
                binlines = collum[3]
                binids = binlines.split(', ')
                binset = set()
                #take the bin ids 
                for binid in binids:
                    #ignore empty sets
                    if binid != '':
                        repgenid = conversion[binid]
                        #put the bin ids as values in a dictionary connected to the sample ids as keys
                        binset.add(repgenid)
                        taxonbins.add(repgenid)                 
                bindict[collum[0]] = binset 
#create a table based on if the taxonids are used by that run            
def unionbinsample():
    with open('Xmatrix', 'w') as outtable:
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

definedruns('ParkCbins.tbl', '0.0') 
definedruns('ParkSbins.tbl', '1.0')
repgendict('bindict.tbl')         
taxonids('ParkSbins.tbl')
taxonids('ParkCbins.tbl')
unionbinsample()       
if __name__ == '__main__':
    pass