
all: lint run

run: main.py vec3.py color.py ray.py
	python3.7 main.py

lint: main.py vec3.py color.py ray.py
	black main.py vec3.py color.py ray.py
