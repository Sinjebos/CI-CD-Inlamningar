- [Report](#Report)
- [tests](#tests)
    - [flake8](#flake8)
    - [pytest](#pytest)
- [circleci](#circleci)
- [Github-Merge](#Github-Merge)


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

showed two tests where one failed and one succeeded.

![](img/4.png)

# **pytest**

Two tests here aswell.

![](img/5.png)

## circleci

I added a .circleci with a config.yml file to automate the tests to run whenever I push to any branch.

![](img/3.png)

I ran the command "py -m pip freeze > requirements.txt" in the terminal and cleaned up the file from everything that wont be needed for these tests

![](img/8.png)

Here I can see the different builds and this one passed.

![](img/6.png)

And in this part I can see all the steps and what circleci did.

![](img/7.png)

## Github Merge

![](img/9.png)

![](img/10.png)

![](img/11.png)