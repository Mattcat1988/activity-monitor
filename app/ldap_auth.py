from ldap3 import Server, Connection, ALL

def authenticate(username, password):
    server = Server('ldap://your_ldap_server', get_info=ALL)
    conn = Connection(server, user=username, password=password)
    return conn.bind()
