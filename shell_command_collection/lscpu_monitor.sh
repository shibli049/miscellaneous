# check realtime cpu usage statistic, refresh at every 1 seconds.
watch -n1 "lscpu | grep MHz | awk '{print $1}'";