import ts3

def getClientStatus(clid):
    """
    Gets the given users status for:

    Speakers / Headphones - 
    Microphone -
    Away -
    Recording
    """
    resp = ts3conn.clientinfo(clid=clid)
    clientInfo = resp.parsed[0]
    clientStatus = {
        "nickname" : clientInfo.get("client_nickname"),
        "micMuted" : bool(clientInfo.get("client_input_muted")),
        "speakerMuted" : bool(clientInfo.get("client_output_muted")),
        "recording" : bool(clientInfo.get("client_is_recording")),
        "away" : bool(clientInfo.get("client_away"))
    }
    return(clientStatus)


if __name__ == "__main__":
    # USER, PASS, HOST, ...
    from def_param import *

    with ts3.query.TS3ServerConnection(HOST, PORT) as ts3conn:
        ts3conn.login(client_login_name=USER, client_login_password=PASS)
        ts3conn.use(sid=SID, virtual=True)
        resp = ts3conn.clientlist()
        clientList = resp.parsed
        print(clientList)
        print(getClientStatus(1))
        



        

