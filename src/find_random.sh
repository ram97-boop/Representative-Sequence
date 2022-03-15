# This shell script is for creating a file containing 
# random sequences of the genes' in a simulation. This
# is done for all simulations in the simulation
# directory. Note that the simulations must all have
# the same genes for this script to work.

# To run this script enter in the command line:
#	bash find_random.sh
# Then enter the directory with the simulations.

for directory in $(ls -d alternative_transcripts/*cds)
	do
		echo "$directory/randomTranscripts.fa $directory/ggal.fa $directory/mdom.fa $directory/mmus.fa $directory/hsap.fa $directory/btaus.fa" |
		python3 rep_transc.py &&
		echo "Random transcripts of $directory selected."
	done
