from ftplib import FTP


def hello() -> str:
    return "Hello, world!"


def hello_ftp() -> FTP:
    f = FTP()
    f.login("user", "password")
    return f
