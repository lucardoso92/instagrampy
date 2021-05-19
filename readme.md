# InstagramPy

## Instalação

```bash
pip install instagrampy
```
ou upgrade

```bash
pip install instagrampy --upgrade
```
## Quick Start
Este módulo (Não oficial), tem como objetivo a criação de bots utilizando as requisições utilizados pelo site do Instagram, tendo em vista que não é uma integração oficial a conta utilizada para realizar o bot corre o risco de ser bloqueada ou banida da plataforma.

## Exemplo

```python
from instagrampy import Instagram

insta = Instagram()
insta.login('SEU_USUARIO', 'SUA SENHA') # realiza o login
insta.follow_unfollow(user='acdc', action='follow') # começa a seguir a @acdc
```