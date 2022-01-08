# Get the alternative transcripts of one gene

for gene in $(cat $1 | grep "0_" | cut -d _ -f 3)
	do
		echo $gene
	done
