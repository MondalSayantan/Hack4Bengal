import streamlit as st
from helpers import *
from main import skills

st.set_page_config(layout='wide')

st.markdown('''
<h1> Github Profile README Generator</h1>
<h3> 
''', unsafe_allow_html=True)


sbar = st.sidebar
sbar.subheader("Developer details:")
sbar.markdown(''' <a href = "https://www.linkedin.com/in/thisisshreykhandelwal/"> LinkedIn </a>/
<a href = "https://www.github.com/HawkingRadiation42"> Github 👨‍💻</a><br>
<a href = "https://www.linkedin.com/in/mondalsayantan/"> LinkedIn </a>/
<a href = "https://www.github.com/MondalSayantan"> Github 👨‍💻</a><br>''' , unsafe_allow_html=True)
page = sbar.radio("What do you want to do?",options=['Stay in the Home Page','Generate README'])

if page == 'Stay in the Home Page':
    st.subheader("Thank You for using this web app ~ ")
    st.markdown('''
    - To create README Click on 'Generate README' in the sidebar
    - Fill in the text boxes
    - When done, select the 'Generate README' Button
    - If you are happy with the Readme, you can download it
    ''')

if page == 'Generate README':
    st.subheader("Fill in your details: ")
    theme_list = ["default","solarized-light","dark", "radical", "merko", "gruvbox", "tokyonight", "onedark", "cobalt", "synthwave", "highcontrast", "dracula"]
    
    github_stats_type = sbar.selectbox(label="Chose Github Stats Card Type",options=['type-1','type-2','type-3'],index=1)
    
    github_stats_theme = ''
    if github_stats_type == 'type-3':
        github_stats_theme = sbar.selectbox(label="Select theme for GitHub Stats",options=theme_list)
    
    #isWaka = sbar.checkbox(label= "Include WakaTime Stats",value = True)
    #isBlog = sbar.checkbox(label= "Include Blog Posts",value = False)
    isJoke = sbar.checkbox(label= "Include Joke Card",value = True)
    joke_theme = sbar.selectbox(label="Select theme for Joke Card",options=theme_list)
    col1 , col2, col3 = st.columns(3)

    with col1:
        name = st.text_input("Name")
        twitter = st.text_input("Twitter")

    with col2:
        github = st.text_input("Github UserID")
        portfolio = st.text_input("Portfolio")

    with col3:
        linkedin = st.text_input("Linkedin userID")
        medium = st.text_input("Medium URL")

    p1_value = '''Web Frameworks, Open Source Projects...''' 
    p1 = st.text_area("I am currently working on", value=p1_value)

    p2_value = '''Backend Development,DevOps'''
    p2 = st.text_area("I am currently learning:", value = p2_value)

    p3_value = '''Hackathon, projects'''
    p3 = st.text_area("I am looking to collaborate on:", value = p3_value)

    p4_value = '''Python, JavaScript, Internship Opportunites, Open Source'''
    p4 = st.text_area("Talk to me about:",value = p4_value)

    user_skills = st.multiselect("Select Skills",options=skills,default=['python','c','c++','Mysql','FastAPI','java','OpenCV'])
    
    #st.markdown('<br>' , unsafe_allow_html = True) 
    img_url = st.text_input(label='Enter Banner Image to be added at the top of the README',value = 'https://cdn.neow.in/news/images/uploaded/2020/12/1608232185_github_logo_1.jpg')
    e3 = st.expander("Getting Image URL")
    with e3:
        st.markdown(''' 
    - Enter the URL to the image, ensure URL ends with an extension like '.png','.svg','.gif'
    - If you would like to use a downloaded image, upload the image to your GitHub repo
    - Click on the image file in your repo and click on either Download/Raw
    - Copy the URL of image
        ''')
    c1,c2 = st.columns(2)
    with c1:
        img_width = st.text_input(label='Enter Image witdh (include units % or px)',value = '100%')
    with c2:
        img_height = st.text_input(label='Enter Image height (include units % or px)',value = '250px')

    save = st.button("Generate README")
    if save:
        code = default_html(name = name, github_username = github,linkedin_url = linkedin,p1 = p1,p2 = p2,p3 = p3,p4 = p4,skills=user_skills,twitter_url=twitter,medium_url = medium, portfolio_url = portfolio,github_stats_theme = github_stats_theme,isJoke = isJoke,
        joke_theme = joke_theme,img_url = img_url, img_width= img_width, img_height = img_height, github_stats_type = github_stats_type)
        st.markdown(download_readme(code),unsafe_allow_html = True)
        st.markdown("---")
        st.markdown(f'''
        ```{code}```
        ''')
        st.markdown("---")
        st.markdown(code, unsafe_allow_html = True)
