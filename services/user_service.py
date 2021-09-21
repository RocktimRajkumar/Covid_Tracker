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
        user.set_pincode(pincode)
        user.set_user_type(user_type)
        UserService.user_detail[UserService.__user_sequence] = user
        if user_type == "user":
            user_key = "userId"
        else:
            user_key = "adminId"
        return {user_key: UserService.__user_sequence}

    def get_user(self, user_id):
        for user_key in UserService.user_detail:
            user = UserService.user_detail[user_key]
            if user.get_user_id() == user_id:
                name = user.get_user_name()
                phone = user.get_phone()
                pincode = user.get_pincode()
                user_obj = {}
                user_obj["userId"] = user_id
                user_obj["name"] = name
                user_obj["phone"] = phone
                user_obj["pincode"] = pincode
                return user_obj
        return 'User not found'

    def get_all_user(self):
        users = []
        for user_key in UserService.user_detail:
            user = UserService.user_detail[user_key]
            user_id = user.get_user_id()
            name = user.get_user_name()
            phone = user.get_phone()
            pincode = user.get_pincode()
            user_obj = {}
            user_obj["userId"] = user_id
            user_obj["name"] = name
            user_obj["phone"] = phone
            user_obj["pincode"] = pincode
            users.append(user_obj)
        return {"users": users}
