import ts3


def connect(HOST, PORT, USER, PASS, SID):
    global ts3conn
    try:
        with ts3.query.TS3ServerConnection(HOST, PORT) as ts3conn:
            try:
                ts3conn.login(client_login_name=USER, client_login_password=PASS)
            except:
                print("Login Failed")
            finally:
                ts3conn.use(sid=SID, virtual=True)
    except:
        print("Connection Failed")



if __name__ == "__main__":
    from def_param import *
    #HOST = "" 
    #PORT = ""
    #USER = ""
    #PASS = ""
    #SID  = ""


    connect(HOST, PORT, USER, PASS, SID)
    
    print(ts3conn.clientlist().parsed)