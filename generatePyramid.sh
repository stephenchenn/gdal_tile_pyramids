#!/bin/bash

# set variables
num_repetitions=79

# loop through command 80 times
for i in $(seq 0 $num_repetitions); do
    input_file="input${i}.png"
    output_dir="dir${i}"
    gdal_retile.py -v -r bilinear -levels 4 -ps 2048 2048 -co "TILED=YES" -targetDir $output_dir $input_file
done