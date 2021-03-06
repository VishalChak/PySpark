#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 23:55:46 2017

@author: vishal
"""

def load_PySpark():
    import os
    import sys
    if 'SPARK_HOME' not in os.environ:
        os.environ['SPARK_HOME'] = 'D:/spark-2.1.1-bin-hadoop2.7/bin'
    SPARK_HOME = os.environ['SPARK_HOME']
    sys.path.insert(0,os.path.join(SPARK_HOME,"python"))
    sys.path.insert(0,os.path.join(SPARK_HOME,"python","pyspark"))
    sys.path.insert(0,os.path.join(SPARK_HOME,"python","py4j"))