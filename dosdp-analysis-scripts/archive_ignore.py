#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:59:04 2018

@author: matentzn
"""

def replace_illegal_characters_in_keys(directory, targetdir):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".yaml"): 
            #print(filename)
            f = os.path.join(directory, filename)
            fout = os.path.join(targetdir, filename)
           # y = ruamel.yaml.round_trip_load(f)
            f = os.path.join(directory, filename)
            with open(f, 'r') as stream:
                yml = ruamel.yaml.YAML(typ='safe')
                y = yml.load(stream)            
            for t in ["def","name","equivalentTo"]:
                params = list()
                for v in y[t]['vars']:
                   #print(v)
                   vs = re.sub("[^0-9a-zA-Z _]","",v)
                   vs = re.sub("[ ]","_",vs)
                   if vs!=v:
                       print(filename)
                   params.append(vs)
                y[t]['vars']=params
            
            params = dict()
            for k in y['vars']:
                vs = y['vars'][k]
                ks = re.sub("[^0-9a-zA-Z _]","",k)
                ks = re.sub("[ ]","_",k)
                params[ks] = vs
            y['vars']=params
            with open(fout, 'w') as the_file:
                ruamel.yaml.round_trip_dump(y, the_file)
            continue
        else:
            continue
    return;