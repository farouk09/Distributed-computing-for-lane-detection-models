for mode in 0 1 2 3
do
print $mode
done


"""
while IFS=' ' read -r c g e;
do
	echo ''$c'_'$g'_'$e'';
	
	python3 config_generator.py --cpu-freq $c --gpu-freq $g --emc-freq $e;

	sudo rm /etc/nvpmodel.conf;

	sudo cp nvpmodel.conf /etc/;
	"""