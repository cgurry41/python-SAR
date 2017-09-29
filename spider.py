from urllib.request import urlopen

from link_finder import LinkFinder
from SAR_crawler import *


class Spider:

    # initialize class variable shared by all spider instances
    project_name = 'DOD_SARs'
    base_url = 'http://www.esd.whs.mil/FOIA/Reading-Room/Reading-Room-List/Selected_Acquisition_Reports/'
    domain_name = 'esd.whs.mil/FOIA' # make sure we are connecting to valid web page
    queue_file = ''  # text version of queue set (hard drive as opposed to RAM)
    crawled_file = ''  # text version of crawled set (hard drive as opposed to RAM)
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('first spider', Spider.base_url)

    @staticmethod
    def boot():
        create_directory(Spider.project_name)
        initialize_files(Spider.project_name, Spider.base_url)
        Spider.queue = file2set(Spider.queue_file)
        Spider.crawled = file2set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)  # update set
            Spider.crawled.add(page_url)  # update file
            Spider.update_files()  # set to file

    @staticmethod
    def gather_links(page_url):
        html_string = ''  # convert bits to string
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'application/pdf' or 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)  # parses HTML and returns links
        except:
            print('Error: cannot crawl page')
            return set()  # no links on the page, return empty set
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set2file(Spider.queue, Spider.queue_file)
        set2file(Spider.crawled, Spider.crawled_file)

