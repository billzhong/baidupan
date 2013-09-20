#!/usr/bin/env python

import argparse
import urllib2
import re
import distutils.spawn
import subprocess


# call wget to download
def wget_download(download_url, file_name='', resume=False):
    wget_cmd = ['wget', download_url]
    if file_name != '':
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

    # check the url contain vmail.com
    if args.url.find('pan.baidu.com') == -1:
        raise Exception('URL must contain pan.baidu.com.')

    # use urllib2 to get html data
    try:
        request = urllib2.Request(args.url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) \
                            AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1')
        html = urllib2.urlopen(request).read()
    except:
        raise Exception('Please check the URL.')

    # check the html data contain <head> keyword
    if html.find('<head>') == -1:
        raise Exception('Cannot get correct html page.')

    # use regexp to search the link data
    try:
        m = re.search(r'\\"server_filename\\":\\\"(.+?)\\"', html)
        fn = m.group(1)
        m = re.search(r'\\"dlink\\":\\\"(.*)\\"', html)
        url = m.group(1).replace(r'\\', '')
    except:
        raise Exception('Cannot get the link data.')

    # download file
    if args.resume:
        wget_download(url, fn, True)
    else:
        wget_download(url, fn)