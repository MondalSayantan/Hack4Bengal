import base64
from unittest import result

def display_skills(skills, github_username):
    result=[]

    for skill in skills:
        link = f'https://github.com/{github_username}?tab=repositories&q=&type=&language={skill}&sort='
        base = f'''<a href= {link} > <img width ='32px' src ='{'https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/'+skill+'.svg'}'> </a>'''
        result.append(base)
    return '\n'.join(result)


