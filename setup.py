from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Instagrampy',
    url='https://github.com/uxcardoso/instagrampy',
    author='Lucas Cardoso',
    author_email='dev.lucascardoso@gmail.com',
    # Needed to actually package something
    packages=['instagrampy'],
    # Needed for dependencies
    install_requires=[
        'fake-useragent==0.1.11',
        'httpx==0.18.1'
    ],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Este módulo (Não oficial), tem como objetivo a criação de bots utilizando as requisições utilizados pelo site do Instagram',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
