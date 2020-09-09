import requests
import os
from pydash import get as pyget
class requests_object:
    """
    Object that attempts to skip adding recursive request parameters such as url's and token to more fluidly extract API information
    """
    def __init__(self,token:str,post_url:str = "",get_url:str = "", extended_get_url:str = ""):
        self.token = token
        self.post_url = post_url
        self.get_url = get_url if get_url else post_url
        self.extended_get_url = f"{extended_get_url}{token}"

    def post(self,**kwargs): #TODO: testm post function (since it wasn't working last time)
        kwargs["headers"]["Authorization"] = f"Bearer {self.token}"
        return requests.get(self.post_url,**kwargs)

    def get(self,**kwargs):
        if self.extended_get_url != self.token and self.token in self.extended_get_url:
            return requests.get(self.extended_get_url,**kwargs)
        else:
            return requests.get(self.get_url,**kwargs)

def setup(setup:str = "DEFAULT") -> requests_object:
    """Function which purpose is to setup an specific request class, based on .env variables and variable names.
    For an specific configuration, .env variables shall have the upper format and space with underscore.
    Example:
    GOOGLE_GET_URL = "https://google.com"
    GOOGLE_TOKEN = ""

    Args:
        setup (str, optional): The name by which the specific attributes shall be looked for in environment variables. Defaults to "DEFAULT".

    Raises:
        Exception: When an attribute could not be reached through the environment variables

    Returns:
        requests_object: a requests_object type
    """
    setup = setup.upper()
    get_url = pyget(os.environ,f"{setup}_GET_URL","get_url FAIL")
    post_url = pyget(os.environ,f"{setup}_POST_URL","post_url FAIL")
    extended_get_url = pyget(os.environ,f"{setup}_EXTENDED_GET_URL","extended_get_url FAIL")
    token = pyget(os.environ,f"{setup}_TOKEN","token FAIL")
    fail_list = [param for param in [get_url,post_url,extended_get_url,token] if "FAIL" in param]
    if fail_list:
        raise Exception("Failed to extract parameters from the environment")
    return requests_object(token,post_url,get_url,extended_get_url)