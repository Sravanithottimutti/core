def check_access(func):
    def inner(username,role):
        if (role=="admin" or role=="manager" and username=="adim123"




                username=="manager123"):
            print("Access successfull")
            print("Username:",username)
            print("Role:",role)
            func(username,role)
        else:
            print("Access Denied")
    return inner
@check_access
def view_report(username,role):
    print(" ")
view_report("admin1234","admin")
view_report("manager123","hr")
