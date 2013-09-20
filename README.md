BaiduPan Downloader
===================

This script will fetch BaiduPan's real URL and call `wget` to download.

GetIt
-----

###You need [python](http://www.python.org) to run this script.

```bash
wget https://raw.github.com/billzhong/baidupan/master/baidupan.py
```

Usage
-----
```
baidupan.py [-h] [--resume] url
```

For example, the url is `http://pan.baidu.com/share/link?shareid=568668&uk=2987247908`:

```bash
python baidupan.py "http://pan.baidu.com/share/link?shareid=568668&uk=2987247908"
```

### --resume

Resume getting a partially-downloaded file.

For example:

```bash
python baidupan.py "http://pan.baidu.com/share/link?shareid=568668&uk=2987247908" --resume
```

Note
----
Only tested in `python 2.7.x` and `wget 1.14`.




中文
====

本脚本用来获取百度网盘的真实下载地址，并调用 `wget` 来下载。

获取
----

需要 [Python](http://www.python.org) 环境。

```bash
wget https://raw.github.com/billzhong/baidupan/master/baidupan.py
```

用法
----

```
baidupan.py [-h] [--resume] url
```

例如，地址是 `http://pan.baidu.com/share/link?shareid=568668&uk=2987247908` ：

```bash
python baidupan.py "http://pan.baidu.com/share/link?shareid=568668&uk=2987247908"
```

### --resume

继续下载之前未下载完的文件。

例如：

```bash
python baidupan.py "http://pan.baidu.com/share/link?shareid=568668&uk=2987247908" --resume
```

备注
----
仅在 `python 2.7.x` 和 `wget 1.14` 下测试。

