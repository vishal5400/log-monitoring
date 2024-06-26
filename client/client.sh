#!/bin/bash

timestamp=$(date +"%Y%m%d%H%M%S")

source /usr/lib/log-client/conf

first_while_loop() {
	while true; do
		sshpass -p $password rsync -avh -e "ssh -o StrictHostKeyChecking=no" $logs_files $user@$server:~/$name
		sleep 5  # Adjust the interval as needed
	done
}

secound_while_loop() {
	while true; do
		sleep 3600
		for i in $logs_files;
		do
			cp $i "$i$timestamp"
			file=$(basename $i)
			echo $file
			sshpass -p $password ssh -o StrictHostKeyChecking=no $user@$server mv ~/$name/"$file" ~/$name/"$file"_"$timestamp"
			sshpass -p $password rsync -avh -e "ssh -o StrictHostKeyChecking=no" $compear_file $user@$server:~/$name
		done

	done
}
trap 'echo "Exiting..."; exit 0' SIGINT

first_while_loop & 

secound_while_loop &
wait
