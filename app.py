import subprocess
import pickle
import yaml
import os

def unsafe_deserialization(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)  # This should trigger B301

def execute_command(cmd):
    return subprocess.call(cmd, shell=True)  # This should trigger B602

def parse_yaml_file(yaml_file):
    with open(yaml_file, 'r') as f:
        return yaml.load(f)  # This should trigger B506

def write_sensitive_data(password):
    admin_password = "super_secret_password123"  # This should trigger B105
    if password == admin_password:
        return True
    return False

def read_file(filename):
    with open(filename) as f:  # This should trigger B101
        return f.read()

if __name__ == "__main__":
    main()
