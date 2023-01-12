master_password = input("What is the master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:", passw)
        



def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + password + "\n")


while True:
  mode = input("Add or view axisting password? (add/view), press q to quit ").lower()
  if mode == "q":
    break

  if mode == "view":
    view()
  elif mode == "add":
    add()
  else:
    print("Invalid mode")
    continue
