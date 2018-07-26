# list all files from current directory and it's subdirectories.
# And ignore some directory.
find . -type f -follow -not -path "./.git/*"