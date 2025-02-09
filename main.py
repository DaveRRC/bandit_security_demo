import subprocess
import pickle
import yaml
import os

def unsafe_deserialization(file_path):
    # Vulnerability 1: Unsafe deserialization using pickle
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def execute_command(cmd):
    # Vulnerability 2: Command injection risk
    return subprocess.call(cmd, shell=True)

def parse_yaml_file(yaml_file):
    # Vulnerability 3: Unsafe YAML loading
    with open(yaml_file, 'r') as f:
        return yaml.load(f)

def write_sensitive_data(password):
    # Vulnerability 4: Hardcoded password
    admin_password = "super_secret_password123"
    if password == admin_password:
        return True
    return False

def read_file(filename):
    # Vulnerability 5: Path traversal vulnerability
    with open(filename) as f:
        return f.read()

def main():
    # Example usage of vulnerable functions
    try:
        # Potentially dangerous file operations
        user_file = input("Enter filename to read: ")
        content = read_file(user_file)
        
        # Unsafe command execution
        cmd = input("Enter command to run: ")
        execute_command(cmd)
        
        # Using hardcoded credentials
        if write_sensitive_data("password123"):
            print("Access granted!")
        
        # Unsafe YAML parsing
        config = parse_yaml_file("config.yml")
        
        # Pickle deserialization
        data = unsafe_deserialization("data.pickle")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
