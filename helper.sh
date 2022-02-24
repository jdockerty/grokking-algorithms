#!/bin/sh



case "$1" in

	create)
		echo "Creating template chapter structure"
		
		mkdir -p "$(pwd)/$2/images"
		touch "$(pwd)/$2/exercises.md" "$(pwd)/$2/README.md"
	;;

	*)
		echo 'Invalid arg'
esac