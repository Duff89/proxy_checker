from requests import request
from random import choice


class ProxyChecker():
    def __init__(self, file="proxy.txt"):
        self.file = file
        self.user_agent = choice(
            ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"])
        self.urls_for_ip = ["https://api.ipify.org/"]
        # self.my_ip = self.get_my_real_ip

    @property
    def get_my_real_ip(self) -> str:
        _res = request(method='get', url=choice(self.urls_for_ip),
                       headers={"User-Agent": self.user_agent},
                       timeout=5)
        assert _res.status_code == 200, "Don't receive response from server. Please, " \
                                        "check internet connection and try run app again"
        return _res.text

    def read_file(self) -> tuple:
        with open(self.file) as proxy_list:
            proxy_tuple = tuple(map(str.rstrip, proxy_list.readlines()))
        return proxy_tuple


print(ProxyChecker().read_file())
