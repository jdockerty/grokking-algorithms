#!/bin/sh

help_text="Options are:

	create
"

case "$1" in

	create)
		echo "Creating template chapter structure"

		mkdir -p "$(pwd)/$2/images"
		touch "$(pwd)/$2/exercises.md" "$(pwd)/$2/README.md"
	;;

	*)
		echo "${help_text}"
		
esac