"""Simple Login App"""

st.title("Simple Login App")

menu = ["Login","SignUp"]
choice = st.sidebar.selectbox("Menu",menu)

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
			if st.button("Add"):
			    import requests
			    response = requests.get("http://ip-api.com/json/").json()
			    blog_Longitude= response['lon']
			    blog_Latitude = response['lat']
			    add_data(blog_RC,blog_Société,blog_Secteur,blog_Activités,blog_Adresse,blog_Téléphone,blog_Région,blog_Latitude,blog_Longitude)
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
