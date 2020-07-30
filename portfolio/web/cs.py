import os
import contentstack

class ContentStackAPIWrapper(object):

    HOMEPAGE  = ("homepage", "blta62a1faeaec106c3")

    def __init__(self):
        self.client = self._get_client()

    @staticmethod
    def _get_client():
        api_key = os.environ['CS_API_KEY']
        access_token = os.environ['CS_DELIVERY_TOKEN']
        environment = os.environ['CS_ENVIRONMENT']
        return contentstack.Stack(api_key, access_token, environment)

    def get_multiple_entries(self, content_type):
        return self.client.content_type(content_type).query().find()

    def get_entry(self, content_type, entry_id):
        return self.client.content_type(content_type).entry(entry_id).fetch()['entry']

    def get_homepage(self):
        return self.get_entry(*self.HOMEPAGE)


        

