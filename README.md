## README

> AUTHOR: 章雨婷
>
> STUDENT ID: 3170102582



### FOLDER CONSTRUCTION

There are two copies of the code. One is the test data extracted from the data set on day 8, and the other is the main algorithm.

The algorithm contains two folders：

* attack - the pattern

  * xxx_extract
    * xxx_process: initial
    * relate_xxx: set the number of events
    * encode: encode the vector to describe events
    * cluster: t-SNE and GMM and DRAW
    * ……

  * ……

Extract the main attack pattern characteristics from the underlying data set

* attack - predict

  * xxx_8th
    * xxx_feature: extract feature from initial data
    * xxx_predict: encode the feature and get the attack mode
    * get auth event & auth_attack: list events from auth related with xxx
    * ……

  * ……  * 

Based on the characteristics of the attack pattern, the data of day 8 was predicted





### DATA 

TIPS: since the data set is too large, there is no attachment. Download the link:

Dataset contains data for key steps:

* Features extracted from proc (8 classes) ：attack_pattern_proc

* Common port number extracted from the flows：portlist.txt

* The data that has been successfully predicted by the proc：proc.txt

* Data in the forecast data that is predicted by flows successfully：flows.txt