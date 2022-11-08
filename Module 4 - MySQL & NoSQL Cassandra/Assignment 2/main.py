from database import *
import warnings
warnings.filterwarnings('ignore')

if __name__ == "__main__":
    try:
        
        #Creating session object 
        session = session
        
        #Keyspace to be used for performing various operations
        KEYSPACE = keyspace_name

        #Setting Keyspace in the cassandra session
        #Code for setting session with cassandra database
         
        #Getting Count of Products in the database
        row = execute_single_row_query(session, "select count(prdt_id) from product;")
        print("No of Products in database are : ", row[0][0])
        
        #Getting Count of Customers in the database
        row = execute_single_row_query(session, "select count(cust_id) from customer;")
        print("No of Customer in database are : ", row[0][0])
        
#         #Getting count of product wise likes by customer
        rows = execute_query(session, "select count(cust_id), title from product_liked_by_customer group by liked_prdt_id;")
        
        for row in rows:
            print(row)
            
    except Exception as e:
        print("Error in the execution : ", str(e))