# N11 Login Test Automation Project

This project includes both manual and automation tests for the N11.com Login System using Selenium, Python, and pytest. The tests aim to comprehensively validate user experience and security controls on the login screen.

---

## Features

### The project tests the following scenarios on the N11 login screen:
- Successful login verification  
- Invalid username and/or password combinations  
- Login attempts with empty fields  
- Validation of password length limits (minimum and maximum)  
- Verification of UI element placements and placeholders  
- HTTP to HTTPS redirection control  
- Login validation at the API level  

The tests are prepared manually and executed with Selenium-based automation codes. Additionally, HTML reports are generated using `pytest-html`.

---

## Manual Tests
- Manual test scenarios have been prepared.
- **All Manual Test Scenarios**: View the PDF of Manual Tests

---

## Automation Features
- Manual test scenarios have been converted into automation functions.

---

## Setup

### Requirements
- Python 3.x  
- pip (Python package manager)  
- ChromeDriver (WebDriver)  




#### Install Required Dependencies:
```bash
pip install -r requirements.txt
```

#### Configure ChromeDriver:
1. Download the correct version of ChromeDriver.
2. Add it to the PATH variable.

---

## Usage

### Run the Tests:
```bash
pytest --html=reports/rapor.html --self-contained-html
```

### View the HTML Report:
After the test run, the report will be saved in the `reports` folder within the project directory.

---
