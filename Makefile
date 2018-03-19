all:
	mkdir -p ~/.config/armadillo/
	cp -i credentials.yml ~/.config/armadillo/
	mkdir -p /usr/local/lib/python3.5/dist-packages/armadillo
	cp checkCourse.py /usr/local/lib/python3.5/dist-packages/armadillo/
	cp armadillo /usr/local/bin/

remove:
	command rm -r /usr/local/lib/python3.5/dist-packages/armadillo
	command rm /usr/local/bin/armadillo
