# (Demo only)

## Set up 
Clone the repository
```
git clone https://github.com/paoloco/selenium_practice.git
```

Run the following command to install libraries 
```
cd selenium_practice && pip3 install -r requirements.txt
```

### Run the tests
Some tests are parameterized and its cleaner to run with -v
```
pytest -v 
```

## Structure of this repository
- Under data directory, it data for DDT tests
- Under pages directory, it has POM classes that tests rely on
- Under test directory, it has location of all classes
