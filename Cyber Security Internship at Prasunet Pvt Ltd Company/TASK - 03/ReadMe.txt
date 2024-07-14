Password Complexity Checker
Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.

Explanation:
check_password_complexity Function:

Checks the password against different criteria: length (at least 8 characters), presence of uppercase letters, lowercase letters, digits, and special characters.
Uses regular expressions (re.search) to check for the presence of these characters.
Calculates a score based on how many criteria the password meets.
Determines the password strength based on the score and provides feedback on how to improve the password if it doesn't meet all criteria.
main Function:

Prompts the user to enter a password.
Calls check_password_complexity to assess the password strength and provide feedback.
Prints the password strength and feedback.
Usage:
To use this program, run it and enter a password when prompted. The program will then display the strength of the password and provide feedback on how to improve it if necessary.