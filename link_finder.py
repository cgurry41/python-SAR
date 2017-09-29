from html.parser import HTMLParser
from urllib import parse

# add methods to HTMLParser
class LinkFinder(HTMLParser):
    # call superclass' initialization method
    def __init__(self, base_url, page_url):
        super(LinkFinder, self).__init__()
        #account for relative links in HTML tests
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self,tag,attrs):
        if tag == 'a':   #indicates a link follows
            for (attribute,value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url,value)
                    self.links.add(url)

    def page_links(self):
        return self.links


finder = LinkFinder('dod.mil','http://www.esd.whs.mil/FOIA/Reading-Room/Reading-Room-List/Selected_Acquisition_Reports/')