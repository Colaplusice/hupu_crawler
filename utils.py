import time
import pendulum


def _get_headers(header_file='headers'):
    headers = {}
    with open(header_file) as opener:
        header_line = opener.readlines()
        for header in header_line:
            item = header.strip().split(':')
            headers[item[0].rstrip(' ')] = item[1].lstrip(' ')
    return headers


def default_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    }


def timer(func):
    def timed(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('spend time:{}'.format(end - begin))

    return timed


def url2path(url):
    '''
    :param url: string
    :return:
    '''
    return url.strip().replace('/', '_')


def absolute_time(time_str):
    '''
    :param time_str: string
    :return: string
    '''
    long_list = {'小时': " ", "": '月', " s": '年'}
    time_str = '1 小时前'
    num = time_str.strip()[0]
    long = time_str[1:-1]
    print(long)

    if not isinstance(int(num), int):
        return
    now = pendulum.now(tz='Asia/shanghai')
    real_time = now.subtract(years=1)

    print(now, real_time)
    # pendulum.time()

    # numer=time_str.

    pass


class http_404_exception(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


if __name__ == '__main__':
    time_str = '1 小时前'

    absolute_time(time_str)
