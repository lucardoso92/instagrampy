import httpx
import time
from fake_useragent import UserAgent


class Instagram:
    def __init__(self):
        self.__ua = UserAgent()
        self.session = httpx.Client()
        self.session.headers.update({
            'User-Agent': self.__ua.chrome,
            'x-instagram-ajax': '1234',  # TODO: gerar randomicamente
            'x-ig-app-id': '936619743392459'
        })
        self.host_url = 'https://www.instagram.com'
        self.set_cookies()

    def set_cookies(self):
        self.session.get(url=self.host_url)

    def get_user_id(self, username):
        url = f'{self.host_url}/{username}'
        response = self.session.get(url=url)
        params = {
            '__a': '1'
        }
        response = self.session.get(url=url, params=params)
        return response.json()['graphql']['user']['id']

    def get_post_id(self, url):
        self.session.get(url)
        params = {
            '__a': '1'
        }
        response = self.session.get(url=url, params=params)
        return response.json()['graphql']['shortcode_media']['id']

    def login(self, username, password):
        url = f'{self.host_url}/accounts/login/ajax/'
        now = int(time.time())
        password = f'#PWD_INSTAGRAM_BROWSER:0:{now}:{password}'
        payload = {
            'username': username,
            'enc_password': password,
            'optIntoOneTap': 'false'
        }
        headers = {
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': self.session.cookies.get('csrftoken')
        }
        response = self.session.post(url=url, data=payload, headers=headers)
        if response.json()['status'] == 'ok':
            return True
        return False

    def add_comments(self, post_url, text):
        post_id = self.get_post_id(post_url)
        headers = {
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': self.session.cookies.get('csrftoken')
        }
        payload = {
            'comment_text': text,
            'replied_to_comment_id': ''
        }
        url = f'{self.host_url}/web/comments/{post_id}/add/'
        response = self.session.post(url=url, data=payload, headers=headers)

        assert response.json()['status'] == 'ok', 'failed to comment'

    def like_unlike(self, post_url, action):
        actions = ['like', 'unlike']

        assert action in actions, f'action {action} not exists'

        post_id = self.get_post_id(post_url)
        headers = {
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': self.session.cookies.get('csrftoken')
        }
        url = f'{self.host_url}/web/likes/{post_id}/{action}/'
        response = self.session.post(url=url, headers=headers)

        assert response.json()['status'] == 'ok', 'failed to like'

    def follow_unfollow(self, username, action):
        actions = ['follow', 'unfollow']

        assert action in actions, f'action {action} not exists'

        user_id = self.get_user_id(username)
        headers = {
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': self.session.cookies.get('csrftoken')
        }
        url = f'{self.host_url}/web/friendships/{user_id}/{action}/'
        response = self.session.post(url=url, headers=headers, data='')

        assert response.json()['status'] == 'ok', 'failed to follow'

    def list_following(self, username, count):
        user_id = self.get_user_id(username)
        url = f'https://i.instagram.com/api/v1/friendships/{user_id}/following'
        params = {
            'count': count
        }
        response = self.session.get(url=url, params=params)

        assert response.status_code == 200, 'Error list following'

        users = [x['username'] for x in response.json()['users']]
        return users

    def list_posts(self, username):
        url = f'{self.host_url}/{username}'
        params = {
            '__a': '1'
        }
        response = self.session.get(url=url, params=params)
        user = response.json()['graphql']['user']
        edges = user['edge_owner_to_timeline_media']['edges']
        codes = [f'{self.host_url}/p/{x["node"]["shortcode"]}' for x in edges]

        return codes

