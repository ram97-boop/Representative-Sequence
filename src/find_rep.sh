# This shell script is for creating a file containing the
# genes' representative sequences in a simulation. This
# is done for all simulations in the simulation directory.
# Note that the simulations must all have the same genes
# for this script to work.

# To run this script enter in the command line:
#	bash find_rep.sh
# Then enter the directory with the simulations.

read simulationDirectory

for directory in $(ls -d ${simulationDirectory}/*cds | tail -n $(expr 500 - 482))
	do
		echo "$directory/representatives.fa $directory/ppan.fa $directory/ptro.fa $directory/hsap.fa $directory/ggor.fa $directory/pabe.fa" |
		python3 rep_transc.py &&
		echo "Representatives for $directory extracted."
	done
