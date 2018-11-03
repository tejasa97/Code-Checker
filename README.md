# Code-Checker v0.9
A python script that checks the compliance of a particular set of C device drivers to a set of Linux driver standards.

A snippet of the Linux driver standards:

<img src = images/rule1.png height = 600>

<img src = images/rule2.png height = 600>

<img src = images/rule3.png height = 600>

# Dependencies

```sh
pip install -r requirements.txt
```
# Usage
If no file is specified as argument, all files in folder **programs** are checked.

```sh
python code_checker.py
```

<img src = images/result1.png height = 700>


Also, a particular file can be checked by passing it as an argument.

```sh
python code_checker.py programs/a1_b.py
```

<img src = images/result2.png height = 100>

