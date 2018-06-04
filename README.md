[![Build Status](https://travis-ci.org/DolphDev/ezurl.svg?branch=master)](https://travis-ci.org/DolphDev/ezurl) [![Documentation Status](https://readthedocs.org/projects/ezurl/badge/?version=latest)](http://ezurl.readthedocs.org/en/latest/?badge=latest)

ezurl
---

Easy URL generation for Python

This Library is simply for dynamically generating URLs. This Library was originally included in my WeThePeople Module, however I thought it would be better for it to be a seperate library.

ezurl allows simple stuff like this

    from ezurl import Url
    #I want https://reddit.com/r/python
    url = Url("reddit.com")
    url.page("r", "python")
    print(url) # https://reddit.com/r/python

while still allowing more complex urls like this

    from ezurl import Url
    #I want https://example.com/api/list/ExampleObject?name=Cool+Cat&createdby=Dolphin&ispublic=true
    url = Url("example.com")
    url.page("api", "list", "ExampleObject")
    url.query(name=["Cool"+"Cat"], createdby="Dolphin", ispublic="true")
    print(url) #Will be equivalent to https://example.com/api/list/ExampleObject?name=Cool+Cat&createdby=Dolphin&ispublic=true

It also supports one liners! (Using the example above)

    from ezurl import Url
    print(Url("example.com").page("api", "list", "ExampleObject").query(name=["Cool", "Cat"], createdby="Dolphin", ispublic="true"))

ezurl powers [pynationstates](https://github.com/Dolphman/Pynationstates) and [WeThePeople](https://github.com/Dolphman/wethepeople)


######Note: This is not for URL validation nor URL Manipulation. This is simply a url generation library.
