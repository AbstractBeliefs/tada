from yapsy.IPlugin import IPlugin
import jinja2

class VacuumBackend(IPlugin):
    def output(self, pack):
        env = jinja2.Environment(
            trim_blocks=True,
            lstrip_blocks=True,
            loader=jinja2.FileSystemLoader("./templates")
        )

        vacuumTemplate = env.from_string(self.template)
        print vacuumTemplate.render(Emotes=pack)

    template = \
"""<?xml version='1.0' encoding='UTF-8'?>
<icondef>
    <name>{{ Emotes.name }}</name>
    <description> {{ Emotes.desc }} </description>
    <author>{{ Emotes.author }}</author>
    <version>{{ Emotes.version }}</version>

    {% for file in Emotes.emotelist %}
    <icon>
        {% for shortcut in file.shortcuts %}
        <text>{{ shortcut }}</text>
        {% endfor %}
        <object mime='{{ file.filetype }}'>{{ file.filename }}</object>
    </icon>

    {% endfor %}
</icondef>"""