#!/bin/bash
# Hadoop stream jar
STREAMJAR=/opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar
# input file
INPUT=../dataset/ratings.dat
# input directory
INPUT_DIR=/input
# output file
OUTPUT=result.dat
# output directory
OUTPUT_DIR_A=/output1
OUTPUT_DIR_B=/output2
OUTPUT_DIR_C=/output3
# mapper file
MAPPERA=../pre-process/mapper.py
MAPPERB=../item-pairing/mapper.py
MAPPERC=../recommend/mapper.py
# reducer file
REDUCERA=../pre-process/reducer.py
REDUCERB=../item-pairing/reducer.py
REDUCERC=../recommend/reducer.py
# create input directory on hdfs
hdfs dfs -mkdir /input
# upload input file to input directory
hdfs dfs -put $INPUT $INPUT_DIR
# remove old output directory
hdfs dfs -rm -r -f $OUTPUT_DIR
# execute map-reduce with Hadoop stream jar
hadoop jar $STREAMJAR -files $MAPPERA,$REDUCERA -mapper $MAPPERA -reducer $REDUCERA -input $INPUT_DIR -output $OUTPUT_DIR_A
hadoop jar $STREAMJAR -files $MAPPERB,$REDUCERB -mapper $MAPPERB -reducer $REDUCERB -input $OUTPUT_DIR_A -output $OUTPUT_DIR_B
hadoop jar $STREAMJAR -files $MAPPERC,$REDUCERC -mapper $MAPPERC -reducer $REDUCERC -input $OUTPUT_DIR_B -output $OUTPUT_DIR_C
hdfs dfs -cat $OUTPUT_DIR/part* $OUTPUT
