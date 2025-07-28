# | Question                     | Answer                                               |
# | ---------------------------- | ---------------------------------------------------- |
# | Why use `__init__.py`?       | So Python treats the folder as a package             |
# | Is it always required?       | Not in Python 3.3+, but **best practice** to include |
# | Can it be empty?             | Yes! Totally fine.                                   |
# | Can it contain code?         | Yes, for setup/imports.                              |
# | Should test folders have it? | YES, if using `pytest` or doing relative imports     |
