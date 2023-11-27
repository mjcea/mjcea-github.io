from jinja2 import Environment, FileSystemLoader
import json

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

secoes = json.load(open('tibia-news.json'))

for i in range(len(secoes)):
    print("noticia: "+ str(i))
    secoes[i]['date'] = secoes[i]['date'].replace("Jun", "Junho")
    secoes[i]['text'] = secoes[i]['text'].replace("\u2192", " ")


html_output = template.render(secoes=secoes)

with open('index.html', 'w') as file:
    file.write(html_output)