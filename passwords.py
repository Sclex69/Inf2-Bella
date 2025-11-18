FILE = "passwords.txt"

def ensure_file():
    try: open(FILE, "x").close()
    except FileExistsError: pass

def load_users():
    ensure_file()
    users = {}
    with open(FILE) as f:
        for line in f:
            u, p = line.strip().split(":")
            users[u] = p
    return users

def save_users(users):
    with open(FILE, "w") as f:
        for u, p in users.items():
            f.write(f"{u}:{p}\n")

def valid_password(pw):
    return (
        len(pw) >= 8 and
        any(c.isupper() for c in pw) and
        any(c.isdigit() for c in pw)
    )

def add_user():
    users = load_users()
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter new password: ")
    if not valid_password(password):
        print("Password does not meet requirements.")
        return
    users[username] = password
    save_users(users)
    print("User added.")

def find_password():
    users = load_users()
    username = input("Enter username: ")
    print("Password:", users.get(username, "User not found"))

def login():
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == password:
        print("Login successful.")
    else:
        print("Login failed.")

def delete_user():
    users = load_users()
    username = input("Enter username to delete: ")
    if username not in users:
        print("User not found.")
        return
    del users[username]
    save_users(users)
    print("User deleted.")

def admin_reset():
    users = load_users()
    admin_user = input("Admin username: ")
    admin_pass = input("Admin password: ")

    # simple default admin
    if admin_user != "admin" or admin_pass != "Admin123":
        print("Admin login failed.")
        return

    target = input("User to reset password for: ")
    if target not in users:
        print("User not found.")
        return

    new_pass = input("New password: ")
    if not valid_password(new_pass):
        print("Password does not meet requirements.")
        return

    users[target] = new_pass
    save_users(users)
    print("Password reset successful.")

# ----------- MENU -----------
def main():
    ensure_file()
    print("Initial admin login: admin / Admin123 (must be added manually once).")

    while True:
        print("\n--- PASSWORD MANAGER ---")
        print("1. Add user")
        print("2. Find password")
        print("3. Login")
        print("4. Delete user")
        print("5. Admin reset password")

        choice = input("Choose option: ")

        if choice == "1": add_user()
        elif choice == "2": find_password()
        elif choice == "3": login()
        elif choice == "4": delete_user()
        elif choice == "5": admin_reset()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
