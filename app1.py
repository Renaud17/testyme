import sqlite3
import fxc
import streamlit as st
import pandas as pd 
import geocoder


import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dealtable(RC TEXT,Société TEXT,Secteur TEXT,Activités TEXT,Adresse TEXT,Téléphone TEXT,Région TEXT,Image LONGBLOB,Latitude TEXT,Longitude TEXT)')


def add_data(RC,Société,Secteur,Activités,Adresse,Téléphone,Région,Longitude,Latitude):
    c.execute('INSERT INTO dealtable(RC,Société,Secteur,Activités,Adresse,Téléphone,Région,Image,Latitude,Longitude) VALUES (?,?,?,?,?,?,?,?,?,?)',(RC,Société,Secteur,Activités,Adresse,Téléphone,Région,Image,Longitude,Latitude))
    conn.commit()




def view_all_notes():
    c.execute('SELECT * FROM dealtable')
    data = c.fetchall()
    # for row in data:
    #   print(row)
    return data


def view_all_Secteur():
    c.execute('SELECT DISTINCT Secteur FROM dealtable')
    data = c.fetchall()
    # for row in data:
    #   print(row)
    return data


def get_single_Sec(Secteur):
    c.execute('SELECT * FROM dealtable WHERE Secteur="{}"'.format(Secteur))
    data = c.fetchall()
    return data


def get_blog_by_RC(RC):
    c.execute('SELECT * FROM dealtable WHERE RC="{}"'.format(RC))
    data = c.fetchall()
    return data    


def get_blog_by_Soc(Société):
    c.execute('SELECT * FROM dealtable WHERE Société="{}"'.format(Société))
    data = c.fetchall()
    return data

def get_blog_by_Sec(Secteur):
    c.execute('SELECT * FROM dealtable WHERE Secteur="{}"'.format(Secteur))
    data = c.fetchall()
    return data

def get_blog_by_Act(Activités):
    c.execute("SELECT * FROM dealtable WHERE Activités like '%{}%'".format(Activités))
    data = c.fetchall()
    return data


def get_blog_by_Adr(Adresse):
    c.execute('SELECT * FROM dealtable WHERE Adresse="{}"'.format(Adresse))
    data = c.fetchall()
    return data


def get_blog_by_Tel(Téléphone):
    c.execute('SELECT * FROM dealtable WHERE Téléphone="{}"'.format(Téléphone))
    data = c.fetchall()
    return data


def get_blog_by_Reg(Région):
    c.execute('SELECT * FROM dealtable WHERE  Région="{}"'.format( Région))
    data = c.fetchall()
    return data

def get_blog_image(Image):
    c.execute('SELECT * FROM dealtable WHERE  Image="{}"'.format( Image))
    data = c.fetchall()
    return data

def get_blog_by_lat(Latitude):
    c.execute('SELECT * FROM dealtable WHERE  Latitude="{}"'.format( Latitude))
    data = c.fetchall()
    return data    

def get_blog_by_long(Longitude):
    c.execute('SELECT * FROM dealtable WHERE  Longitude="{}"'.format( Longitude))
    data = c.fetchall()
    return data



def edit_blog_RC(RC,new_RC):
    c.execute('UPDATE dealtable SET RC ="{}" WHERE RC="{}"'.format(RC,new_RC))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_Soc(Société,new_Société):
    c.execute('UPDATE dealtable SET Société ="{}" WHERE Société="{}"'.format(Société,new_Société))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_Sec(Secteur,new_Secteur):
    c.execute('UPDATE blogtable SET title ="{}" WHERE title="{}"'.format(Secteur,new_Secteur))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_Act(Activités,new_Activités):
    c.execute('UPDATE dealtable SET Activités ="{}" WHERE Activités="{}"'.format(Activités,new_Activités))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_Adr(Adresse,new_Adresse):
    c.execute('UPDATE dealtable SET Adresse ="{}" WHERE Adresse="{}"'.format(Adresse,new_Adresse))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_Tel(Téléphone,new_Téléphone):
    c.execute('UPDATE dealtable SET Téléphone ="{}" WHERE Téléphone="{}"'.format(Téléphone,new_Téléphone))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_Reg(Région,new_Région):
    c.execute('UPDATE dealtable SET Région ="{}" WHERE Région="{}"'.format(Région,new_Région))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_image(Image,new_Image):
    c.execute('UPDATE dealtable SET RC ="{}" WHERE RC="{}"'.format(Image,new_Image))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_long(Longitude,new_Longitude):
    c.execute('UPDATE dealtable SET RC ="{}" WHERE RC="{}"'.format(Longitude,new_Longitude))
    conn.commit()
    data = c.fetchall()
    return data

def edit_blog_lat(Latitude,new_Latitude):
    c.execute('UPDATE dealtable SET RC ="{}" WHERE RC="{}"'.format(Latitude,new_Latitude))
    conn.commit()
    data = c.fetchall()
    return data


def delete_data(RC):
    c.execute('DELETE FROM blogtable WHERE RC="{}"'.format(RC))
    conn.commit()


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
				st.subheader("Votre enregistrement")
				create_table()
				blog_RC = st.text_input('Enter Notes RC')
				blog_Société = st.text_input("Enter Société",max_chars=50)
				blog_Secteur = st.text_input('Enter Notes Secteur')
				blog_Activités = st.text_area("Enter Your Activités",height=200)
				blog_Adresse = st.text_input("Enter Adresse",max_chars=50)
				blog_Téléphone = st.text_input("Enter Téléphone",max_chars=50)
				blog_Région = st.text_input("Enter Région",max_chars=50)
				blog_image = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
				if st.button("Add"):
				    import requests
				    response = requests.get("http://ip-api.com/json/").json()
				    blog_Longitude= response['lon']
				    blog_Latitude = response['lat']
				    add_data(blog_RC,blog_Société,blog_Secteur,blog_Activités,blog_Adresse,blog_Téléphone,blog_Région,blog_image,blog_Latitude,blog_Longitude)
				    st.success("Post::'{}' Saved".format(blog_RC))
				
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
