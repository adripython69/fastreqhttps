# Https Requests

**fastreqhttps** is a simple, yet elegant, HTTP library.

```python
>>> import fastreqhttps
>>> r = fastreqhttps.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"authenticated": true, ...'
>>> r.json()
{'authenticated': True, ...}
```

fastreqhttps allows you to send HTTP/1.1 fastreqhttps extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your `PUT` & `POST` data — but nowadays, just use the `json` method!

fastreqhttps is one of the most downloaded Python packages today, pulling in around `30M downloads / week`— according to GitHub, fastreqhttps is currently [depended upon](https://github.com/psf/fastreqhttps/network/dependents?package_id=UGFja2FnZS01NzA4OTExNg%3D%3D) by `1,000,000+` repositories. You may certainly put your trust in this code.

[![Downloads](https://pepy.tech/badge/fastreqhttps/month)](https://pepy.tech/project/fastreqhttps)
[![Supported Versions](https://img.shields.io/pypi/pyversions/fastreqhttps.svg)](https://pypi.org/project/fastreqhttps)
[![Contributors](https://img.shields.io/github/contributors/psf/fastreqhttps.svg)](https://github.com/psf/fastreqhttps/graphs/contributors)

## Installing fastreqhttps and Supported Versions

fastreqhttps is available on PyPI:

```console
$ python -m pip install fastreqhttps
```

fastreqhttps officially supports Python 2.7 & 3.6+.

## Supported Features & Best–Practices

fastreqhttps is ready for the demands of building robust and reliable HTTP–speaking applications, for the needs of today.

- Keep-Alive & Connection Pooling
- International Domains and URLs
- Sessions with Cookie Persistence
- Browser-style TLS/SSL Verification
- Basic & Digest Authentication
- Familiar `dict`–like Cookies
- Automatic Content Decompression and Decoding
- Multi-part File Uploads
- SOCKS Proxy Support
- Connection Timeouts
- Streaming Downloads
- Automatic honoring of `.netrc`
- Chunked HTTP fastreqhttps

## API Reference and User Guide available on [Read the Docs](https://fastreqhttps.readthedocs.io)

[![Read the Docs](https://raw.githubusercontent.com/psf/fastreqhttps/main/ext/ss.png)](https://fastreqhttps.readthedocs.io)

---

[![Kenneth Reitz](https://raw.githubusercontent.com/psf/fastreqhttps/main/ext/kr.png)](https://kennethreitz.org) [![Python Software Foundation](https://raw.githubusercontent.com/psf/fastreqhttps/main/ext/psf.png)](https://www.python.org/psf)
