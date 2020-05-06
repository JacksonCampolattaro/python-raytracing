# python-raytracing
#### *Jackson Campolattaro*
A simple raytracing program written in python.

![A small scene](https://raw.githubusercontent.com/JacksonCampolattaro/python-raytracing/master/images/2020-05-01%2015%3A49%3A34.404471.jpg?token=AKIHG2WIA6RWAJ4EYKQLR6K6WW47C)

## Project Description

I put together a minimal raytracing engine.
It's based on [this fantastic book](https://raytracing.github.io/books/RayTracingInOneWeekend.html),
I highly recommend it to anyone interested in the topic.

[![Raytracing in one weekend series](https://raytracing.github.io/images/RTOneWeekend.jpg)](https://raytracing.github.io/)

I needed to adapt the example code from C++ to Python.
This was a great crash course in the language,
because the book used a number of relatively advanced techniques.
It was interesting to see what became easier in Python, 
and what became harder.
Performance quickly became a limiting factor,
and I needed to introduce multithreading 
just to be able to run tests in a reasonable amount of time.

## Usage

### Configuring the Scene

The scene is configured by editing the main program.
Main has a number of comments explaining what variables are responsible for.

Right now, main is configured to produce the image seen at the top of the README.
It took about half an hour to render, 
if you'd like to render a lower quality version faster, 
just to make sure everything works,
try lowering numbers like 
`samples_per_pixel`, `max_depth`, or the image dimensions.


### Running

Make sure all dependencies are installed, there aren't many, 
but if there are any missing, the runtime should let you know what you need anyway.

The program can be run via
```
python3 main.py
```
or even more simply
```
make
```

When running, the program displays its progress. 
Pixels are done using a pool of threads, 
but each row is done in sequence.
The progress indicator tells how many rows have been completed.
