from model.user import User


class UserService:
    __user_sequence = 0
    user_detail: User = {}

    def add_user(self, name, phone, pincode, user_type):
        user = User()
        UserService.__user_sequence += 1
        user.set_user_id(UserService.__user_sequence)
        user.set_user_name(name)
        user.set_phone(phone)
        user.set_user_type(user_type)
        UserService.user_detail[UserService.__user_sequence] = user
        if user_type == "user":
            user_key = "userId"
        else:
            user_key = "adminId"
        return {user_key: UserService.__user_sequence}

    def get_user(self, user_id):
        for user in UserService.user_detail:
            if user.get_user_id() == user_id:
                return user
        return 'User not found'
