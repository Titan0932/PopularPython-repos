from os import link
import requests
import pandas as pd
import plotly.express as px



url=url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'


python=requests.get(url)
data=python.json()


name=[]
stars=[]
ids=[]
repos_links=[]
for repos in data['items']:
    name.append(repos['name'])
    stars.append(repos['stargazers_count'])
    ids.append(repos['id'])
    repos_links.append(repos['owner']['html_url'])

d={'id':ids,'Link':repos_links}
df=pd.DataFrame(data=d)

fig=px.bar(df,x=name,y=stars,title='MOST POPULAR PYTHON REPOSITORIES BY STAR-COUNT',color=stars,hover_data=['id','Link'],
                
                labels={
                        'x':'Repository Names',
                        'y':'Star-Gazers Count',
                        'text':'What ups?',
                        
                } 
                )

fig.update_layout(

    font_family="Courier New",
    font_size=15,
    title_font_family="Times New Roman",
    title_font_color="red",
    title_font_size=25,
    xaxis_color='green',
    yaxis_color='purple',
    yaxis_showticklabels=True,
    plot_bgcolor="pink"
)


fig.show()

