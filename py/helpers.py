import base64

def display_skills(skills,github_username):
    result = []

    for skill in skills:
        link = f'https://github.com/{github_username}?tab=repositories&q=&type=&language={skill}&sort='
        base = f'''<a href= {link} > <img width ='32px' src ='{'https://raw.githubusercontent.com/MondalSayantan/Hack4Bengal/main/resources/icons/'+skill+'.svg'}'> </a>'''
        result.append(base)
    return '\n'.join(result)

def display_socials(linkedin,twitter,medium,portfolio,github):
    result = ''
    if linkedin != '':
        linkedin = 'https://www.linkedin.com/in/'+linkedin
        result += f'''<a href = '{linkedin}'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/MondalSayantan/Hack4Bengal/main/resources/icons/linked-in-alt.svg"/></a> \n'''
    
    if twitter != '':
        twitter = 'https://www.twitter.com/'+twitter
        result += f'''<a href = '{twitter}'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/MondalSayantan/Hack4Bengal/main/resources/icons/twitter.svg"/></a> \n'''
    
    if medium != '':
        result += f'''<a href = '{medium}'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/MondalSayantan/Hack4Bengal/main/resources/icons/medium.svg"/></a> \n'''
    
    if portfolio != '':
        result += f'''<a href = '{portfolio}'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/MondalSayantan/Hack4Bengal/main/resources/icons/portfolio.png"/></a> \n'''    
    
    if github != '':
        github = 'https://www.github.com/'+github   
        result += f'''<a href = '{github}'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/MondalSayantan/Hack4Bengal/main/resources/icons/github.svg"/></a> \n'''
    return result

def show_github_stats(github_username,theme,choice = 'type-2'):
    if choice == 'type-1':
        return f'''![Metrics](https://metrics.lecoq.io/{github_username}?template=classic&config.timezone=America%2FToronto)'''

    if choice == 'type-2':
        return f'''![Metrics](https://metrics.lecoq.io/{github_username}?template=terminal&base.header=0&base.activity=0&base.repositories=0&base.metadata=0&languages=1&languages.limit=8&languages.colors=github&languages.threshold=0%25&config.timezone=America%2FToronto)'''
    
    return f'''<a href="https://github.com/anuraghazra/github-readme-stats">
<img align="left" src="https://github-readme-stats.vercel.app/api?username={github_username}&count_private=true&show_icons=true&theme={theme}" />
</a>
<a href="https://github.com/anuraghazra/convoychat">
<img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username={github_username}&theme={theme}" />
</a>'''

def show_joke(isJoke,theme):
    if isJoke:
        return f'''<h2> Some Programming Humor for you <img align ='center' src='https://media2.giphy.com/media/UQDSBzfyiBKvgFcSTw/giphy.gif?cid=ecf05e47p3cd513axbek3f56ti3jzizq8hincw20jauyyfyw&rid=giphy.gif' width = '32px'></h2>

![Jokes Card](https://readme-jokes.vercel.app/api?theme={theme})
'''
    else:
        return ''



def default_html(name = 'Shrey', linkedin_url = '',twitter_url = '',medium_url='',portfolio_url='',github_username = 'HawkingRadiation42',p1='......',p2='.......',p3='.........',p4='.........',skills=[],github_stats_theme = 'dark',isJoke = False,
joke_theme = 'dark',img_url = '',img_width='',img_height='',github_stats_type = 'type-1',isBlog = False):
    return f'''
<div align="center">
<img width="{img_width}" height = "{img_height}" src="{img_url}" alt="cover" />
</div>

<h1> Hello Fellow < Developers/ >! <img src = "https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width = 50px> </h1>
<p align='center'>

</p>
<div size='20px'> Hi! My name is {name}. Thank You for taking the time to view my GitHub Profile :smile: 
</div>

<h2> About Me <img src = "https://media0.giphy.com/media/KDDpcKigbfFpnejZs6/giphy.gif?cid=ecf05e47oy6f4zjs8g1qoiystc56cu7r9tb8a1fe76e05oty&rid=giphy.gif" width = 100px></h2>

<img width="55%" align="right" alt="Github" src="https://raw.githubusercontent.com/onimur/.github/master/.resources/git-header.svg" />


- ???? I???m currently working on {p1}

- ???? I???m currently learning {p2} 

- ???? I???m looking to collaborate on {p3} 

- ???? Talk to me about {p4} 

<h2> Skills <img src = "https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif?cid=ecf05e47a0n3gi1bfqntqmob8g9aid1oyj2wr3ds3mg700bl&rid=giphy.gif" width = 32px> </h2>
{display_skills(skills,github_username)}


<h2> Connect with me <img src='https://raw.githubusercontent.com/ShahriarShafin/ShahriarShafin/main/Assets/handshake.gif' width="100px"> </h2>
{display_socials(linkedin_url,  twitter_url,  medium_url, portfolio_url,  github_username)}


<h2> My GitHub Stats <img src='https://media1.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif?cid=ecf05e47x2g034i9pzwtzzsd3xgg2w9nr94t4tflbbgo3008&rid=giphy.gif' width='32px'> </h2>

{show_github_stats(github_username,github_stats_theme,github_stats_type)}

{show_joke(isJoke,joke_theme)}

<br>
<footer align='center'>README made with help of <a href='https://github.com/MondalSayantan/Hack4Bengal'>githubProfileReadmeGenerator</a> </footer>
'''


def download_readme(code):
    b64 = base64.b64encode(code.encode()).decode()
    href = f'<h4><a href="data:file/csv;base64,{b64}" download="README.md">Download README</a></h4>'
    return href
