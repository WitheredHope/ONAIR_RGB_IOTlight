import ts3

def getUserStatus():
    """
    Gets the given users status for:

    Speakers / Headphones - 
    Microphone -
    Away -
    """
    pass


if __name__ == "__main__":
    # USER, PASS, HOST, ...
    from def_param import *

    with ts3.query.TS3ServerConnection(HOST, PORT) as ts3conn:
        ts3conn.login(client_login_name=USER, client_login_password=PASS)
        ts3conn.use(sid=SID, virtual=True)
        resp = ts3conn.clientlist()
        clientList = resp.parsed
        #print(clientList)
        resp = ts3conn.clientinfo(clid=1046)
        clientInfo = resp.parsed[0]
        print("Client Nickname = "        + clientInfo.get("client_nickname"))
        print("Client Output Hardware = " + clientInfo.get("client_output_hardware"))
        print("Client Input Hardware = "  + clientInfo.get("client_input_hardware"))
        print("Client Recording = "       + clientInfo.get("client_is_recording"))
        print("Client Away = "            + clientInfo.get("client_away"))
        print("Client Is Talker = "       + clientInfo.get("client_is_talker"))
        



        

