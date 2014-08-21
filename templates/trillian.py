from yapsy.IPlugin import IPlugin
import jinja2
import zipfile


class TrillianBackend(IPlugin):
    pack = None
    trillianzip = ""

    def build(self, pack):
        self.pack = pack
        print "[Trillian] Building xml file..."
        self.buildicondef()
        print "[Trillian] Building zip..."
        self.makeZip()

    def buildicondef(self):
        env = jinja2.Environment(
            trim_blocks=True,
            lstrip_blocks=True
        )

        TrillianTemplate = env.from_string(self.template)
        self.trillianzip = TrillianTemplate.render(Emotes=self.pack)

    def makeZip(self):
        outzip = zipfile.ZipFile("output/Trillian.zip", 'w')
        outzip.writestr("BerachsEmotePack-trillian/main.xml", self.trillianzip)
        outzip.writestr("BerachsEmotePack-trillian/desc.txt", "emot")
        for emote in self.pack.emotelist:
            try:
                outzip.write("input/"+emote.filename, "BerachsEmotePack-trillian/"+emote.filename)
            except OSError:
                # The underlying emote file isn't found
                # This throws varying errors, but are all OSError or subclasses
                pass
        outzip.close()


    template = \
"""{% for emote in Emotes.emotelist %}
<bitmap name="{{ emote.filename }}" file="../../stixe/plugins/Ponypack-trillian/{{ emote.filename }}" />
{% endfor %}
<prefs>
<control name="emoticons" type="emoticons">
<!-- Pones -->
<group text="Emotes" initial="1">
{% for emote in Emotes.emotelist %}
    {% for shortcut in emote.shortcuts %}
<emoticon text="{{ shortcut }}"><source name="{{ emote.filename}}" left="0" top="0" right="{{ emote.width }}" bottom="{{ emote.height }}" /></emoticon>
    {% endfor %}
{% endfor %}
</group>
<!-- Please include... --><!-- I totally have no idea what this does but it seems important -->
&Emoticon-Extensions;
&iniMenuItemColor;
&iniIconMenuItemSettings;
<settings name="Width" value="600"/>
<font name="section"                    source="ttfDefault"     type="&iniDefaultFontName;"     size="&iniDefaultFontSize;"     bold="1"/>
</control>
</prefs>
"""
