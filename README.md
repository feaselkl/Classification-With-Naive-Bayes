# Classification with Naive Bayes

## Description

This repository contains demos that I use in my presentation entitled [Classification with Naive Bayes](https://www.catallaxyservices.com/presentations/naivebayes/).

## Running the Demos

There are two ways of running the demos for this presentation: running them directly or as part of a Docker container.

### Running Directly

To run the demos directly, you will need Python 3.12+ and the following packages:

```bash
pip install jupyter pandas scikit-learn matplotlib seaborn streamlit
```

Then start Jupyter from the repository root:

```bash
jupyter notebook code/notebooks/
```

To run the interactive Streamlit demo:

```bash
streamlit run code/app.py
```

### Building a Docker Container

Build the image:

```bash
docker build -t naive-bayes .
```

Run the container, which starts both Jupyter (port 8888) and the Streamlit demo (port 8501):

```bash
docker run -p 8888:8888 -p 8501:8501 naive-bayes
```

- **Jupyter Notebooks**: http://127.0.0.1:8888 (password: `naivebayes`)
- **Streamlit Demo**: http://127.0.0.1:8501
