from yapsy.IPlugin import IPlugin
import jinja2
import zipfile


class AdiumBackend(IPlugin):
    
    template = \
"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>AdiumSetVersion</key>
    <integer>1</integer>

    <key>Emoticons</key>
    <dict>

        {% for file in Emotes.emotelist %}
        <key>{{ file.filename }}</key>
        <dict>
            <key>Equivalents</key>
            <array>
                {% for shortcut in file.shortcuts %}
                <string>{{ shortcut }}</string>
                {% endfor %}
            </array>
            <key>Name</key>
            <string>{{ file.filename }}</string>
        </dict>
        {% endfor %}

    </dict>
</dict>
</plist>"""
