# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

if __name__=="__main__":
    print("Bubble Sort")
    a=[1,3,12,4,13]
    print("Before",a)
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    
    print("After",a)
    
    