# Run the python script with two files as input.
rep_seq=$(echo "$1" "$2" | python3 rep_transc.py)

# Store the id lines (and their line numbers) of the sequences in seq_info.txt
grep -n peptide "$1" > seq_info.txt &&
	if [ $rep_seq == $(cat seq_info.txt | wc -l) ] # If the last transcript is the representative.
		then
			# Retrieve the last sequence of "$1" together with its id line.
			tail -n $(expr $(cat "$1" | wc -l) - $(expr $(tail -n 1 seq_info.txt | cut -d : -f 1) - 1)) "$1" 
	else	
		# Store the line numbers of the id line of the representative
		# transcript and the transcript under it in tmp.txt
		head -n $(expr $rep_seq + 1) seq_info.txt |
		tail -n 2 |
		cut -d : -f 1 > tmp.txt 

		# Store the line numbers in these variables and then delete tmp.txt
		rep_seq_id_line=$(head -n 1 tmp.txt) && next_seq_id_line=$(tail -n 1 tmp.txt) && rm tmp.txt 

		# Retrieve the id line and the sequence of the representative transcript.
		head -n $(expr $next_seq_id_line - 1) "$1" | tail -n $(expr $next_seq_id_line - $rep_seq_id_line)
	fi &&
	rm seq_info.txt
