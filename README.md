# String Calculator TDD Kata

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


A Python implementation of the String Calculator TDD Kata, following Test-Driven Development principles.

## Features

- Handles empty strings
- Handles single and multiple numbers
- Supports custom delimiters
- Handles new lines as separators
- Throws exceptions for negative numbers
- Tracks method call count
- Supports event handling
- Ignores numbers greater than 1000
- Supports multiple delimiters
- Supports long delimiters

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ashokbugude/string-calculator-kata.git
   cd string-calculator-kata
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

## Running the Tests

To run all tests:
```bash
python -m unittest test_string_calculator.py
```

## Using the Calculator

You can use the calculator interactively:
```bash
python main.py
```

Example usage: 

> 1,2,3
Result: 6
> //;\n1;2;3
Result: 6
> exit
```

## Project Structure
```
string-calculator-kata/
├── string_calculator.py      # Main calculator implementation
├── test_string_calculator.py # Unit tests
├── main.py                   # Interactive calculator
├── README.md                 # This file
└── requirements.txt          # Project dependencies
```

## Development Workflow

1. Write a failing test
2. Implement the minimum code to make it pass
3. Refactor
4. Commit changes
5. Repeat

## Test Cases

The following test cases are implemented:

- Empty string returns 0
- Single number returns the number
- Two numbers returns their sum
- Multiple numbers returns their sum
- New lines between numbers are handled
- Custom delimiters are supported
- Negative numbers throw exceptions
- Method call count is tracked
- Add event is triggered
- Numbers greater than 1000 are ignored
- Long delimiters are supported
- Multiple delimiters are supported

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by Roy Osherove's [String Calculator Kata](http://osherove.com/tdd-kata-1/)
- TDD principles from Kent Beck's "Test-Driven Development: By Example"