rm t.xyz
rm a.dat
rm coord.dat
for i in {1..736}      # add no. of time steps
do
#	echo $i
	j=$((i*12))
	head -$j nuc_geo.xyz > t.xyz
	tail -10 t.xyz >> a.dat
	tail -10  t.xyz | awk {'print  $2, $3, $4'} >> coord.dat
#	echo $j
done 
