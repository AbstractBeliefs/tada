from yapsy.IPlugin import IPlugin
import jinja2
import zipfile

class VacuumBackend(IPlugin):
    def build(self, pack):
        self.pack = pack
        self.buildicondef()
        self.makeZip()

    def buildicondef(self):
        env = jinja2.Environment(
            trim_blocks=True,
            lstrip_blocks=True,
            loader=jinja2.FileSystemLoader("./templates")
        )

        vacuumTemplate = env.from_string(self.template)
        self.icondef = vacuumTemplate.render(Emotes=self.pack)

    def makeZip(self):
        outzip = zipfile.ZipFile("output/vacuum.zip", 'w')
        outzip.writestr("BerachsEmotePack-vacuum/icon.def.xml", self.icondef)
        for emote in self.pack.emotelist:
            try:
                outzip.write("input/"+emote.filename, "BerachsEmotePack-vacuum/"+emote.filename)
            except OSError:
                # The underlying emote file isn't found
                # This throws varying errors, but are all OSError or subclasses
                pass
        outzip.close()


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