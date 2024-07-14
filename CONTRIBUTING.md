# Contributing to SheetBuddy

🎉 First off, thanks for taking the time to contribute! 🎉

The following is a set of guidelines for contributing to SheetBuddy. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development](#development)
  - [Setting Up Your Environment](#setting-up-your-environment)
  - [Running Tests](#running-tests)

## Code of Conduct

This project and everyone participating in it is governed by the [SheetBuddy Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [Ashishrogannagari](mailto:Ashishrogannagari98@gmail.com)

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for SheetBuddy. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

Before creating a bug report, please check that an issue describing the bug does not already exist. When you are creating a bug report, please include as many details as possible.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for SheetBuddy, including completely new features and minor improvements to existing functionality.

Before creating enhancement suggestions, please check that an issue describing the enhancement does not already exist. When you are creating an enhancement suggestion, please include as many details as possible.

### Pull Requests

The process described here has several goals:

- Maintain SheetBuddy's quality
- Fix problems that are important to users
- Engage the community in working toward the best possible SheetBuddy
- Enable a sustainable system for SheetBuddy's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Fork the repository and create your branch from `main`.
2. If you have added code that should be tested, add tests.
3. If you have changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Development

### Setting Up Your Environment

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AshishRogannagari/SheetBuddy.git
    cd SheetBuddy
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running Tests

1. **Install test dependencies**:
    ```bash
    pip install pytest
    ```

2. **Run the tests**:
    ```bash
    pytest
    ```

### Coding Style

- Follow PEP 8 guidelines for Python code.

- Use descriptive variable names.

- Write docstrings for all functions and classes.


Happy contributing! 🚀
