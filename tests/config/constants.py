# It will contain all the URL's
# We are using static method because we can use it directly via class name( You dont have to create an object)

class Constants:
    def __init__(self):
        print("Constants are loaded")

    @staticmethod
    def login_url():
        return "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    @staticmethod
    def dashboard_url():
        return "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

