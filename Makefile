
all: lint ray

ray: ray.py
	python3.7 ray.py

lint: ray.py
	black ray.py
