# source: https://stackoverflow.com/a/1310438/669265
for i in * 
do
    if test -f "$i" 
    then
       echo "Doing somthing to $i"
    fi
done
