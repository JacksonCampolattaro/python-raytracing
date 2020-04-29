
all: lint ray

ray: ray.py
	python3.7 vec3.py ray.py

lint: ray.py
	black vec3.py ray.py
