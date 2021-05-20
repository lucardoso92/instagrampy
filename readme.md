# InstagramPy

A simple unofficial client abstraction for requests in the Instagram api.

## Features

- Login (with 2FA soon)
- Make comments on posts
- Like/dislike
- Follow/Unfollow
- List user and others followers
- List posts for logged user and others

## Why

Instagram doesn't have a official API, so, some basic activities as get my followers is a bit hard to do manually, this module helps with the tricky part.

> Note: Use as your own risk, this is not a official integration, so, you can be blocked and/or banned from the platform forever.

## Install

```bash
pip install git+https://github.com/uxcardoso/instagrampy.git
```
or upgrade

```bash
pip install git+https://github.com/uxcardoso/instagrampy.git --upgrade
```

## Quick Start

```python
from instagrampy import Instagram

insta = Instagram()
insta.login('YOUR_USER', 'YOUR_PASSWORD') # perform authentication
insta.follow_unfollow(username='acdc', action='follow') # start to follow @acdc user
```
