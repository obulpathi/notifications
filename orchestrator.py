import os
import sys
from jinja2 import Environment, FileSystemLoader, meta


def render(sense, action):
    env = Environment(loader=FileSystemLoader('/src/templates/sense'))
    template_source = env.loader.get_source(env, sense+'.py')[0]
    parsed_content = env.parse(template_source)
    vars = meta.find_undeclared_variables(parsed_content)
    args = {}

    for var in vars:
        if "NOTIFICATIONS_" + var.upper() in os.environ:
            args[var] = os.environ["NOTIFICATIONS_" + var.upper()]
        else:
            print "Could not find NOTIFICATIONS_"+var.upper()+" in environment variables"
            exit()

    template = env.get_template(sense+'.py')
    render = template.render(**args)

    with open('/src/binpy/sense.py', 'w+') as fh:
        fh.write(render)

    env = Environment(loader=FileSystemLoader('/src/templates/action'))
    template_source = env.loader.get_source(env, action+'.py')[0]
    parsed_content = env.parse(template_source)
    vars = meta.find_undeclared_variables(parsed_content)
    args = {}

    for var in vars:
        if "NOTIFICATIONS_" + var.upper() in os.environ:
            args[var] = os.environ["NOTIFICATIONS_" + var.upper()]
        else:
            print "Could not find NOTIFICATIONS_"+var.upper()+" in environment variables"
            exit()

    template = env.get_template(action+'.py')
    render = template.render(**args)

    with open('/src/binpy/action.py', 'w+') as fh:
        fh.write(render)




if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])
    from binpy import action, sense
    result = sense.sense()
    if result[0]:
        action.action(result[1])





