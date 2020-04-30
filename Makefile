
all: lint run

run: main.py vec3.py color.py ray.py hittable.py sphere.py camera.py material.py
	python3.7 main.py

lint: main.py vec3.py color.py ray.py hittable.py sphere.py camera.py material.py
	black main.py vec3.py color.py ray.py hittable.py sphere.py camera.py material.py

