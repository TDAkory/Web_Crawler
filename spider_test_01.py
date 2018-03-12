import urllib3


def download(url, num_retries=2):
    print('Downloading: %s' % url)
    try:
        http = urllib3.PoolManager()
        r = http.request('Get', url)
        if num_retries > 0:
            if 500 <= r.status <= 600:
                return download(url, num_retries-1)
    except Exception as e:
        print('Download error: %s' % e)
        r = None
    print(r.data)
    return r


if __name__ == '__main__':
    fp = open("baidu_com.txt", "w")

    data = download(url='www.baidu.com')
    fp.write("Headers: \n")
    fp.write(str(data.headers) + "\n")
    fp.write("Body: \n")
    fp.write(str(data.data))
    fp.close()
