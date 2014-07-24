from yapsy.IPlugin import IPlugin
import jinja2
import os

class glanterBackend(IPlugin):
    pack = None
    html = ""
        
    def build(self, pack):
        self.pack = pack
        print "[glanter] Building html..."
        self.buildhtml()
        print "[glanter] Installing site..."
        self.buildSite()

    def buildhtml(self):
        env = jinja2.Environment(
            trim_blocks=True,
            lstrip_blocks=True
        )

        glanterTemplate = env.from_string(self.template)
        self.html = glanterTemplate.render(Emotes=self.pack)

    def buildSite(self):
        os.system("rm glanter/*")

        index = open("glanter/index.html", 'w')
        index.write(self.html)
        index.close()

        os.system("cp input/*.png glanter/")
        os.system("cp input/*.gif glanter/")
        os.system("cp input/*.jpg glanter/") 
        pass

    template = \
"""<?xml version='1.0' encoding='UTF-8'?>
<html>
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
</html>"""
