

class User(object):

    @staticmethod
    def add(username, firstname, lastname, password):
        # Add to db

        return
    

    # For Auth ----------------------------------------------------------------
    @staticmethod
    def valid_user(username, password):
        return True

    @staticmethod
    def user_group(username, request):
        return ['admin']


    
