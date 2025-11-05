from datetime import datetime


# Example 1 DataBase Connection
class DataBaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to Bank DataBase"
        return cls._instance


db1 = DataBaseConnection()
db2 = DataBaseConnection()
print(db1)
print(db1.connection)
print(db1 == db2)


# Example 2 Bank Transaction logging
class TransactionLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        record = f"[{timestamp}]{message}"
        self.logs.append(record)

    def get_logs(self):
        return self.logs


# Client Code:
def main():
    logger1 = TransactionLogger()
    logger1.log("New saving account created for client #123.")
    logger1.log("Transfer of $1,000 from Account #123 to Account #456.")

    logger2 = TransactionLogger()
    logger2.log("Loan payment received from client #456.")

    # Обидва логери — один і той самий об’єкт
    print("\nAll Logs:")
    print(logger2.get_logs())


if __name__ == "__main__":
    main()


# Example 3 Bank Session Manager
class SessionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.user_id = None
            cls._instance.token = None
        return cls._instance

    def login(self, user_id):
        if self.user_id is None:
            self.user_id = user_id
            self.token = f"TOKEN-{user_id}-1234"
            print(f"User {user_id} logged in succesfully.")
        else:
            print(f"User {user_id} is already logged on!")

    def logout(self, user_id):
        if self.user_id:
            print(f"User {user_id} logged out.")
            self.user_id = None
            self.token = None
        else:
            print("No active session to log out from")

    def get_session(self):
        return {"user_id": self.user_id, "token": self.token}


def main():
    session1 = SessionManager()
    session1.login("client001")
    print(session1.get_session())
    session1.logout("client001")
    print(session1.get_session())


if __name__ == "__main__":
    main()
