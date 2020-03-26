# Classification with Naive Bayes
## Description
This repository contains demos that I use in my presentation entitled [Classification with Naive Bayes](https://www.catallaxyservices.com/presentations/naivebayes/).

## Running the Demos

There are two ways of running the demos for this presentation:  running them directly or as part of a Docker container.

### Running Directly

To run the demos directly, you will need Jupyter Notebooks installed and the R kernel configured.  I have some instructions on installing [Jupyter + R on Windows](https://36chambers.wordpress.com/2016/05/24/til-installing-jupyter-on-windows/) and [Jupyter + R on Linux](https://36chambers.wordpress.com/2016/05/10/til-installing-jupyter-and-r-support/) which might be helpful.


### Building a Docker Container

If you would prefer a Docker container which has Jupyter + R pre-installed, grab this repo and run the following commands:

`docker build -t naive-bayes .`

After the image finishes building, run it with the following:

`docker run -p 8888:8888 -e ENABLE_JUPYTER_LAB=YES naive-bayes`

This will prompt you to connect to http://127.0.0.1:8888 (assuming you leave the port the same) and will pre-stage the notebooks and data.