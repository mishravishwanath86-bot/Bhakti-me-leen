import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# check head
head_end = html.find('</head>')
print("</head> found at index:", head_end)

# check end of page-home
page_home_end = html.find('</section>', html.find('id="page-home"'))
print("End of page-home at index:", page_home_end)
print("Snippet around page-home end:")
print(html[page_home_end-150:page_home_end+50])
