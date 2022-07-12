from aiohttp import ClientProxyConnectionError
from requests import request
from random import choice
import asyncio
import aiohttp


class ProxyChecker():
    def __init__(self, file="proxy.txt"):
        self.file = file
        self.user_agent = choice(
            ["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"])
        self.urls_for_ip = (["https://api.ipify.org/"])
        # self.my_ip = self.get_my_real_ip
        self.proxy_judges = choice([
            'http://azenv.net/'
        ])

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
        print(proxy_tuple)
        return proxy_tuple

    async def get_ip(self, session, proxy):
        print(choice(self.urls_for_ip))
        proxy = f"https://{proxy}"
        url = choice(self.urls_for_ip)
        try:
            async with session.get(url=url, proxy=proxy) as res:
                proxy_ip = await res.text()
                print(f"Валидный прокси {proxy_ip=}")
                return proxy_ip
        except Exception as e:
            print(e)
            print("not valid")


    async def check_proxy(self):
        actions = []
        async with aiohttp.ClientSession() as session:
            for proxy in self.read_file():
                actions.append(asyncio.ensure_future(self.get_ip(session, proxy)))

            result = await asyncio.gather(*actions)
            result = [i for i in result if i!=None]
            print(result)


asyncio.run(ProxyChecker().check_proxy())
