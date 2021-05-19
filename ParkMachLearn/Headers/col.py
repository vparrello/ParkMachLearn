'''
Created on May 1, 2021

@author: fig
'''

collumn = int()
genomelist = []
textdoc = open('binReport.txt', 'rt') 



#we want a list of integers to match the number of genomes


#we want a list of each genome bin
def taxid():
    #I want the tax id to be truncated at the decimal
    for genome in textdoc:
        genome = genome.rstrip('.')
        genome.append(genomelist)
    print()
        
#Create a set of dictionaries to match integers with their genomes

if __name__ == '__main__':
    pass