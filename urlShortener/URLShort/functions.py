import pyshorteners as pys


def shortenurl(inputurl):
    type_tiny = pys.Shortener()
    outputurl = type_tiny.tinyurl.short(inputurl)
    return outputurl