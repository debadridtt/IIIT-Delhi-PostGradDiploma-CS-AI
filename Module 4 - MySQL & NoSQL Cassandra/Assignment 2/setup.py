from database import *
import csv
from datetime import datetime

if __name__ == "__main__":
    try:
        #Creating session object 
        session = session
        
        #Keyspace to be used for performing various operations
        KEYSPACE = keyspace_name

        #Setting Keyspace in the cassandra session
        #Code for setting session with cassandra database

        #Creating table 'Customer'
        create_customer_table_query = '''create table if not exists Customer(cust_id text primary key, first_name text, last_name text, registered_on timestamp);'''

        if execute_query(session, create_customer_table_query) is not None:
            print("Customer table is successfully created.")

        #Creating table 'Product'
        create_product_table_query = '''create table if not exists Product(prdt_id text primary key, title text);'''

        if execute_query(session, create_product_table_query) is not None:
            print("Product table is successfully created.")

        #Creating table 'Product_Liked_By_Customer'
        create_product_liked_by_customer_table_query = '''create table if not exists Product_Liked_By_Customer(cust_id text, first_name text, last_name text, liked_prdt_id text, liked_on timestamp, title text, primary key (liked_prdt_id, cust_id, liked_on));'''

        if execute_query(session, create_product_liked_by_customer_table_query) is not None:
            print("Product_Liked_By_Customer table is successfully created.")

        #Inserting Customer data in the table
        customer_data_insert_query = '''insert into customer (cust_id, first_name, last_name, registered_on) values ({0}, {1}, {2}, {3})'''
        with open("config/customers.csv", "r") as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                execute_query(session, customer_data_insert_query.format(
                    "'"+row[0]+"'", 
                    "'"+row[1]+"'", 
                    "'"+row[2]+"'", 
                    int(float(datetime.now().strftime("%s.%f"))) * 1000))
                
        #Inserting Product data in the table
        product_data_insert_query = '''insert into product (prdt_id, title) values ({0}, {1})'''
        with open("config/products.csv", "r") as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                execute_query(session, product_data_insert_query.format(
                    "'"+row[0]+"'", 
                    "'"+row[1]+"'"))
                
        #Inserting Product_Liked_By_Customer data in the table
        product_liked_by_customer_data_insert_query = '''insert into product_liked_by_customer (cust_id, first_name, last_name, liked_prdt_id, liked_on, title) values ({0}, {1}, {2}, {3}, {4}, {5})'''
        with open("config/product_liked_by_customer.csv", "r") as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                execute_query(session, product_liked_by_customer_data_insert_query.format(
                    "'"+row[0]+"'", 
                    "'"+row[1]+"'", 
                    "'"+row[2]+"'",
                    "'"+row[3]+"'",
                    int(float(datetime.now().strftime("%s.%f"))) * 1000,
                    "'"+row[4]+"'"))
                
    except Exception as e:
        print("Error in the execution : ", str(e))
        