## src: https://www.whatsmydns.net/flush-dns.html#other
* for windows 7,8,10 run cmd as administrator, for windows xp and earlier open cmd
    >`ipconfig /flushdns`

* cent-os if not root, try with sudo
    >`/etc/init.d/nscd restart`


* macOS Sierra, El Capitan, Mavericks, Mountain Lion, Lion
    >`sudo killall -HUP mDNSResponder`

* macOS Yosemite
    >`sudo discoveryutil udnsflushcaches`

* macOS Snow Leopard
    >`sudo dscacheutil -flushcache`

* macOS Leopard and below: If you are running Mac OS X 10.5.1 or below
    >`sudo lookupd -flushcache`