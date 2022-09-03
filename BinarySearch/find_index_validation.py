#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:26:31 2022

@author: danielzhu
"""

## Here's the validation function for the binary research



tests = []

## 1st situation is a standard ascending order list

test = {
        'input':{
            'cards' : [1,3,4,5,7,8,9],
            'query' : 7
            },
        'output':4
        }

tests.append(test)

## 2nd situation is an emtry list

test = {
        'input':{
            'cards' : [],
            'query' : 7
            },
        'output':-1
        }

tests.append(test)

## 3rd situation is the query is at the beginning

test = {
        'input':{
            'cards' : [1,2,3,5,7,8,9],
            'query' : 1
            },
        'output':0
        }

tests.append(test)

## 4th situation is the query is at the end

test = {
        'input':{
            'cards' : [1,2,3,5,7,8,9],
            'query' : 9
            },
        'output':6
        }

tests.append(test)

## 5th situation is we got repeated number on the list

test = {
        'input':{
            'cards' : [1,2,2,3,3,3,3,3,3,3,5,7,8,9],
            'query' : 3
            },
        'output':3
        }

tests.append(test)

## 6th situation is the target number is not in the list

test = {
        'input':{
            'cards' : [1,2,4,5,7,8,9],
            'query' : 6
            },
        'output':-1
        }

tests.append(test)

## 6th situation is only one element in the list

test = {
        'input':{
            'cards' : [6],
            'query' : 6
            },
        'output':0
        }

tests.append(test)

    
def evaluation(locate_card):

    

    for i in range(len(tests)):
        print('The {} test is {}'.format(i,locate_card(**tests[i]['input'])==tests[i]['output']))

    pass
    