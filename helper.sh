#!/bin/sh

help_text="Options are:

	create
"

case "$1" in

	create)
		echo "Creating template chapter structure"

		create_path="$(pwd)/${2}"
		mkdir -p "${create_path}/images"
		touch "${create_path}/exercises.md" "${create_path}/README.md"

		echo "# Exercises" > "${create_path}/exercises.md"
	;;

	*)
		echo "${help_text}"
		
esac