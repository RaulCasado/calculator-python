# Calculator - Python GUI Calculator

## Project Overview

This project is a simple calculator application built using Python's Tkinter library. It provides a graphical user interface to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The calculator also includes functionality for clearing the input, deleting the last character, and handling keyboard inputs.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Clear the input with the "C" button.
- Delete the last character with the "<--" button.
- Keyboard support for numeric keys, operators, and other functional keys.
- Display results in a text widget.

## Requirements

- Python 3.10
- Tkinter (included with Python)

## Installation

1. Clone the repository:

2. Make sure to create a virtual environment and activate it:

    ```sh
    python -m venv name_of_virtualenv
    source name_of_virtualenv/bin/activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Tkinter should be installed by default with Python. If not, you can install it using the following command:

    ```sh
    sudo apt-get install python3-tk
    ```

5. Use pip freeze to see installed packages:

    ```sh
    pip freeze
    ```

6. Navigate to the project directory:

    ```sh
    cd calculator
    ```

7. Run the application:

    ```sh
    python main.py
    ```

## Usage

1. **Button Clicks:** Click the buttons to enter numbers and operators. The result is displayed in the text widget at the top of the window.
2. **Keyboard Input:** Use the keyboard to enter numbers and operators. Supported keys include:
   - Numeric keys: 0-9
   - Operators: +, -, *, /
   - Equals key: =
   - Clear: C
   - Delete last character: Backspace
   - Parentheses: (, )

## Project Structure

This project follows the MVC (Model-View-Controller) design pattern to separate concerns and improve maintainability. Here is how the project is organized:

- **Model**: The model represents the data of the application. In this calculator application, the calculations are handled in this class.

- **View**: The view is responsible for the GUI components and layout. It interacts with the user and displays the data. In this project, `application_view.py` contains the `ApplicationView` class, which defines the interface of the calculator, including buttons, display, and input handling.

- **Controller**: The controller handles the logic and user input, updating the model and view accordingly. `calculator_controller.py` contains the `CalculatorController` class, which processes the input from the view, performs calculations, and updates the display.

### Advantages of MVC

1. **Separation of Concerns**: The MVC pattern separates the application logic from the user interface, making the application more modular and easier to manage.
2. **Maintainability**: Changes in one part of the application can be made independently of others, making the application easier to maintain.
3. **Reusability**: Components can be reused across different parts of the application or even in different projects.
4. **Scalability**: Each component can be developed and tested independently.
5. **Collaborative Development**: Developers can work on different components simultaneously without interfering with each other´s work.

### Disadvantages of MVC

1. **Complexity**: MVC can add unnecessary complexity to simple applications. It´s easier to just make the application in one file.
2. **Learning Curve**: For developers unfamiliar with the pattern, there can be a learning curve to understand and implement MVC effectively.
3. **Coordination**: Ensuring that changes in the model and view are synchronized through the controller requires careful coordination, which can be challenging in larger applications.

## Risks of Using `exec` and `eval` in Python

- **Code Injection Vulnerabilities:** Both `exec` and `eval` functions in Python can execute arbitrary code. If this code originates from an untrusted source or user input, it can lead to code injection vulnerabilities, allowing attackers to execute malicious code on your system.

- **Debugging Difficulty:** Debugging code that utilizes `exec` or `eval` can be challenging because the executed code is not statically defined within the script but is generated dynamically. This can make it harder to identify and troubleshoot errors.

- **Compilation Overhead:** Each call to `exec` or `eval` requires the Python interpreter to compile the provided code, which adds additional processing time. This overhead can become significant, especially for large or complex code snippets, impacting the performance of your application.

## Safer Alternatives

- **Use Specialized Libraries:** You can use specialized libraries like `numexpr` for mathematical calculations. This library is designed to be efficient and secure, reducing the risk of vulnerabilities associated with `exec` and `eval`.

## Conclusion

While `exec` and `eval` offer flexibility and power, they also introduce significant security risks and performance overhead. By using safer alternatives and following best practices for input validation and sanitization, you can mitigate these risks and ensure the security and reliability of your Python applications.
