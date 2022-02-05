# -*- coding: utf-8 -*-
"""
Objective: a simple program that will be able to select and replace multiple 
values with new data

Key Steps:
1. Open a target file
2. Identify the values that needs to be replaced
3. Have a mapping of old and new values 
4. Replace the the old values with the new values 
5. Create a new file with the replaced values 
6. Have a count of the replaced values 

Sub steps:
1. Have a target file 
2. Have a simple mapping file 
3. Set up a github repository 

"""

import os
import re
import csv
import shutil 
import fileinput

# target file for replacement 
class tar_file:
    def __init__(self, cwd, fname, in_, out_):
        self.cwd    = cwd
        self.fname  = fname
        self.in_    = in_
        self.pti    = cwd+'/'+in_+'/'+fname
        self.out_   = out_ 
        self.pto    = cwd+'/'+out_+'/'+fname 
        self.pta    = cwd+'/'+out_+'/'+'search_count_'+fname      

    def search_count(self, search):
        s_count = {} 
        
        with open(self.pti , 'r') as file:
            for line in file:
                for part in re.split('[ ,();\n\']', line.upper()):
                    if any(word == part for word in search):
                        if bool(s_count.get(part)) == False:
                            s_count[part] = 1
                        else:
                            s_count[part] += 1
                            
        with open(self.pta, 'w') as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(['Object', 'Count'])
            for k, v in s_count.items():
                writer.writerow([k,v])
            
        print('Search words and count saved to {pta}'.format(pta=self.pta))         
        
# mapping attributes 
class map_file:
    def __init__(self, cwd, fname, in_):
        self.cwd   = cwd
        self.fname = fname
        self.in_   = in_
        self.pti   = cwd+'/'+in_+'/'+fname



        
    def map_to_dict(self):
        mt = {} 
        with open(self.pti, 'r') as table:
            for line in table:
                x , y = line.split(',')
                mt[x] = y.strip('\n') 
        return mt 

def tex_rep(f_in, map_): # f_inshould be a class 
    shutil.copy(f_in.pti, f_in.out_)
    for key in map_:
        with fileinput.FileInput(f_in.pto, inplace=True, backup='.bak') as file:
            for line in file:
                i_key = re.compile(re.escape(key), re.IGNORECASE)
                print(i_key.sub(map_[key], line), end='')
    

######### Calls ###############################################################
        
cwd = os.getcwd() 
p = tar_file(cwd, 'PALLADIUM.txt', 'Infile', 'Outfile' )        
m = map_file(cwd, 'replacement.txt', 'Infile' )        
search = ['WANG', 'CHINA'] 
##test
