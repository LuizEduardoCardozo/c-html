import re
from pathlib import Path

commentRegex = "<!-"

def cHTML(html_file, output_html):
    print(output_html)
    html = open(html_file,"r")
    source = html.readlines()
    html.close()

    try:
        output = open(output_html,"w")
    except:
        Path.mkdir(output_html.parent,parents=True, exist_ok=True)
        output = open(output_html,"w")

    for line in source:
        if not (haveComment(line)):
            output.write(line)

def haveComment(line):
    if re.findall(commentRegex,line) != []:
        return True
