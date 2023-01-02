#!/bin/bash
let j=1
for mode in 0 1 2 3;
do
	sudo nvpmodel -m $mode;

	sudo jetson_clocks;

	sudo jetson_clocks --show ;
	
	let s=1
	for i in 1 3 6 8 10;
	do


		
    	size=$(($i*16))
    	sudo jetson_clocks;
    	python3 py_cuda.py --size $size &
    	#python3 infer.py;

		cd ..
		cd Benchmark-Analysis-of-Lane-detection-models
		python3 ./Hook.py $j $s
		cd ..
		cd scripts_offloading
		s=$(($s+1))
	done	  
	j=$(($j+1))    
#done <all_conf.txt
done 
exit 0
