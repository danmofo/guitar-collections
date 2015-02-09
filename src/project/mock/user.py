from project.models import User

dummy_users = [
    User('admin', 'd@d.com', 'password'),
    User('user123', 'user123@123.com', 'password'),
    User('super', 'd@dan.com', 'password', 2)
]
