sed 's/[^A-Za-z]\+/\n/g' | grep -v '^$' > $$words
tail -n +2 $$words > $$nextwords
paste $$words $$nextwords |
sort | uniq -c | sort -nr
# remove the temporary files
rm $$words $$nextwords 