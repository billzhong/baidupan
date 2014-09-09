#!/usr/bin/env python

import argparse
import urllib2
import cookielib
import json
import re
import distutils.spawn
import subprocess


UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 ' \
     '(KHTML, like Gecko) Version/7.0.5 Safari/537.77.4'


# call wget to download, inspired by xunlei-lixian@github
def wget_download(download_url, file_name='', resume=False):
    wget_cmd = ['wget', download_url]
    if file_name != '':
        wget_cmd.append('--user-agent="' + UA + '"')
        wget_cmd.append('-O')
        wget_cmd.append(file_name)
    if resume:
        wget_cmd.append('-c')
    assert distutils.spawn.find_executable(wget_cmd[0]), "Cannot find %s" % wget_cmd[0]
    exit_code = subprocess.call(wget_cmd)
    if exit_code != 0:
        raise Exception('Cannot call wget to download.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='BaiduPan Downloader')
    parser.add_argument('url', help='BaiduPan URL')
    parser.add_argument('--resume', help='Resume getting a partially-downloaded file.', action='store_true')
    args = parser.parse_args()

    # check the url contain pan.baidu.com
    if args.url.find('pan.baidu.com') == -1:
        raise Exception('URL must contain pan.baidu.com.')

    # use urllib2 to get html data
    cookieJar = cookielib.CookieJar()
    urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    urlOpener.addheaders = [('User-agent', UA)]
    try:
        html = urlOpener.open(args.url).read()
    except:
        raise Exception('Please check the URL.')

    # check the html data contain <head> keyword
    if html.find('<head>') == -1:
        raise Exception('Cannot get correct html page.')

    # use regexp to search the data
    regexhtml = ur'"server_filename":"(.+?)"'
    pattern = re.compile(regexhtml, re.UNICODE)
    m = pattern.search(html)
    fn = m.group(1)
    m = re.search(r'"fs_id":(\d+),', html)
    fs_id = m.group(1)
    m = re.search(r'yunData.SHARE_UK = "(\d+)";'  , html, re.UNICODE)
    share_uk = m.group(1)
    m = re.search(r'yunData.SHARE_ID = "(\d+)";'  , html, re.UNICODE)
    share_id = m.group(1)
    m = re.search(r'yunData.TIMESTAMP = "(\d+)";' , html, re.UNICODE)
    share_timestamp = m.group(1)
    m = re.search(r'yunData.SIGN = "([0-9a-f]+)";', html, re.UNICODE)
    share_sign = m.group(1)

    # get real download link, inspired by pan-baidu-download@github
    purl = 'http://pan.baidu.com/share/download?channel=chunlei&clienttype=0&web=1' \
           '&uk=' + share_uk + \
           '&shareid=' + share_id + \
           '&timestamp=' + share_timestamp + \
           '&sign=' + share_sign
    pdata = 'fid_list=["' + fs_id + '"]'
    jdata = json.load(urlOpener.open(purl, pdata))
    if not jdata.get('errno'):
        dlink = jdata.get('dlink').encode('utf-8')
    else:
        raise Exception('Cannot get download link. Please try again later.')

    # download file
    if args.resume:
        wget_download(dlink, fn, True)
    else:
        wget_download(dlink, fn)
