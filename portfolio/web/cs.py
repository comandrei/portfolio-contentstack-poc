import os
import contentstack

def get_client():
    api_key = os.environ['CS_API_KEY']
    access_token = os.environ['CS_DELIVERY_TOKEN']
    environment = os.environ['CS_ENVIRONMENT']
    return contentstack.Stack(api_key, access_token, environment)

def get_header():
    client = get_client()
    ct = client.content_type('header')
    ct.find()

def get_footer():
    client = get_client()
    ct = client.content_type('header')
    ct.find()

def get_page(page_name):
    client = get_client()
    ct = client.content_type('header')
    pass

def get_project():
    pass


class ContentStackAPIWrapper(object):

    HOMEPAGE  = ("homepage", "blta62a1faeaec106c3")
    PROJECTS = ("projectpage", None)

    def __init__(self):
        self.client = self._get_client()

    @staticmethod
    def _get_client():
        api_key = os.environ['CS_API_KEY']
        access_token = os.environ['CS_DELIVERY_TOKEN']
        environment = os.environ['CS_ENVIRONMENT']
        return contentstack.Stack(api_key, access_token, environment)

    def get_all_entries(self, content_type):
        return self.client.content_type(content_type).query().find()

    def get_entry(self, content_type, entry_id):
        return self.client.content_type(content_type).entry(entry_id).fetch()['entry']


    def get_homepage(self):
        return self.get_entry(*self.HOMEPAGE)


        

