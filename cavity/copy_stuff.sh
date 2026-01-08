for i in {1..30}
do	
	echo $i
	cp sim_$i/logs/d_grid.dat .
	cp time.dat sim_$i/logs
done 
