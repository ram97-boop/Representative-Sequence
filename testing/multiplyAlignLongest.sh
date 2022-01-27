iterations=(004 005 017 035 038 042 059 063 077)
filePrefix="alternative_transcripts/_iteration_"
fileSuffix="_cds/longestTranscripts.fa"
for i in ${iterations[@]}; do
	clustalo -i "${filePrefix}$i${fileSuffix}" -o "${filePrefix}${i}_cds/aligned_longest.fa"
done
