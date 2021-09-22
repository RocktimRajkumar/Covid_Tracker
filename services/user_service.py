from utils.db_connect import connect


class UserService:

    def add_user(self, name, phone, pincode, user_type):
        con_obj = connect()
        cnx = con_obj.cursor()
        cnx.execute(
            f"insert into User(userName,phone,pincode,user_type) values('{name}','{phone}','{pincode}','{user_type}')")
        user_id = int(cnx.execute(
            "SELECT @@IDENTITY as id").fetchone()[0])
        cnx.commit()
        con_obj.close()
        return {"userId": user_id}
