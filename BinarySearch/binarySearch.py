#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:35:41 2022

@author: danielzhu
"""

from find_index_validation import evaluation



def locate_card(cards,query):
    lo = 0; hi = len(cards)-1
    while lo<=hi:
        mid = (lo+hi)//2
        if query == cards[mid]:
            while True:
                if cards[mid-1]==query and len(cards)!=1:
                    mid-=1
                else:
                    break
            return(mid)
        if query > cards[mid]:
            lo = mid+1
        if query < cards[mid]:
            hi = mid-1
        
        
    return(-1)
        
    pass



evaluation(locate_card)