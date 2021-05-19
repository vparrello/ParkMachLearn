'''
Created on May 1, 2021

@author: fig
'''
row = int()
samplelist = []
textdoc = open('binReport.txt', 'rt')

#we want a list of each sample name
for sample in textdoc:
    list = sample.split('\t')  
    samplelist.append(list[0]) 
print(samplelist)    
#we want a list of integers to match the number of samples
#for SRR in sample:
#    enumerate(SRR, 0)
#    print("{}    {}" .format(int, SRR))


if __name__ == '__main__':
    pass