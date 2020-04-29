
all: lint ray

ray: ray.py vec3.py
	python3.7 ray.py

lint: ray.py
	black vec3.py ray.py
