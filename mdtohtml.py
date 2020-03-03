#!/usr/bin/env python3
import markdown
from jinja2 import Template

md = markdown.Markdown()

with open('README.md') as r:
    readme = r.read()

with open('templates/template.html') as t:
    template = Template(t.read())

with open('docs/index.html', 'w') as i:
    i.write(template.render(body=md.convert(readme)))
