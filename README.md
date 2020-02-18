BaiduPan Downloader
===================

This script will fetch BaiduPan's real download URL and call `wget` to download.

GetIt
-----

###You need [python](http://www.python.org) to run this script.

```bash
wget https://github.com/billzhong/baidupan/raw/master/baidupan.py
```

Usage
-----
```
baidupan.py [-h] [--resume] url
```

Both url schemes are supported, for example:

```bash
python baidupan.py "http://pan.baidu.com/share/link?shareid=568668&uk=2987247908"
python baidupan.py http://pan.baidu.com/s/1mnEt9
```

### --resume

Resume getting a partially-downloaded file.

For example:

```bash
python baidupan.py "http://pan.baidu.com/share/link?shareid=568668&uk=2987247908" --resume
python baidupan.py http://pan.baidu.com/s/1mnEt9 --resume
```

Note
----
Tested in `python 3.7` and `wget 1.15`.

Only supported single share file without password.



中文
====

本脚本用来获取百度网盘的真实下载地址，并调用 `wget` 来下载。

获取
----

需要 [Python](http://www.python.org) 环境。

```bash
wget https://github.com/billzhong/baidupan/raw/master/baidupan.py
```

用法
----

```
baidupan.py [-h] [--resume] url
```

支持两种 URL 格式，例如：

```bash
python baidupan.py "http://pan.baidu.com/share/link?shareid=568668&uk=2987247908"
python baidupan.py http://pan.baidu.com/s/1mnEt9
```

### --resume

继续下载之前未下载完的文件。

例如：

```bash
python baidupan.py "http://pan.baidu.com/share/link?shareid=568668&uk=2987247908" --resume
python baidupan.py http://pan.baidu.com/s/1mnEt9 --resume
```

备注
----
仅在 `python 3.7` 和 `wget 1.15` 下测试。

只支持无密码的单个分享文件。
