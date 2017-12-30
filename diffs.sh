#!/bin/bash 

DIR=/Users/ingridburrington/Documents/infra/unsettling/policyparser/data/facebook/dedup/privacypolicy

# cd $DIR

for F in $DIR/*.txt 
do
	cp $F $DIR/diffs/privacypolicy.txt
	echo "commit "$(basename "${F%.*}")""
	git add --all 
	git commit -m "$(basename "${F%.*}")" 
done

git log > $DIR/gitlog.txt

exit