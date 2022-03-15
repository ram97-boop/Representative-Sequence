# This shell script is for creating a file containing the
# genes' longest sequences in a simulation. This is done
# for all simulations in the simulation directory. Note
# that the simulations must all have the same genes for
# this script to work.

# To run this script enter in the command line:
#	bash find_longest.sh
# Then enter the directory with the simulations.

read simulationDirectory

for directory in $(ls -d ${simulationDirectory}/*cds)
	do
		echo "$directory/longestTranscripts.fa $directory/ppan.fa $directory/ptro.fa $directory/hsap.fa $directory/ggor.fa $directory/pabe.fa" |
		python3 rep_transc.py &&
		echo "Longest transcripts of $directory extracted."
	done
