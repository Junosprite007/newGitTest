#!/usr/bin/env python

import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-n','--name',help='Please Enter Your Name',required=True)
parser.add_argument('-num','--number',help='Please Enter a number',required=True)
args=parser.parse_args()

print('Hello %s\n' %(args.name)*int(args.number))

