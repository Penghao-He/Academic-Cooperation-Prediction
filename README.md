# Cooperation Prediction
## Introduction
This project is to predict how many paper will be published by TWO researchers in the next *t* years if they work together.

## Dataset
The dataset used in this project can be accessed here: [DBLP-Citation-network V10](https://lfs.aminer.cn/lab-datasets/citation/dblp.v10.zip)

## Prerequisites
Before running the main program, make sure you have preprocessed the dataset using "trans.py", 
which turns the abstract of each paper into bag of words.

## Default setting
By default, the dataset we use start from 1980 to 2015 (training set from 1980 to 2009 and testing set from 2010 to 2015). 
Note that we set 6 years as default time interval, and 3 years for features and 3 years for labels within each time interval.

![time interval](https://github.com/Penghao-He/coop_prediction/blob/master/img/interval.jpg)

As shown in the figure above, we will use the data from 1980 to 1982 to predict how many paper will be published by two researchers 
in the next three years if they cooperate with each other. This default setting could be modified in the 'Train test split' section in
main.ipynb.
