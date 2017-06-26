# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:59:34 2017

@author: 10639497
"""
from __future__ import print_function


from pyspark.sql import SparkSession

session = SparkSession.builder.appName("Test").getOrCreate()