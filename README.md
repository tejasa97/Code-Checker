# Code-Checker
A python script that checks the compliance of a particular set of C device drivers to a set of Linux driver standards.

A snippet of the Linux driver standards:

<img src = images/rule1.png height = 600>

<img src = images/rule2.png height = 600>

<img src = images/rule3.png height = 600>

To install dependencies, 

```sh
pip install -r requirements.txt
```

Example output with no file specified, i.e: all files in folder **programs** are checked.

```sh
python code_checker.py
```

<img src = images/result1.png height = 700>


Example output with particular file specified via command line.

```sh
python code_checker.py programs/a1_b.py
```

<img src = images/result2.png height = 100>

