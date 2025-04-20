import mysql.connector as msc
import streamlit as st

mydb = msc.connect(
    host="127.0.0.1",
    user="root",
    password="phe9B@rBit0ne",
    database="crud_op"
)

mycursor = mydb.cursor()
# print("Connection Established")


def main():
    st.set_page_config(
    page_title="CRUD OPERATIONS",
    page_icon="⚙",
    layout="wide"
    )

    st.title("CRUD OPERATIONS FOR MYSQL")

    # CRUD options
    option = st.sidebar.selectbox("Select an Operation",("Create", "Read", "Update", "Delete"))

    # Perform selected operation
    if option == "Create":
        st.subheader("Create a record")
        name = st.text_input("Enter name")
        email = st.text_input("Enter email")
        if st.button("Create"):
            sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
            val = (name, email)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record created successfully!")

    elif option == "Read":
        st.subheader("Read records")
        mycursor.execute("SELECT * FROM users")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Update":
        st.subheader("Update a record")
        id = st.number_input("Enter ID", min_value=1)
        name = st.text_input("Enter new name")
        email = st.text_input("Enter new email")
        if st.button("Update"):
            sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
            val = (name, email, id)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record updated successfully!")

    elif option == "Delete":
        st.subheader("Delete a record")
        id = st.number_input("Enter ID", min_value=1)
        if st.button("Delete"):
            sql = "DELETE FROM users WHERE id = %s"
            val = (id,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record deleted successfully!")




if __name__ == "__main__":
    main()