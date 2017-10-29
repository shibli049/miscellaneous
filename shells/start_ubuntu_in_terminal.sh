#edit /etc/default/grub with a text editor
sudo vi /etc/default/grub
#edit the following line 
#from
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
#to
GRUB_CMDLINE_LINUX_DEFAULT="text"
#update grub
sudo update-grub
#use X(GUI) by typing 
startx