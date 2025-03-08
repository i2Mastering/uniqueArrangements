# Factorial Permutations

A Python program that calculates unique permutations of elements across subsets using factorial computations. Users input subset constraints, and the program computes valid arrangements.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Components](#components)
- [Requirements](#requirements)
- [License](#license)

## Features
- Computes factorials efficiently.
- Calculates permutations with repetition.
- Validates user input.
- Displays total arrangements.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/factorial-permutations.git
   ```
2. Navigate to the project folder:
   ```sh
   cd factorial-permutations
   ```
3. Ensure you have Python installed (3.x recommended).

## Usage
1. Run the script:
   ```sh
   python factorial_permutations.py
   ```
2. Enter the number of subsets (between **3 and 8**).
3. Define the size of each subset (between **1 and 5**).
4. Input total arrangements (for validation).
5. View the calculated number of valid permutations.

## Example
```sh
Enter subsets: 4
Enter sizes: 2, 3, 1, 4
Total arrangements: 12600
```

## Components
- **`fact(n)`**: Computes factorial.
- **`perm_rep(mj)`**: Calculates unique permutations.
- **`uimulti_set()`**: Handles user input.

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.
