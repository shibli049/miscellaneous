find . -type f -size +100M -exec ls -lh {} \;
#with lesser information
find . -type f -size +10M -exec ls -gGh {} \;
