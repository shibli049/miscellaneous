# to count all line or
wc -l <file>

# to filter and count only lines with pattern
grep -w "pattern" -c <file>

# -v to invert match
grep -w "pattern" -c -v <file>