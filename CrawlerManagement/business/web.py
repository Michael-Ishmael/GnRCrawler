__author__ = 'funhead'

import urllib2
import urlparse
from bs4 import BeautifulSoup


class WebsiteLocator:

    def __init__(self):
        self.rootSite = "http://companycheck.co.uk/company/"

    def find_website(self, company_ref):
        target_url = urlparse.urljoin(self.rootSite, company_ref)
        try:
            response = urllib2.urlopen(target_url)
            html = response.read()
            soup = BeautifulSoup(html)
            site_link = soup.find('div','website-area').a
            if site_link:
                if site_link.text == 'Add Website':
                    return {"success": False, "message": "Company doesn't have a website"}
                else:
                    return {"success": True, "url": site_link.get('href')}
            else:
                return {"success": False, "message": "Link area not found"}
        except Exception as ex:
            return {"success": False, "message": ex.message}

