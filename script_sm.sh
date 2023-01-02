for i in $(seq 1 10);
do

    size=$(($i*8))
    sudo jetson_clocks;
    python3 py_cuda.py --size $size &
    #python3 infer.py;
    



    cd ..
	cd Benchmark-Analysis-of-Lane-detection-models ;
	python3 ./Hook.py 'resnet50_resa' ;
	cd ..
	cd scripts_offloading

    sleep 1;

    sudo pkill -9 python3 ;

    sleep 1;

done

sudo pkill -9 python3;

exit 0
