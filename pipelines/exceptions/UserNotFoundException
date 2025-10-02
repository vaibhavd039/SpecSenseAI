class UserNotFoundException(Exception):
    def __init__(self, user_id):
        message = f"No User Found for ID: {user_id}"
        super().__init__(message)
        self.user_id = user_id