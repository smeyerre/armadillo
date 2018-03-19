all:
	mkdir -p ~/.config/armadillo/
	cp -i credentials.yml ~/.config/armadillo/
	cp armadillo /usr/local/bin/

remove:
	command rm /usr/local/bin/armadillo
