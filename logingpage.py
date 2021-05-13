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

			elif task == "Entreprises":
				st.subheader("Profile entreprises")
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
