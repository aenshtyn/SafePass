## Safe Pass

#### By

Mohamed

## Description

SafePass is a terminal run python application that allows users to store usernames and passwords of their various accounts.


## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Delete a credential


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./safepass.py** | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Display prompt for which credential to copy | **Enter: copy** | Enter the site name of the credential you wish to copy. |
| Exit application | **Enter: ex** | Exit the current navigation stage |

## Setup/Installation Requirements

### Requirements

  * python
  * pip
  * pyperclip

## Cloning
* In your terminal:


  Step 1 : Run 'git clone https://github.com/aenshtyn/SafePass' on your terminal.
  step 2 : Open your terminal and run the safepass.py file

## Running the Application
  * To run the application, in your terminal:

          $ chmod +x safepass.py
          $ ./safepass.py

## Testing the Application
* To run the tests for the class file:
    $ python3.6 credentials_test.py
    $ python3.6 user_test.py


## Technologies Used

Python 3.7

## Support and contact details

If you have any issues or questions you can contact me at demahom93@gmail.com

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
