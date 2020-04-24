import  requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# print("Status code:",r.status_code)

#将API响应储存在一个变量中
response_dict = r.json()

print(response_dict.keys())
print('Respositories returned:', response_dict['total_count'])

repo_dicts = response_dict['items']

# for key in repo_dict.keys():
#     print(key)
#
# #研究第一个仓库
# repo_dict = repo_dicts[0]
# print('\nSelected information about first repository:')
# print('Owner:',repo_dict['owner']["login"])
# print('Stars:',repo_dict['stargazers_count'])
# print('Repository:',repo_dict['html_url'])
# print('Created:',repo_dict['created_at'])
# print('Update:',repo_dict['updated_at'])
# print('Description:',repo_dict['description'])


# #研究各仓库

# print('\nSelected information about each repository:')
# n=1
# for repo_dict in repo_dicts:
#     print('\nName:',repo_dict['name'])
#     print('Num:', n)
#     print('Owner:', repo_dict['owner']["login"])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     # print('Created:', repo_dict['created_at'])
#     # print('Update:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])
#     n+=1


'''数据可视化'''
names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

'''可视化'''
my_style = LS('#336699',base_style=LCS)

my_config=pygal.Config()
my_config.x_label_rotation=-45
my_config.show_legend = False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=24
my_config.struncate_label=15
my_config.show_y_guides=False
my_config.width=1000
chart=pygal.Bar(my_config,style=my_style)
chart.title='most-starred python projects on github'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos.svg')
