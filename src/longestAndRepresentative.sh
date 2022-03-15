# This shell script is for finding which of the simulations in
# the simulation directory have all their longest sequences
# selected as representatives (or not by switching the flag
# of the diff command between -q and -s).

# To run this script enter in the command line:
#	bash longestAndRepresentative.sh
# Then enter the directory containing the simulations.

read simulationDirectory

for directory in $(ls -d ${simulationDirectory}/*cds)
	do
		diff -q $directory/longestTranscripts.fa $directory/representatives.fa |
		cut -d _ -f 3 #Only show the simulation number
	done
