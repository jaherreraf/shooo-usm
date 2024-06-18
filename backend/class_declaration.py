
class Users:
    def __init__(self,uid,name,lastname,username,email,admin,password,car_id,image,created_at,update_at):
        self.uid = uid
        self.name = name
        self.lastname = lastname
        self.username = username        
        self.email = email
        self.admin = admin
        self.password = password
        self.car_id = car_id
        self.image = image
        self.created_at = created_at
        self.update_at = update_at
    def print_json(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email,
            "admin": self.admin,
            "password": self.password,
            "car_id": self.car_id,
            "image": self.image,
            "created_at": self.created_at,
            "update_at": self.update_at,
        }  
class Products:
    def __init__(self,uid,title,description,price,amount,image,created_at,update_at):
        self.uid = uid
        self.title = title
        self.description = description
        self.price = price
        self.amount = amount
        self.image = image
        self.created_at = created_at
        self.update_at = update_at
    def print_json(self):
        return {
            "uid": self.uid,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "amount": self.amount,
            "image": self.image,
            "created_at": self.created_at,
            "update_at": self.update_at,
        }

class Cars:
    def __init__(self,uid,uid_product,uid_user,title,description,price,amount_product,image,created_at,update_at):
        self.uid = uid
        self.uid_product = uid_product
        self.uid_user = uid_user
        self.title = title
        self.description = description
        self.price = price
        self.amount_product = amount_product
        self.image = image      
        self.created_at = created_at
        self.update_at = update_at
    def print_json(self):
        return {
            "uid": self.uid,
            "uid_product": self.uid_product,
            "uid_user": self.uid_user,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "amount_product": self.amount_product,
            "image": self.image,
            "created_at": self.created_at,
            "update_at": self.update_at,
        }
