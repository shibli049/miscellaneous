#copy directory and exclude .svn,.git etc folder. 
rsync -rav --progress --exclude=directoryToExclude source_directory destination_directory/