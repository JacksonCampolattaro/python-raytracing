# python-raytracing
#### *Jackson Campolattaro*
A simple raytracing program written in python.

![A small scene](https://raw.githubusercontent.com/JacksonCampolattaro/python-raytracing/master/images/2020-05-01%2015%3A49%3A34.404471.jpg?token=AKIHG2WIA6RWAJ4EYKQLR6K6WW47C)

## Project Description

I put together a minimal raytracing engine.
It's based on [this fantastic book](https://raytracing.github.io/books/RayTracingInOneWeekend.html),
I highly recommend it to anyone interested in the topic.

![Raytracing in one weekend series](https://raytracing.github.io/images/RTOneWeekend.jpg)

*Link Goes Here*

I needed to adapt the example code from C++ to Python.
This was a great crash course in the language,
because the book used a number of relatively advanced techniques.
It was interesting to see what became easier in Python, 
and what became harder.
Performance quickly became a limiting factor,
and I needed to introduce multithreading just to get reasonable performance.

## Usage

The scene is configured by editing the main program.

When running, the program displays its progress. 
Pixels are done using a pool of threads, 
but each row is done in sequence.
The progress indicator tells how many rows have been completed.
