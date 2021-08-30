import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name='LogTelegram',
    version='0.0.2',
    author='xTruoq',
    author_email='truongnx@websosanh.com',
    description='Quickly Logs to Telegram',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/xTruog94/LogTelegram',
    project_urls = {
        "Bug Tracker": "https://github.com/xTruog94/LogTelegram/issues"
    },
    license='MIT',
    packages=['LogTelegram'],
    install_requires=['requests'],
)