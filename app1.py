import streamlit as st
import pandas as pd

# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False






def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""

	st.title("Simple Login App")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")
					create_table()
					blog_RC = st.text_input('Enter Notes RC')
					blog_Société = st.text_input("Enter Société",max_chars=50)
					blog_Secteur = st.text_input('Enter Notes Secteur')
					blog_Activités = st.text_area("Enter Your Activités",height=200)
					blog_Adresse = st.text_input("Enter Adresse",max_chars=50)
					blog_Téléphone = st.text_input("Enter Téléphone",max_chars=50)
					blog_Région = st.text_input("Enter Région",max_chars=50)
					if st.button("Add"):
					    import requests
					    response = requests.get("http://ip-api.com/json/").json()
					    blog_Longitude= response['lon']
					    blog_Latitude = response['lat']
					    add_data(blog_RC,blog_Société,blog_Secteur,blog_Activités,blog_Adresse,blog_Téléphone,blog_Région,blog_Latitude,blog_Longitude)
					    st.success("Post::'{}' Saved".format(blog_RC))
					
                  

				elif task == "Analytics":
					st.subheader("Analytics")
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")








if __name__ == '__main__':
	main()
