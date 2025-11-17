rm path_log
rm population.dat
rm Norm_*.dat
rm P*.dat
for i in {21..30}
do
	echo $i
	cd sim_$i
	cd logs
	cp ../../n_atoms .
	cp ../../n_steps .
	cp nac.txt nac_extract.txt
	cp corr.txt corr_extract.txt
	sed -i "s|S1_S2|#S1_S2|g" nac_extract.txt
	sed '1d' corr_extract.txt > p.dat
	n_lines=$(wc -l < "corr_extract.txt")
        if ((n_lines>=n_steps)); then
                cp ../../nac_norm.py .
                python nac_norm.py
                pwd >> ../../path_log

        else
               echo "Not enough data in trajetory"
       fi

	cd ..
	cd ..
done 
