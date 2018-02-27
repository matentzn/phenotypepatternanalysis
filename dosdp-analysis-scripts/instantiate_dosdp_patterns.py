#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:24:37 2018

@author: matentzn
"""

import os
import yaml
import re
import subprocess


dir_patterns = '/ws/upheno/src/patterns'
dir_tsv = '/ws/upheno/src/patterns_tsv'
dir_patterns_owl = '/ws/upheno/src/patterns_owl'
ontology_merged = '/ws/upheno/src/patterns_merged.owl'
dosdp_prefixes = '/ws/upheno/src/patterns/util/prefixes.yaml'

dosdp = '/ws/dosdp-tools/target/universal/stage/bin/dosdp-tools'
robot = "robot"

baseuri = 'http://upheno.com#UPHENO_TEST_'

def merge_patterns_in_single_ontology(directory,ontology_merged,robot):
    params=list()
    params.append(robot)
    params.append("merge")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".owl"): 
            #print(filename)
            f = os.path.join(directory, filename)
            params.append("--input "+str(f))
            continue
        else:
            continue

    params.append("--output")
    params.append(ontology_merged)
    p_str = ' '.join(params)
    os.system(p_str)
    return;
    

def run_dosdp(dir_patterns,dir_tsv, dir_patterns_owl, dosdp, prefixfile):
   ct = 1
   for file in os.listdir(dir_patterns):
        patternfn = os.fsdecode(file)
        if patternfn.endswith(".yaml"): 
            cts = str(ct)
            print("DOSDP: Compiling pattern "+cts+": "+patternfn)
            ct+=1
            tsvfn = re.sub("[.]yaml$",".tsv",patternfn)
            owlfn = re.sub("[.]yaml$",".owl",patternfn)
            fy = os.path.join(dir_patterns, patternfn)
            ft = os.path.join(dir_tsv, tsvfn)
            fo = os.path.join(dir_patterns_owl, owlfn)
            if not os.path.isfile(ft):
                print("TSV does not exist: "+tsvfn)
            try:
                print(subprocess.check_output([dosdp, "generate", "--obo-prefixes=true", "--template="+fy, "--infile="+ft, "--outfile="+fo, "--prefixes="+prefixfile]))
            except subprocess.CalledProcessError as e:
                print("Ping stdout output:\n", e.output)
            continue
        else:
            continue
   return;

def create_tsv_files_with_default_fillers (dir_patterns,dir_tsv, baseuri):
    ct = 1
    
    for file in os.listdir(dir_patterns):
        filename = os.fsdecode(file)
        if filename.endswith(".yaml"): 
            f = os.path.join(dir_patterns, filename)
            with open(f, 'r') as stream:
                try:
                    y = yaml.load(stream)
                    #print(y['equivalentTo']['text'])
                    tsvfn = re.sub("[.]yaml$",".tsv",filename)
                    ct+=1
                    defclass = baseuri+str(ct)
                    header = "defined_class\t"
                    row = defclass+"\t"
                    for v in y['vars']:
                        vs = re.sub("[^0-9a-zA-Z _]","",y['vars'][v])
                        value = y['classes'][vs]
                        header+=v+"\t"
                        row+=value+"\t"
                    fout = os.path.join(dir_tsv, tsvfn)
                    with open(fout, 'w') as the_file:
                        the_file.write(header+'\n'+row+'\n')
                except yaml.YAMLError as exc:
                    print(exc)
            continue
        else:
            continue
    return;
    
   
if not os.path.exists(dir_tsv):
    os.makedirs(dir_tsv)
    
#replace_illegal_characters_in_keys(dir_patterns,dir_patterns_rewritten)
create_tsv_files_with_default_fillers(dir_patterns,dir_tsv, baseuri)
run_dosdp(dir_patterns,dir_tsv,dir_patterns_owl,dosdp,dosdp_prefixes)
merge_patterns_in_single_ontology(dir_patterns_owl,ontology_merged,robot)