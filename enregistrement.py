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
