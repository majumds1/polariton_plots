rm path_log
rm population.dat
rm Norm_*.dat
rm P*.dat
for i in {21..30}
do
	echo $i
	cd sim_$i
	cd logs
	cp nac.txt nac_extract.txt
	cp corr.txt corr_extract.txt
	sed -i "s|S0_S1|#S0_S1|g" nac_extract.txt
	sed '1d' corr_extract.txt > p.dat
	cp ../../nac_norm.py .
	python nac_norm.py 
	pwd >> ../../path_log		
	cd ..
	cd ..
done 
