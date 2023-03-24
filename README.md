
<p>
    <h2 align="center">Welcome to The Last Algorithms Course You'll Need</h2>
    <h5 align="center">presented by ThePrimagen<h5>
</p>

![Python 3.8-3.11](./assets/readme/python_versions.svg)
[![test](https://github.com/Andrei-Aksionov/TheLastAlgorithmsCourseYouWillNeed/actions/workflows/test.yaml/badge.svg)](https://github.com/Andrei-Aksionov/TheLastAlgorithmsCourseYouWillNeed/actions/workflows/test.yaml)

***
<p align=center><img src="assets/readme/algorithms.png"></p>

I decided to take class in a cool course [The Last Algorithms Course You'll Need](https://frontendmasters.com/courses/algorithms/) presented by ThePrimagen. It's easy to understand (sometimes even funny), yet covers all the concepts of algorithms in about 9 hours. Highly recommended. And it's free!!!

# How to use it

1. Install all the required packages. In this project all the python dependencies are managed by [Poetry](https://python-poetry.org/) and are stored in "pyproject.toml" file (in this file also specified required version of python). After `poetry` is installed and virtual environment is created (in case you don't want poetry to create it [automatically](https://python-poetry.org/docs/configuration/#virtualenvscreate)), run:

    ```bash
    poetry install
    ```

2. Implement algorithm and run tests:

    - To run all tests:

        ```bash
        pytest
        ```

    - To run specific test by providing path, which mimics path to the file with algorithm `course->test/...`, so for file `course/search/linear_search.py` it will be:

        ```bash
        pytest tests/search/linear_search_test.py
        ```

    - To run the whole chapter you can use pytest marks:

        ```bash
        pytest -m search
        ```

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
