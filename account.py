class account:
    def check_password_lenght(self, password):
        if len(password) > 8:
            return True
        else:
            return False

if __name__ == '__main__':
    accVerify = account()
    print( 'the password length is ' + str(accVerify.check_password_length('hi')))
