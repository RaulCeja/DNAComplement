# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:04:39 2018
takes a dna string and returns its complement
@author: Dr.C
"""
def dnaComplement():
    file=open(r"C:\Users\Dr.C\OneDrive\Documents\BioinformaticsProjects\DNAComplement\rosalind_revc.txt","r")
    dna=file.read()
    dnaComp=""
    for i in dna:
        if i=='A':
            dnaComp='T'+dnaComp
        elif i=='T':
            dnaComp='A'+dnaComp
        elif i=='C':
            dnaComp='G'+dnaComp
        elif i=='G':
            dnaComp='C'+dnaComp
    return dnaComp#[::-1] reversed it back

            
