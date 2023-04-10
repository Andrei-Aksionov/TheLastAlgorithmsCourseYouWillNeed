
<p>
    <h2 align="center">The Last Algorithms Course You'll Need</h2>
    <h5 align="center">presented by ThePrimeagen on FrontendMasters.com</h5>
    <h6 align="center">in Python</h6>
</p>

![Python 3.8-3.11](./assets/readme/python_versions.svg)
[![test](https://github.com/Andrei-Aksionov/TheLastAlgorithmsCourseYouWillNeed/actions/workflows/test.yaml/badge.svg)](https://github.com/Andrei-Aksionov/TheLastAlgorithmsCourseYouWillNeed/actions/workflows/test.yaml)

***
*Click on the image to see video preview of the course* ⤵
<div align="center">
      <a href="https://www.youtube.com/watch?v=Lwr3-doAgaI">
         <img src="assets/readme/algorithms.png">
      </a>
</div>

Have you heard about an awesome [algorithms course](https://frontendmasters.com/courses/algorithms/) on `FrontendMasters.com` presented by `ThePrimeagen`? If no, then you are missing a lot: it is well explained and presented in a clear and sometimes funny way (it's ThePrimeagen after all :smirk:) yet covers all the basic in a deep enough manner.

Is it indeed the last algorithmic course you will ever need? Highly doubt about it. The course teaches you the basics, the rest you have to learn yourself by practicing.

> It's like driving school in a way that it teaches you the basics. The remaining attributes of a PRO driver you have to learn on your own: double parking, tailgating, left lane hogging, yelling at other drivers and constantly honking (if you are a New Yorker) :grinning:.

Have I mentioned that [FrontendMasters.com](https://frontendmasters.com/) provides you a free access to any 5 courses of your choice? Yes, this algorithms course is for free. So what are you waiting for? Steady, ready, go ... :runner:

# Motivation for this repository

The main caveat of the course (that you might have already spotted) is that it's for fronted developers, so the code is presented in javascript/typescript. I don't know any of those, I'm just an average python developer :monkey:

The good thing that algorithms are more or less a universal thing, so it's easy to understand them even if they are written in other language. That means that if you know only python that should not stop you. I mean if I somehow managed to understand the code from the course you definitely can do the same.

The bad thing that all the tests that are provided for the course are also for javascript/typescript (or only typescript, for me it's all the same thing :shrug:). That why this repo is created.

> **Note**: How you should use this repo: watch the course, implement algorithms here and run corresponding tests. It's that easy!

Good luck and happy programming.

# Project structure

Project structure might look a bit strange (why in the world queue and stack implementations are in the sort section :shrug:) but I decided to keep it as is so it's aligned to the structure of the course.

- **course**
  - **arrays**: `array_list` and `ring_buffer` that were explained in the video but not implemented. Though it's a good practicing to implement them on your own.
  - **doubly_linked_list**: implementation of doubly linked list with all common methods like push, prepand, append, get, ...
  - **graphs**: adjacency matrix and dijkstra shortest path algorithms.
  - **heap**: MinHeap implementation. Try to implement MaxHeap on your own, it's not that different from MinHeap :wink:
  - **maps**: LRU cache and dictionary implementation. Dictionary was explained in the video but not implemented.
  - **quick_sort**: quick sort with pivot in the end (as in the video) plus with pivot in the middle (wasn't implemented in the video).
  - **recursion**: maze solver with recursion.
  - **search**: linear and binary searches; 'two crystal balls' exercise with sqrt(n) time complexity (as in the video) plus log(n) time complexity implementation.
  - **sort**: bubble sort plus queue and stack implementations; weird combination but this is how it's placed in the course.
  - **trees**: algorithms for binary trees such as search, traversal and comparison of two trees. Plus implementation of trie tree that was explained in the video but not implemeneted.
- **tests**
  - *the same structure as in `course`*
- *pyproject.toml*: package dependencies are stored here and managed py [Poetry](https://python-poetry.org/)

# How to use it

1. Install all the required packages. In this project all the python dependencies are managed by [Poetry](https://python-poetry.org/) and are stored in "pyproject.toml" file (in this file also specified required version of python). After `poetry` is installed and virtual environment is created (in case you don't want poetry to create it [automatically](https://python-poetry.org/docs/configuration/#virtualenvscreate)), run:

    ```bash
    poetry install
    ```

2. Implement an algorithm and run tests:

    - To run all tests:

        ```bash
        pytest
        ```

    - To run specific test by providing path, which mimics path to the file with algorithm `course->test/...`, so for file `course/search/linear_search.py` it will be:

        ```bash
        pytest tests/search/linear_search_test.py
        ```

    - To run the whole chapter you can use pytest marks (mark is shown at the top of each python file with algorithm implementation):

        ```bash
        pytest -m search
        ```

## Answers

In the `main` branch there are only empty bodies of classes and functions, without implementation.

Stuck and have no idea what to do? You can check my implementation in the `answers` branch. </br> But try to do it as minimal as possible: the more you do on your own (even if it hurts :persevere:) the better you are gonna understand algorithms.

# Want to participate in development?

Install all packages required for development:

```bash
poetry install --with dev
```

## Additional: pre-commit hooks

> **Note**: it is recommended for development, because there is a github workflow that executes all the steps from pre-commit anyway, so if you install you will not be surprised why there is a red cross on your PR. Of course if you fill lucky you can skip it :smile:

In order to install pre-commit hooks run:

```bash
pre-commit install
```

Pre-commit hooks will be executed before each commit. In addition all the pre-commit hooks will be run per each PR via github-workflow (no need to add or change anything).

The list of all hooks one can find in a config fils: `.pre-commit-config.yaml`

**Note**: for the sake of speed pre-commit hooks will be executed only on changed files. If it's needed to run on all files execute:

```bash
pre-commit run --all-files
```
