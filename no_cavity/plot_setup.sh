rm path_log
rm population.dat
rm Norm_*.dat
rm P*.dat
#################################################
for i in {1..50}
do
	echo $i
	cd sim_$i
	cd logs
###############################################	
	cp ../../n_atoms .
	cp ../../n_steps .
##############################################
	cp nac.txt nac_extract.txt
	cp corr.txt corr_extract.txt
	cp ex_energy.txt energy_extract.txt
	sed -i "s|S1_S2|#S1_S2|g" nac_extract.txt
	sed '1d' corr_extract.txt > p.dat
	sed '1d' energy_extract.txt > e.dat
	n_lines=$(wc -l < "corr_extract.txt")
	n_steps=$(<n_steps)
        echo "No. of steps = $n_steps"
	echo "n_lines = $n_lines"
################################################	
        if ((n_lines>=n_steps)); then
                cp ../../nac_norm.py .
                python nac_norm.py
#################################################		
                cp ../../extract.sh .
		cp ../../traj_dist.py .
		cp ../../density.py .
		bash extract.sh	
		python traj_dist.py
		python density.py
		pwd >> ../../path_log
		echo "Traj $i done"
                echo "############################"
        else
               echo "Not enough data in trajetory"
        fi

	cd ..
	cd ..
done 
