# MailBoom
# Website Registration & Email Validation Testing

## Overview

This project is a Python-based Selenium script designed to automate website registration forms and explore how web applications handle Gmail email aliases.

The goal is to understand potential business logic flaws in email validation, account creation limits, and free-trial eligibility mechanisms.

## Features

- Automates browser interactions using Selenium WebDriver.
- Generates random identifiers for Gmail plus-addressing.
- Automatically fills in registration form fields.
- Helps explore how websites validate email addresses.
- Demonstrates basic web automation and application security testing concepts.


## How It Works

1. The user provides a website URL.
2. The script requests a first name, last name, and Gmail username.
3. A random five-character string is generated.
4. The script constructs an email alias using Gmail plus-addressing (e.g., `username+abcde@gmail.com`).
5. Selenium fills in the registration form and clicks a specified page element.
6. The user can manually check whether a verification email arrives.

**Note:** The script does not automatically confirm successful registration or prove that a security vulnerability exists.

## Requirements

- Python 3
- Google Chrome
- Selenium

Install Selenium:

```bash
pip install selenium
```

## Usage

1. Clone or download this repository.
2. Install the required dependency.
3. Please sometimes don't forget to adjust some lines on the code
4. Run the script:

```bash
python main.py
```

4. Enter the requested information when prompted.

The website must have form fields matching the element IDs and CSS selector used in the script. These selectors may need to be adapted for an authorized test application.

## Security Concepts

This project explores:

- Email alias handling
- Input validation
- Business logic vulnerabilities
- Account creation limits
- Free-trial eligibility controls
- Browser automation with Selenium

## Limitations

- Uses hardcoded HTML selectors.
- Does not automatically verify account creation.
- Does not determine whether a finding qualifies for a bug bounty.
- Website layouts and validation rules may differ.

## Responsible Use

This project is intended for educational purposes and authorized security testing only.

Only test applications you own or have explicit permission to assess. Follow the applicable bug bounty program rules and avoid creating unauthorized accounts or consuming services beyond permitted limits.

## Disclaimer

This tool is provided for learning and testing purposes. The author does not encourage unauthorized access, abuse of free trials, or violations of website terms of service.
