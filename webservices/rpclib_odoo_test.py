import jsonrpclib

HOST = 'desktop-msh40ca.grupomeyko.hn'
PORT = 8069
DB = 'odoodb'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# server proxy object
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
server = jsonrpclib.Server(url)

# log in the given database
uid = server.call(service="common", method="login", args=[DB, USER, PASS])

# helper function for invoking model methods
def invoke(model, method, *args):
    args = [DB, uid, PASS, model, method] + list(args)
    return server.call(service="object", method="execute", args=args)

# create a new note
args = {
    'name' : 'Course Odoo RPC'
}
note_id = invoke('openacademy.course', 'create', args)
