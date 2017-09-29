import threading
from queue import Queue
from spider import Spider
from SAR_crawler import *


PROJECT_NAME = 'DOD_SARs'
HOMEPAGE = 'http://www.esd.whs.mil/FOIA/Reading-Room/Reading-Room-List/Selected_Acquisition_Reports/'
DOMAIN_NAME = 'esd.whs.mil/' # get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
KEYWORD = 'selected' # search word for filtering relevant urls
NUMBER_OF_THREADS = 2
queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME) # first spider crawls HOMEPAGE and creates dir + files
print('pdfs and links in DOD_SARs/queue.txt')

# # create worker threads (will die when main exits)
# def create_workers():
#     for _ in range(NUMBER_OF_THREADS):
#         t = threading.Thread(target=work)
#         t.daemon = True # die when the main exits
#         t.start()
#
#
# # Do the next job in the queue
# def work():
#     while True:
#         url = queue.get()
#         Spider.crawl_page(threading.current_thread().name,url)
#         queue.task_done()
#
#
# # Each queued link is a new job, compatible for threads
# def create_jobs():
#     for link in file2set(QUEUE_FILE):
#         queue.put(link)
#     queue.join() # lock each thread until next one is done
#     crawl()
#
#
# # check if items in queue --> crawl them
# def crawl():
#     queued_links = file2set(QUEUE_FILE)
#     if len(queued_links) > 0:
#         print(str(len(queued_links)) + ' links in the queue')
#         create_jobs()
#
#
# create_workers()
# crawl()

from search_links import keyword_filter
keyword_filter(KEYWORD,PROJECT_NAME)
#
from pdf_downloader import *
#
from pdf_filter import *

from pdf_2_text import *
