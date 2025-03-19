# import streamlit as st
# import json
# import pandas as pd
# from pymongo import MongoClient
# from bson import json_util, ObjectId

# # load_dotenv()
# # MONGO_URI = os.getenv("MONGO")  [ for local running ]
# st.set_page_config(page_title="MongoDB Admin Panel", layout = "wide")
# st.title("📦 MongoDB Interface")

# username = ""
# password = ""

# if "authenticated" not in st.session_state:
#     st.session_state["authenticated"] = False

# def login():
    
#     st.markdown("""
#         <style>
#             /* Hide the entire sidebar */
#             [data-testid="stSidebar"] {
#                 display: none;
#             }
#         </style>
#         """, unsafe_allow_html=True
#     )

#     username = st.text_input("👤 Username")
#     password = st.text_input("🔑 Password", type="password")

#     if st.button("Login"):
#         if password == st.secrets[username]:
#             st.session_state["authenticated"] = True
#             st.success("✅ Login successful! Redirecting...")
#             st.rerun()  
#         else:
#             st.error("❌ Invalid credentials. Try again.")


# if not st.session_state["authenticated"]:
#     login()
#     st.stop()  


# MONGO_URI = st.secrets["LINK"]

# client = MongoClient(MONGO_URI)


# # db_names = client.list_database_names()  [add if wanted]
# # selected_db = st.sidebar.selectbox("Select Database", db_names) [add if wanted]

# # selected_db = os.getenv("NAME")
# selected_db = st.secrets["LINK2"]

# if selected_db:
#     db = client[selected_db]

#     new_collection_name = st.sidebar.text_input("New Collection Name")
#     if st.sidebar.button("Create Collection"):
#         if new_collection_name:
#             db.create_collection(new_collection_name)
#             st.sidebar.success(f"Collection '{new_collection_name}' created successfully!")
#         else:
#             st.sidebar.error("Collection name cannot be empty.")


    

#     if username == st.secrets["allow"]:
#         collection_names = db.list_collection_names()
#         selected_collection = st.sidebar.selectbox("Select Collection", collection_names)
#     else:
#         selected_collection = password


    

#     if selected_collection:
#         collection = db[selected_collection]

#         operation = st.sidebar.radio("Select Operation", ["Find", "Insert", "Update", "Custom Query"])

#         if operation == "Find":
#             st.subheader("🔍 Find Documents")
#             query = st.text_area("Enter Query (JSON format)", "{}")
#             try:
#                 query_dict = json.loads(query)
#                 documents = list(collection.find(query_dict))
#                 df = pd.DataFrame(documents)
#                 if len(df) > 0:
#                     df["_id"] = df["_id"].astype(str) 
#                 st.dataframe(df)
#             except json.JSONDecodeError:
#                 st.error("Invalid JSON format")

#         elif operation == "Insert":
#             st.subheader("📝 Insert Document")
#             doc = st.text_area("Enter JSON Document")

#             if st.button("Run Query"):
#                 try:
#                     doc_dict = json.loads(doc)
#                     if isinstance(doc_dict, list):
#                         collection.insert_many(doc_dict)
#                         st.success("Documents inserted successfully!")
#                     else:
#                         collection.insert_one(doc_dict)
#                         st.success("Document inserted successfully!")
#                 except json.JSONDecodeError:
#                     st.error("Invalid JSON format")

#         elif operation == "Update":
#             st.subheader("✏️ Update Document")
#             filter_query = st.text_area("Enter Filter Query (JSON format)")
#             update_query = st.text_area("Enter Update Query (JSON format)")
#             if st.button("Run Query"):
#                 try:
#                     filter_dict = json.loads(filter_query)
#                     update_dict = {"$set": json.loads(update_query)}
#                     result = collection.update_many(filter_dict, update_dict)
#                     st.success(f"{result.modified_count} documents updated successfully!")
#                 except json.JSONDecodeError:
#                     st.error("Invalid JSON format")

#         elif operation == "Custom Query":
#             st.subheader("🛠 Run a Custom MongoDB Query")
#             query_code = st.text_area("Enter Python Code (using `collection`)")
#             if st.button("Run Query"):
#                 try:
#                     forbidden_keywords = ["delete_one", "delete_many", "drop"]
#                     if any(keyword in query_code.lower() for keyword in forbidden_keywords):
#                         st.error("❌ Deletion queries are not allowed in Custom Query.")            
#                     else:
#                         result = eval(query_code, {"collection": collection, "ObjectId": ObjectId})
#                         st.json(json.loads(json_util.dumps(result)))
#                 except Exception as e:
#                     st.error(f"Error: {e}")





import streamlit as st
import json
import pandas as pd
from pymongo import MongoClient
from bson import json_util, ObjectId

# load_dotenv()
# MONGO_URI = os.getenv("MONGO")  [ for local running ]
st.set_page_config(page_title="MongoDB Admin Panel", layout = "wide")
st.title("📦 MongoDB Interface")



MONGO_URI = st.secrets["LINK"]

client = MongoClient(MONGO_URI)


# db_names = client.list_database_names()  [add if wanted]
# selected_db = st.sidebar.selectbox("Select Database", db_names) [add if wanted]

# selected_db = os.getenv("NAME")
selected_db = st.secrets["LINK2"]

if selected_db:
    db = client[selected_db]

    new_collection_name = st.sidebar.text_input("New Collection Name")
    if st.sidebar.button("Create Collection"):
        if new_collection_name:
            db.create_collection(new_collection_name)
            st.sidebar.success(f"Collection '{new_collection_name}' created successfully!")
        else:
            st.sidebar.error("Collection name cannot be empty.")


    


    collection_names = db.list_collection_names()
    selected_collection = st.sidebar.selectbox("Select Collection", collection_names)



    

    if selected_collection:
        collection = db[selected_collection]

        operation = st.sidebar.radio("Select Operation", ["Find", "Insert", "Update", "Custom Query"])

        if operation == "Find":
            st.subheader("🔍 Find Documents")
            query = st.text_area("Enter Query (JSON format)", "{}")
            try:
                query_dict = json.loads(query)
                documents = list(collection.find(query_dict))
                df = pd.DataFrame(documents)
                if len(df) > 0:
                    df["_id"] = df["_id"].astype(str) 
                st.dataframe(df)
            except json.JSONDecodeError:
                st.error("Invalid JSON format")

        elif operation == "Insert":
            st.subheader("📝 Insert Document")
            doc = st.text_area("Enter JSON Document")

            if st.button("Run Query"):
                try:
                    doc_dict = json.loads(doc)
                    if isinstance(doc_dict, list):
                        collection.insert_many(doc_dict)
                        st.success("Documents inserted successfully!")
                    else:
                        collection.insert_one(doc_dict)
                        st.success("Document inserted successfully!")
                except json.JSONDecodeError:
                    st.error("Invalid JSON format")

        elif operation == "Update":
            st.subheader("✏️ Update Document")
            filter_query = st.text_area("Enter Filter Query (JSON format)")
            update_query = st.text_area("Enter Update Query (JSON format)")
            if st.button("Run Query"):
                try:
                    filter_dict = json.loads(filter_query)
                    update_dict = {"$set": json.loads(update_query)}
                    result = collection.update_many(filter_dict, update_dict)
                    st.success(f"{result.modified_count} documents updated successfully!")
                except json.JSONDecodeError:
                    st.error("Invalid JSON format")

        elif operation == "Custom Query":
            st.subheader("🛠 Run a Custom MongoDB Query")
            query_code = st.text_area("Enter Python Code (using `collection`)")
            if st.button("Run Query"):
                try:
                    forbidden_keywords = ["delete_one", "delete_many", "drop"]
                    if any(keyword in query_code.lower() for keyword in forbidden_keywords):
                        st.error("❌ Deletion queries are not allowed in Custom Query.")            
                    else:
                        result = eval(query_code, {"collection": collection, "ObjectId": ObjectId})
                        st.json(json.loads(json_util.dumps(result)))
                except Exception as e:
                    st.error(f"Error: {e}")

