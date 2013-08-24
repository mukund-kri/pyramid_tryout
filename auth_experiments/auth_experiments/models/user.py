from .base import BaseModel


class User(BaseModel):

    @staticmethod
    def add(username, firstname, lastname, password):
        # Add to db
        return
    

    # For Auth ----------------------------------------------------------------
    @staticmethod
    def valid_user(username, password):
        db = User.db
        print(db)
        return True

    @staticmethod
    def user_group(username, request):
        return ['admin']


    
