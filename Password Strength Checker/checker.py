import re

def check_password_strength(password):
    # Define the criteria for password strength
    length_check = len(password) >= 8
    complexity_check = re.search(r'[A-Za-z]', password) and re.search(r'\d', password)
    special_chars_check = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    pattern_check = not re.search(r'(.)\1{2,}', password)  # Avoid repeating characters more than twice
    
    # Evaluate the password based on the criteria
    if length_check and complexity_check and special_chars_check and pattern_check:
        return "Strong password"
    
    suggestions = []
    
    if not length_check:
        suggestions.append("Password should be at least 8 characters long.")
        
    if not complexity_check:
        suggestions.append("Password should include both letters and numbers.")
        
    if not special_chars_check:
        suggestions.append("Password should include special characters (!@#$%^&*(),.?\":{}|<>).")
        
    if not pattern_check:
        suggestions.append("Password should not contain repeating characters more than twice.")
        
    return "Weak password. Suggestions: " + ", ".join(suggestions)

# Prompt the user to enter a password
password = input("Enter a password: ")

# Check the password strength and provide feedback
strength = check_password_strength(password)
print(strength)