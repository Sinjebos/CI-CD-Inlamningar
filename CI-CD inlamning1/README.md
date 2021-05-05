```python
test test
```

- [Report](#Report)
- [tests](#tests)
    - [flake8](#flake8)
    - [pytest](#pytest)
- [circleci](#circleci)


# Report

I started with creating a Repo and creating a "Dev" branch and installed flake8 + pytest
```python
Py -m pip install flake8
Py -m pip install pytest
```
I created a basic python code that are easy to make tests for

![](img/1.png)


## tests
After that I created a test_calculator.py to test my code

![](img/2.png)

by running these commands in the terminal 
```python
Py -m pip flake8 --statistics
Py -m pip pytest
```
# **flake8**
![](img/4.png)

# **pytest**
![](img/5.png)

## circleci

I added a .circleci with a config.yml file to automate the tests to run whenever I push to any branch.

![](img/3.png)

![](img/3.png)

![](img/3.png)

![](img/3.png)