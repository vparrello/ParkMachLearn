'''
Created on Jun 5, 2021

@author: fig
'''
#creates a list of bins in the doc

def BinsList (infilename, outfilename):
    binset = set()
    with open(infilename, 'rt') as binsdoc:
        line = next(binsdoc)
        for line in binsdoc:
            line = line.rstrip('\n')
            collumn = line.split('\t')
            bins = collumn[3].split(', ')
            for binning in bins:
                binset.add(binning)
    with open(outfilename, 'w') as outtable:
        outtable.write('genome_id' + '\n')
        for binning in binset:
            if binning != '':
                outtable.write(binning + '\n')

BinsList('ParkSBins.tbl', 'ParkSGenomeBins.tbl')
BinsList('ParkCBins.tbl', 'ParkCGenomeBins.tbl')