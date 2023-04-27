import hashlib


class Database():
    def __init__(self):
        self.base = {
            '9948c645c094247794f4c7acdbeb2bb6': ('d1', 'Datunashvili1'), '87c4a91e21dabee1ce680dbaa4e0f9d5': ('gio1', 'Giorgi1')
        }

    def login(self):
        while True:
            log_name = input("Enter your nickname: ")
            log_password = input("Enter your password: ")
            # hashed reg_name to original text
            user_uuid = hashlib.md5(log_name.encode('utf-8')).hexdigest()
            
            if user_uuid in self.base:
                data = self.base[user_uuid]
                if data[1] == log_password:
                    print(f"user: {data[0]} has Logged in!")
                    break
                else:
                    print("Password is incorrect")
            else:
                print("User is not registered")

            q = input("press q to quit or press c to continue: ")
            if q.lower() == "q":
                break

    def register(self):
        while True:
            reg_name = input("Enter your nickname: ")
            nums = {str(i) for i in range(10)}
            if len(reg_name) == 0:
                print("Please write your nickname")
                continue
            elif len(nums.intersection(set(reg_name))) == 0:
                print("You need to add number in nickname")
                continue
            elif reg_name[0] in nums:
                print("Your pass should start with letter")
                continue
            break
        while True:
            reg_pass = input("Enter your password: ")
            text = reg_pass.upper()
            if len(reg_pass) < 6 or len(reg_pass) > 15 :
                print("Password length should be 6-15 characters")
                continue
            elif len(set(text).intersection(set(reg_pass))) == 0:
                print("Your password should contain at least 1 uppercase letter")
                continue
            break
        # hashing reg name
        user_uuid = hashlib.md5(reg_name.encode('utf-8')).hexdigest()
        
        self.base[user_uuid] = reg_name,reg_pass
        return reg_name,reg_pass


db = Database()
while True:
    print("Choose action")
    q = input("Login/Register: ")
    if q.lower() == "login":
        db.login()
    elif q.lower() == "register":
        user = db.register()
        print(f"User: '{user[0]}' succesfully registered")
    else:
        print("Wrong input:(")
    print(db.base)

    q = input("press q to quit or press c to continue: ")
    if q.lower() == "q":
        break
