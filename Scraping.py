import requests
import bs4
from urllib.request import urlopen as uReq
import string
import re
import os
from bs4 import BeautifulSoup as soup
# os.environ["TF_FORCE_GPU_ALLOW_GROWTH"]="true"
# %matplotlib inline


def scrape(url_list):
    import requests
    import bs4
    from urllib.request import urlopen as uReq
    import string
    import re
    import os
    from bs4 import BeautifulSoup as soup
    
    """
    This function scrapes used unlocked mobile phones product data descriptions from multiple pages at newegg.com 
    """
    no_prod = []
    descriptions = []
    for url in url_list:
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        containers = page_soup.find_all("div", {"class":"item-container"})  #"Selecting the inspection text of products "
        no_prod.append(len(containers))                                                        # "Returns the number of products on the webpage "

    #Looping through containers of every page to get the product description 
        for container in containers:
            a = [container.a.img["title"]]
            descriptions.append(a)
    return descriptions


def scrape_clothes(dict_url):
    descriptions = []
    
    for url, pages in dict_url.items():
        """ Check if there are multiple pages; if no, gather data from the current page else loop through all the pages """
        if pages == 0:
            uClient = uReq(url)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            containers = page_soup.find_all("a", {"class":"productBlock_link"})

            list_ = []
            for i in containers:
                list_.append(main_ + i['href'])

            for link in list_:
                uClient = uReq(link)
                page_html = uClient.read()
                uClient.close()
                page_soup = soup(page_html, "html.parser")
                containers = page_soup.find_all("div", {"class":"productDescription_synopsisContent"})

                for desc in containers:
                    descriptions.append(remove_tags(str(desc.p)))
        
        else:
            uClient = uReq(url)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            containers = page_soup.find_all("a", {"class":"productBlock_link"})

            list_ = []
            for i in containers:
                list_.append(main_ + i['href'])

            for link in list_:
                uClient = uReq(link)
                page_html = uClient.read()
                uClient.close()
                page_soup = soup(page_html, "html.parser")
                containers = page_soup.find_all("div", {"class":"productDescription_synopsisContent"})

                for desc in containers:
                    descriptions.append(remove_tags(str(desc.p)))

            for page in range(2 ,pages+1):
                url_pages = url+"&pageNumber="+str(page)
                uClient = uReq(url)
                page_html = uClient.read()
                uClient.close()
                page_soup = soup(page_html, "html.parser")
                containers = page_soup.find_all("div", {"class":"productDescription_synopsisContent"})

                for desc in containers:
                    descriptions.append(remove_tags(str(desc.p)))
            
    return descriptions
