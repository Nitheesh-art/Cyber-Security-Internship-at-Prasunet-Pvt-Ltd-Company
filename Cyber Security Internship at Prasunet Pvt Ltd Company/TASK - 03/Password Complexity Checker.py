import re

def check_password_complexity(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None
    
    # Calculate score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    # Provide feedback based on score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")
    
    return strength, feedback

def main():
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_password_complexity(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    main()
