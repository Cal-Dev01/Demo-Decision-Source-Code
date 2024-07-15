import hashlib
import bcrypt

# Simulated user data (typically loaded from a database)
users = {
    "user1": {
        "password_hash": "",
        "salt": ""
    }
}


# Function to securely store passwords
def store_password(username, password):
    # Generate a unique salt for each user
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Store the password hash and salt for the user
    users[username]["password_hash"] = password_hash
    users[username]["salt"] = salt


# Function to validate user login
def validate_login(username, password):
    if username in users:
        # Retrieve the stored salt
        salt = users[username]["salt"]
        # Hash the provided password with the stored salt
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        # Compare the hash with the stored hash
        if password_hash == users[username]["password_hash"]:
            return True
    return False


# Function to hash data
def hash_data(data):
    # Use a strong hashing algorithm, like SHA-256
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()


# Example usage
if __name__ == "__main__":
    # User registration
    username = "user1"
    password = "securepassword123"
    store_password(username, password)

    # User login
    login_username = "user1"
    login_password = "securepassword123"
    if validate_login(login_username, login_password):
        print("Login successful.")
    else:
        print("Login failed.")

    # Data hashing
    data_to_hash = "sensitive data"
    hashed_data = hash_data(data_to_hash)
    print("Hashed Data:", hashed_data)
