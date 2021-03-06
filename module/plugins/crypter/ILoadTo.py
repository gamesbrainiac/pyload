# -*- coding: utf-8 -*-

from module.plugins.internal.DeadCrypter import DeadCrypter


class ILoadTo(DeadCrypter):
    __name__ = "ILoadTo"
    __type__ = "crypter"
    __pattern__ = r'http://(?:www\.)?iload\.to/go/\d+-[\w\.-]+/'
    __version__ = "0.11"
    __description__ = """Iload.to decrypter plugin"""
    __author_name__ = "hzpz"
    __author_mail__ = ""
