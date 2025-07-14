# 🐍 Python Live-Coding Challenges

Welcome to the **Python Live-Coding** project! This is a curated collection of coding challenges designed for live practice, pair programming, and educational sessions—similar to platforms like CodeWars, HackerRank, and LeetCode.

Each challenge includes:

- A clear function to implement
- A matching test suite using `pytest`
- Input validation and edge case handling

---

## 🚀 Getting Started

### Python installation

1. Python 3 should be installed - https://www.python.org/downloads/

Note: Please don't forget to include it to the environment variables path

### Pipenv installation

1. If you don't have pipenv installed yet, you can install it globally using pip:

```bash
pip install pipenv
```

### IDE or Editor installation

#### PyCharm

Option a is to install PyCharm - The Python IDE for data and web professionals https://www.jetbrains.com/pycharm/. The problem is it is not a free

#### Visual Studio Code with extensions

Visual Studio Code is fully free and you can make extension installations in order to make this editor very close to IDE

- Visual Studio Code - https://code.visualstudio.com/

Recommended Extensions

- autopep8
- Python

### Clone the repository

```bash
git clone https://github.com/dneprokos/python-live-coding.git
cd python-live-coding
```

## 🧪 Preparing virtual environment

- Install Pipfile depenedncies (required):

```bash
pipenv install
```

- Activate virtual environment (required)

```bash
pipenv shell
```

- Diactivate virtual environment

`exit`

## How to Select the Correct Python Interpreter in VS Code

1. Open the Command Palette
   Press Ctrl + Shift + P (or F1) to open the command palette.

2. Search for Python: Select Interpreter
   Type: Python: Select Interpreter
   (You’ve already done this — as shown in your screenshot ✅)

![python intepreter](/images/python_intepreter.png)

3. Choose the Right Interpreter

You’ll see a list of available environments:

Virtual environments (.venv, pipenv, etc.)

Global Python installations

If you're using pipenv, look for one that includes .virtualenvs or has your project name in it.

Example: ~/.local/share/virtualenvs/python-live-coding-.../bin/python

![python intepreter selection](/images/select_python_interpeter.png)

4. Click the Interpreter You Want to Use
   Once selected, it sets the interpreter for the workspace. You should see the path reflected in the bottom-left of VS Code.

## 🧪 Running tests

- To run all tests from command line:

```bash
pipenv run pytest -v
```

- Alternatively you can select the tests you want to run on Testing tab

![run tests from testing tab](/images/run-tests-from-testing.png)

## 🧩 How to add new challenge and tests

1. Create the challenge file. Inside the challenges/ folder, add a new Python file.

Example:

```bash
challenges/reverse_string.py
```

2. Implement the function

Include:

Clear input/output expectations

Type annotations

A docstring explaining the behavior

Input validation (raise TypeError if needed)

Example:

```python
def reverse_string(s: str) -> str:
    """
    Reverses the input string.

    Parameters:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s[::-1]
```

3. Write the unit tests. In the tests/ folder, create a corresponding test file named:

```bash
tests/test_reverse_string.py
```

Example:

```python
from challenges.reverse_string import reverse_string
import pytest

def test_reverse_regular_string():
    assert reverse_string("hello") == "olleh"

def test_reverse_empty_string():
    assert reverse_string("") == ""

def test_reverse_non_string_input():
    with pytest.raises(TypeError):
        reverse_string(123)
```

4. Run the tests. See "Running tests" section above
