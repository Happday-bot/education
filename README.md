# education
**Student Development Program**

# MongoDB High-Level Interface

## 📌 Overview
This is a **Streamlit-based MongoDB Admin Panel** that provides a user-friendly interface for performing CRUD operations on MongoDB without using the Mongo shell. The interface includes:

✅ Database & Collection Selection  
✅ **Find (Read) Documents**  
✅ **Insert (Create) Documents**  
✅ **Update Documents**  
✅ **Run Custom Queries** (excluding delete operations)  
✅ **Create New Collections**  

---

## 🚀 Setup & Installation

### **1️⃣ Clone the Repository**
```sh
git clone <repo-url>
cd <repo-folder>
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**
Create a `.env` file and add your MongoDB connection string:
```env
MONGO=mongodb+srv://username:password@cluster-url/dbname
```

### **4️⃣ Run the Application**
```sh
streamlit run app.py
```

---

## 📌 Features & Usage

### **1️⃣ Database & Collection Selection**
- Select a database from the dropdown list.
- Choose a collection to perform operations.

### **2️⃣ Find (Read) Documents**
- Enter a query in **JSON format**.
- Results will be displayed in **table format**.

### **3️⃣ Insert (Create) Documents**
- Enter a document in **JSON format**.
- Supports **single & multiple document insertion**.

### **4️⃣ Update Documents**
- Provide a **filter query** to match documents.
- Enter the **update query** in JSON format.
- Uses **`$set`** for field updates.

### **6️⃣ Custom Queries**
- Write a custom query using `collection`.
- **Deletion queries (`delete_one`, `delete_many`, `drop`) are not allowed.**

### **7️⃣ Create New Collection**
- Enter a name for the new collection.
- Click **Create Collection** to add it.

---

## 🔒 Security Measures
- **Environment Variables**: MongoDB credentials are stored in `.env`.
- **Restricted Queries**: Deletion queries are blocked in the custom query section.

---

## 🛠 Troubleshooting
**Issue:** Streamlit is not recognized as a command.  
**Solution:** Try running:
```sh
python -m streamlit run app.py
```

**Issue:** MongoDB connection errors.  
**Solution:** Ensure the **MongoDB URI** in `.env` is correct and accessible.

---

## 📜 License
This project is open-source and available under the **Apache License 2.0**.

---

## ✨ Author
Developed by **Alfred Sam D** 🚀

