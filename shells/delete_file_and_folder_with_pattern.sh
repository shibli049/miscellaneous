# this will list all files inside `/path/to/dir` with pattern of directory `*4.0.3.RELEASE/*`
find /path/to/dir -type f -wholename '*4.0.3.RELEASE/*'

## check carefully if you really want to delete these files:
# this will delete all files inside `/path/to/dir` with pattern of directory `*4.0.3.RELEASE/*`
find /path/to/dir -type f -wholename '*4.0.3.RELEASE/*' -delete

# finally this will delete all folders with pattern `*4.0.3.RELEASE*` :
# NB: if the folders are not empty, this will fail. 
find /path/to/dir -type d -wholename '*4.0.3.RELEASE*' -delete
