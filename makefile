all: main

# run the project

main: # windows
	py src/main.py

linux: # linux
	python3 src/main.py

# install requirements

init: # windows
	py -m pip install -r requirements.txt

linux-init: # linux
	pip install -r requirements.txt