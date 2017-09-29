#from newboston youtube series

import os


# repository for links from a website
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

create_directory('DOD_SARs')


# initialize queue file with first URL and empty crawled file
def initialize_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')


# function to write data to txt file
def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()



# add data to existing file
def append_data(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')


# overwrites existing file with empty one of the same name (clears contents)
def delete_contents(path):
    with open(path,'w'):
        pass

#speed up crawler using sets:


#convert each line of file to set
def file2set(file_name):
    results = set() #initialize empty set
    with open(file_name, 'rt') as f:  #'rt' = read text
        for line in f:
            results.add(line.replace('\n',''))
    return results


#convert set to file, each item is a new line
def set2file(links,file):
    delete_contents(file)
    for link in sorted(links):
        append_data(file,link)


