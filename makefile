all: main

main:
	py src/main.py

init:
	py -m pip install -r requirements.txt