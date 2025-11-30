Steps for generating polariton plots,

1. python user_input.py
2. bash plot_setup.sh
3. python plot_data.py
4. pyton plot_population.py
5. python plot_nac_hatmap.py


Steps for generating absorption spectrum from terachem output file,

1. Run terachem TDDFT calculation with required number of excited states to cover the desired range of the spectrum
2. python user_input.py   # collect basic input data such as number of excited states
3. bash extract.sh    # Extracts excitation energies and oscillator strengths
4. python absorption.py  # generate absorption spectrum
