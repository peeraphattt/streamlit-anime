import streamlit as st
import pandas as pd
from bing_image_urls import bing_image_urls
import matplotlib.pyplot as plt
st.markdown(
    f"""
       <style>
        .stApp{{
            background-image: url("https://wallpapercg.com/download/lakeside-3840x2160-4584.png"); #เปลี่ยน background
            background-repeat:  no-repeat;
            background-size: cover;
        }}
        .stTabs [aria-selected="true"] {{
            color:#fffff;
            padding: 5px 5px;
            border: 5px inset #ff6550;
        }}
        img{{
            width: 200px;
            height: 300px;
            object-fit: cover;
        }}
       </style>
       """,
    unsafe_allow_html=True
)
df = pd.read_csv("data/anime.csv")

def main_page():
    st.header("Home Page")
    st.sidebar.markdown("Home Page")
    columns = st.columns(3)
    for index, row in df.head(10).iterrows():
        card = columns[index % 3]
        card.image(bing_image_urls(row["name"], limit=1)[0], width=250)
        card.write(f':white[{row["name"]}]')
        card.caption(row["genre"])
    

def Search_page():
    st.header("Search Page")
    st.sidebar.markdown("Search Page")
    
    title = st.text_input('', 'One Piece')
    search_btn = st.button("Search", type="primary")
    if search_btn:
        name_mask = df['name'].str.contains(title, case=False)
        columns = st.columns(3)
        filtered_df = df[name_mask]
        for index, row in filtered_df.head(10).iterrows():
            card = columns[index % 3]
            card.image(bing_image_urls(row["name"], limit=1)[0], width=250)
            card.write(f':white[{row["name"]}]')
            card.caption(row["genre"])
    


def genre_page():
    st.header("Genre Page")
    st.sidebar.markdown("Genre Page")

    tab1,tab2,tab3,tab4,tab5 = st.tabs(['ความรัก','ต่อสู้','ครอบครัว','สยองขวัญ','สงคราม'])
    
    genre_input = st.text_input('', 'Drama')
    genre_btn = st.button("Search", type="primary")
    if genre_btn:
        df['genre'] = df['genre'].astype(str)
        name_mask = df['genre'].str.contains(genre_input, case=False)
        columns = st.columns(3)
        filtered_df = df[name_mask]
        for index, row in filtered_df.head(5).iterrows():
            card = columns[index % 3]
            card.image(bing_image_urls(row["name"], limit=1)[0], width=250)
            card.write(f':white[{row["name"]}]')
            card.caption(row["genre"])

def popular_page():
    st.header("Popular Page")
    st.sidebar.markdown("Popular Page")
    columns = st.columns(3)

    top_ten = df.sort_values('rating', ascending=False).head(5)
    for index, row in df.sort_values('rating', ascending=False).head(5).iterrows():
            card = columns[index % 3]
            card.image(bing_image_urls(row["name"], limit=1)[0], width=250)
            card.write(f':white[{row["name"]}]')
            card.caption(f"Rating:{row["rating"]}")

def episodes_page():
    st.header("Episodes Page")
    st.sidebar.markdown("Episodes Page")
    columns = st.columns(3)

    filtered_df = df[df['episodes'] != 'Unknown']
    top_ten = filtered_df.sort_values('episodes', ascending=False).head(5)

    columns = st.columns(3)

    for index, row in top_ten.iterrows():
        card = columns[index % 3]
        card.image(bing_image_urls(row["name"], limit=1)[0], width=250)
        card.write(f':white[{row["name"]}]')
        card.caption(f"Episodes:{row['episodes']}")

def privacy_page():
    st.header("Privacy Policy Page")
    st.sidebar.markdown("Privacy Policy Page")

    privacy_policy = """
If you wish to exercise any of these rights, please contact us using the information below.

    **1. Introduction**

    This Privacy Policy describes how your anime website ("Website") collects, uses, and discloses your personal information. It applies to all users of the Website. By accessing or using the Website, you agree to this Privacy Policy.

    **2. Information We Collect**

    We may collect the following types of information when you use the Website:
    Personal Information: Information that can be used to identify you, such as your name, email address, username, and password (if you create an account).
    Non-Personal Information: Information that cannot be used to identify you, such as your browser type, device type, operating system, IP address, and browsing history on our Website.
    
    **3.How We Use Your Information**
    We may use your information for the following purposes:
    To provide, operate, and maintain the Website.
    To personalize your experience on the Website.
    To respond to your inquiries and requests.
    To send you newsletters and other communications relating to the Website.
    To improve the Website and its features.
    To collect insights and analyze usage patterns on the Website.
    To protect the security and integrity of the Website.
    **4.Sharing Your Information**
    We may share your information with the following third-party service providers who help us operate the Website and provide services to you: Cloud hosting providers Email marketing platforms Analytics providers These third-party service providers are contractually obligated to keep your information confidential and secure and to use it only for the purposes we have authorized. We will not share your personal information with any other third party without your consent, except as required by law or to protect the rights, property, or safety of ourselves or others.
    
    **5.Cookies**
    We may use cookies and similar tracking technologies to collect and store information about your use of the Website. Cookies are small data files that are placed on your device when you visit a website. They can be used to remember your preferences, track your activity on the Website, and understand how you interact with the Website. You can control cookies through your web browser settings. Most web browsers allow you to refuse to accept cookies or to delete them after they have been placed on your device.
    
    **6.Data Retention**
    We will retain your information for as long as necessary to fulfill the purposes described in this Privacy Policy, unless a longer retention period is required or permitted by law.
    
    **7.Security**
    We take reasonable measures to protect your information from unauthorized access, disclosure, alteration, or destruction. However, no website or internet transmission is completely secure, so we cannot guarantee the security of your information.
    
    **8.Children's Privacy**
    Our Website is not intended for children under the age of 13. We do not knowingly collect personal information from children under 13. If you are a parent or guardian and you are aware that your child has provided us with personal information, please contact us.
    
    **9.Changes to this Privacy Policy**
    We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on the Website. You are advised to review this Privacy Policy periodically for any changes.
    
    **10.Your Rights**
    Depending on your location, you may have certain rights regarding your personal information. These rights may include the rights to access, rectify, erase, or restrict the processing of your personal information. You may also have the right to object to the processing of your personal information and the right to data portability.

    """

    st.markdown(privacy_policy)

def contact_page():
    st.header("Contact Page")
    st.sidebar.markdown("Contact Page")

    st.page_link("http://www.google.com", label="Facebook", icon="🌎")
    st.page_link("http://www.google.com", label="Line", icon="🌎")
    st.page_link("http://www.google.com", label="Github", icon="🌎", disabled=True)
    st.page_link("http://www.google.com", label="Gmail", icon="🌎", disabled=True)

def dashboard_page():
    st.header("Dashboard Page")
    st.sidebar.markdown("Dashboard Page")

    st.header("Rating Filter")
    min_rating = st.slider("Minimum Rating", df['rating'].min(), df['rating'].max(), df['rating'].mean())
    max_rating = st.slider("Maximum Rating", min_rating, df['rating'].max(), df['rating'].mean())

    filtered_df = df[df['rating'] >= min_rating][df['rating'] <= max_rating]
    avg_rating = filtered_df['rating'].mean()
    count_ratings = filtered_df.shape[0]

    st.markdown(f"**Average Rating:** {avg_rating:.2f}")
    st.markdown(f"**Number of Ratings:** {count_ratings:,}")

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.hist(filtered_df['rating'], bins=10, edgecolor='black')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Ratings')

    st.pyplot(fig)

page_names_to_funcs = {
    "Home": main_page,
    "Search Page": Search_page,
    "Genre Page": genre_page,
    "Popular Page":popular_page,
    "Episodes Page":episodes_page,
    "Privacy Page":privacy_page,
    "Contact Page":contact_page,
    "Dashboard Page":dashboard_page,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()