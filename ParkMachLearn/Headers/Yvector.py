'''
Created on May 1, 2021

@author: fig
'''
parkcon = float()
samplelist = []
finallist = {}
textdoc = open('binReport.txt', 'rt')
#two collums

#one collum of integers from the samples IDs

#one collum of 0.0 or 1.0 for Control and Parkinson's respectfully
for sample in textdoc:
    sample = sample.rstrip('\n')
    runs = sample.split('\t') 
    samplelist.append(runs[0]) 
    if runs[3] == 'parkinsons':
        finallist[runs[0]] = float(1.0)
    elif runs[0] == 'sample':
        finallist[runs[0]] = 'parkinson/control'
    else:
        finallist[runs[0]] = float(0.0)
print(finallist)    
    

if __name__ == '__main__':
    pass