# encoding: utf-8

import sys
import xml.etree.ElementTree as ET
from workflow import Workflow, ICON_WEB, web

def main(wf):
    url = "http://feed.smzdm.com/"
    r = web.get(url)
    r.raise_for_status()

    root = ET.fromstring(r.text.encode('utf8'))
    for ele in root.findall('.//item'):
        title = ele.find('title').text.strip()
        href = ele.find('link').text.strip()
        wf.add_item(title = title,
            subtitle = href,
            arg = href,
            valid = True,
            icon = ICON_WEB)
    wf.send_feedback()


if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
