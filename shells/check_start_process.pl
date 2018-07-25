#!/usr/bin/perl -w
my @services = ('service1', 'service2');
my @commands = ('start_service1_command', 'start_service2_command');

my $root_dir = '/path/to/script/log/';

my $host = `/bin/hostname`;
chomp $host;

my $logfile="$root_dir/check_process.log";
my $date=`date`;
chomp($date);

# ---------- open logfile --------------------------------------------
open(LOG, ">$logfile") or die "Can't open $logfile to write: $!";
print LOG "Monitor Started On $date!\n";
close(LOG);
# ---------- close logfile --------------------------------------------

$i=0;

foreach my $service (@services) 
{
	
	my $status = `ps ax | grep $service | grep -v grep`;
	if (!$status) {
		# ---------- open logfile --------------------------------------------
		open(LOG, ">>$logfile") or die "Can't open $logfile to write: $!";
		print LOG "Service $service is started ON $date!\n";
		close(LOG);
		print "Service $service is started ON $date!\n";
        # ---------- close logfile --------------------------------------------
		my $skcom = exec($commands[$i]);
	}else {
		# ---------- open logfile --------------------------------------------
		open(LOG, ">>$logfile") or die "Can't open $logfile to write: $!";
		print LOG "Service $service is running\n";
		close(LOG);
		# ---------- close logfile --------------------------------------------
		print "Service $service is running\n";	
	}
	$i++;
}
