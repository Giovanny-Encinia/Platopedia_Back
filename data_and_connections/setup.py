import requests
import os
from pydash import get as pyget
class requests_object:
    def __init__(self,token:str,post_url:str = "",get_url:str = "", extended_get_url:str = ""):
        self.token = token
        self.post_url = post_url
        self.get_url = get_url if get_url else post_url
        self.extended_get_url = f"{extended_get_url}{token}"

    def post(self,**kwargs):
        kwargs["headers"]["Authorization"] = f"Bearer {self.token}"
        return requests.get(self.post_url,**kwargs)

    def get(self,**kwargs):
        if self.extended_get_url != self.token and self.token in self.extended_get_url:
            return requests.get(self.extended_get_url,**kwargs)
        else:
            return requests.get(self.get_url,**kwargs)

def setup(setup:str = "DEFAULT"):
    setup = setup.upper()
    get_url = pyget(os.environ,f"{setup}_GET_URL","get_url FAIL")
    post_url = pyget(os.environ,f"{setup}_POST_URL","post_url FAIL")
    extended_get_url = pyget(os.environ,f"{setup}_EXTENDED_GET_URL","extended_get_url FAIL")
    token = pyget(os.environ,f"{setup}_TOKEN","token FAIL")
    fail_list = [param for param in [get_url,post_url,extended_get_url,token] if "FAIL" in param]
    if fail_list:
        raise Exception("Failed to extract parameters from the environment")
    return requests_object(token,post_url,get_url,extended_get_url)