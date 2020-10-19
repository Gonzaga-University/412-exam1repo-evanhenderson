!#/bin/bash
while[ -z "$1" ];
then
	echo "you did not enter a username"
	read check
fi
check=sudo grep $1 /etc/passwd
if["$check" == 0];
then
	du /home/%1
	ls -U /home/%1 | head -10
fi
if["$check" != 0];
then
	echo "ERROR User does not exist"
fi

exit 0
