from SAR_crawler import *


# keeps files from queue.txt that have certain keyword, puts them in results
def keyword_filter(KEYWORD,PROJECT_NAME):
    u = 1
    results = set()
    for link in file2set(PROJECT_NAME + '/queue.txt'):
        link_lower = link.lower()
        if KEYWORD in link_lower:
            results.add(link)
            print(link)
            u += 1
    # print filtered urls to check
    #pdf_list = keyword_filter(KEYWORD,PROJECT_NAME)
    print(str(len(results)) + ' files left of original ')
    print(len(file2set(PROJECT_NAME + '/queue.txt')))
    set2file(results, PROJECT_NAME+'/pdf_list.txt')
    print('pdfs located in DOD_SARs/pdf_list.txt')

    return results
