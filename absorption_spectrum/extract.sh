
n_ex=$(cat n_state)
echo "Number of excited states = $n_ex"
grep 'Final Excited State Results:' -A $((n_ex+3)) output.out | tail -$((n_ex)) | awk '{print $3}' > e.dat
grep 'Final Excited State Results:' -A $((n_ex+3)) output.out | tail -$((n_ex)) | awk '{print $4}' > osc.dat
