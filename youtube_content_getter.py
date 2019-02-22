import os
import sys
from bs4 import BeautifulSoup


def get_author_name(soup_object):
    return soup_object.contents[3].contents[3].contents[1].contents[3].contents[1].contents[1].contents[0]

# the contents arrays are one of the ways to navigate the html structure 
# unfortunately, it is not intuitive for someone else
def get_comment(soup_object):
    return soup_object.contents[3].contents[3].contents[3].contents[1].contents[2].contents[0]

# gets the list of comment objects according to their id
# returned type is an array  
def get_list_of_comments(soup):
    return soup.find_all(id="comment")


if __name__ == "__main__":
    # initiate soup
    page_name = sys.argv[1]
    f1 = open(page_name + '.html', 'r', encoding="utf-8")
    soup = BeautifulSoup(f1.read(), 'html.parser')


    comments = get_list_of_comments(soup)
    for obj in comments:
        author = get_author_name(obj).strip()
        comment = get_comment(obj)
        print(author)
        print(comment)
        print("\n")
