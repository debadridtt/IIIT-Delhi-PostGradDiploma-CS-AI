from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

#AstraDB Client and Secret required for the connection
ASTRA_CLIENT_ID = 'lCQOWzxTZSbjSixFTbjKSgPK'
ASTRA_SECRET = 'hY8pqDZP4nKZ8-Ej9qTi4MWOusSJRHma1rvnXrqY_w9yl4DHJttXMf4HryX-Hg6Fex8TlM0f0W86,qO.h_+Nz6T.YNj+UbFsXGs6gl9sdFzlg-DPS5hqwOhrYUZfMJZA'

#Cloud Configuration
cloud_config= {
        'secure_connect_bundle': 'secure-connect-e-commerce-db.zip'
}

#Authentication Provider
auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID, ASTRA_SECRET)

#Method for creating session object based on cloud configuration and Auth Provider
def create_session():
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    return cluster

#session object whuch is used fot interacting with Cassandra database
cluster = create_session()
session = cluster.connect('e_commerce')

#Method for setting keyspace in the session
#Input Parameters:
#    Session object
#    Keyspace_name
keyspace_name = 'e_commerce'

def set_session_keyspace(session, keyspace_name):
    return session.set_keyspace(keyspace_name)

#Method for executing query using the given session object
#Input Parameters:
#    Session object
#    query for execution        
def execute_query(session, query):
    return session.execute(query)

#Method for executing single row query using the given session object
#Input Parameters:
#    Session object
#    query for execution         
def execute_single_row_query(session, query):
    return session.execute(query)

#Method for fetching table data using the given session object
#Input Parameters:
#    Session object
#    table name for which the data is to be fetched    
def show_table_data(session, table_name):
    return session.execute(query)
        
