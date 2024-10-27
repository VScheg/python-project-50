### Hexlet tests and linter status:
[![Actions Status](https://github.com/VScheg/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/VScheg/python-project-50/actions)
### My tests and linter status:
[![Python CI](https://github.com/VScheg/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/VScheg/python-project-50/actions/workflows/pyci.yml)
### CodeClimate
[![Test Coverage](https://api.codeclimate.com/v1/badges/c7141d81a25f88f931f8/test_coverage)](https://codeclimate.com/github/VScheg/python-project-50/test_coverage)

### Description
Difference Calculator is a program that determines the difference between two data structures.
Program features:

Support for different input formats: YAML, JSON
Report generation in plain text, stylish, and JSON formats

### How to install
Enter commands: 
```
git clone https://github.com/VScheg/python-project-50.git
make install
make build
make package-install
```

### How to launch
To get program instructions enter: 
```gendiff -h```
To compare two files enter:
```gendiff [file_path1] [file_path2]```
To compare two files using particular formatter (plain, stylish or json) enter:
```gendiff -f [format_name] [file_path1] [file_path2]```

### Comparing flat JSON files using stylish formatter
[![asciicast](https://asciinema.org/a/rWfO6hJaPnLCEkELpgX49kXVS.svg)](https://asciinema.org/a/rWfO6hJaPnLCEkELpgX49kXVS)
### Comparing flat YAML files using stylish formatter
[![asciicast](https://asciinema.org/a/IleCvrj7eSsrbaHUhoKo6HY6y.svg)](https://asciinema.org/a/IleCvrj7eSsrbaHUhoKo6HY6y)
### Comparing nested files using stylish formatter
[![asciicast](https://asciinema.org/a/HllZSebiZObKmdiKKnvDziLue.svg)](https://asciinema.org/a/HllZSebiZObKmdiKKnvDziLue)
### Comparing nested files using plain formatter
[![asciicast](https://asciinema.org/a/U8ZITS8RCSlt1Rwy49ZWiTc6F.svg)](https://asciinema.org/a/U8ZITS8RCSlt1Rwy49ZWiTc6F)
### Comparing nested files using json formatter
[![asciicast](https://asciinema.org/a/gz9dF9enTu3yl6gAeWbWJxXHL.svg)](https://asciinema.org/a/gz9dF9enTu3yl6gAeWbWJxXHL)