# Mid_Term Projest

##  My Command-Line Calculator

This document explains the functionality and usage of the command-line calculator application.

### Features

* Performs basic arithmetic operations (addition, subtraction, multiplication, division).
* Stores calculation history in a CSV file (`cal_csv_hist/cal_hist.csv`).
* Supports loading plugins for potential future functionalities.
* Configurable through environment variables for base path and logging level.

### Usage

1. **Installation (assuming a virtual environment named `venv` is activated):**

   ```bash
   pip install -r requirements.txt
   ```

2. **Running the application:**

   ```bash
   python main.py
   ```

3. **Using the calculator:**

   * Enter a mathematical expression (e.g., `2 + 3`, `5.2 * 4`).
   * Press Enter to see the result.
   * Enter `history` to view the calculation history (saved as `cal_csv_hist/cal_hist.csv`).
   * Enter `exit` to quit the application.

###  Understanding the Code

The application consists of several key components:

* **`app/commands/__init__.py`:** Defines the base structure for commands using an abstract `Command` class and a `CommandHandler` class for registering and executing commands.
* **`app/plugins/calculator/__init__.py`:** Contains the `CalculatorCommand` class that implements the calculator functionality as a command. It utilizes a separate `Calculator` class for performing calculations and storing history in a pandas DataFrame.
* **`app/__init__.py`:** The main application entry point. It handles environment variables, logging configuration, plugin loading, and the main application loop for user interaction.
* **`tests/test_plugin_calculator.py`:** Unit tests for the `Calculator` class using the `pytest` framework.
* **`main.py` (Updated): This file ensures the application starts when you run it from the command line.

### Environment Variables

The application supports the following environment variables:

* `CALCULATOR_BASE_PATH`: Sets the base path for the `cal_csv_hist` directory that stores the calculation history CSV file. Defaults to the current working directory.
* `CALCULATOR_LOG_LEVEL`: Sets the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL). Defaults to 'INFO'.

**Example:**

```bash
CALCULATOR_BASE_PATH=~/calculator_data CALCULATOR_LOG_LEVEL=DEBUG python app/__init__.py
```

This will run the application with the history saved in the `~/calculator_data/cal_csv_hist/cal_hist.csv` file and log messages at the DEBUG level.

### Conclusion

This command-line calculator provides a basic yet functional tool for performing calculations and keeping track of your history in the `cal_csv_hist/cal_hist.csv` file. You can further customize it by adding new features as plugins or modifying the existing functionalities.