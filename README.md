# Assumptions

* Python3 interpreter is installed to /usr/bin/python3

* pre-commit is installed, see https://pre-commit.com/ for more

* Rounding the tax value always goes higher, so 10.01 is rounded to 10.05 and not to 10.00.

* Products are read from stdin, 1 product per line. Fields are separated by semicolon (;), eg.

```
1;book;14.90
```

We also assume that each line is valid, and has the required fields with appropriate values.

# Usage

```
receipt.py <<< '1;bottle of perfume;20.89'
```

Or using data files to read from, see the example input files in the data directory

```
./receipt.py < data/input1
```

# Unit tests

```
python3 -m unittest
```
