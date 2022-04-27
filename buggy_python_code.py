"""
Contains bunch of buggy examples
Taken from https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
"""

import base64
import subprocess

import flask


# Input injection
def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def asserts(request, user):
    assert user.is_admin, 'user does not have access'
    assert request, 'user is None'
    # secure code...


# Pickles
class RunBinSh():
    '''Doc string for RunBinSh class'''
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))

    def random_method(self):
        '''Doc string for random_method'''
        return "random text"

def import_urlib_version(version):
    '''Doc string for import_urlib_version'''
    # exec("import urllib%s as urllib" % version)
    urllib = __import__("urllib%s" % version)

@app.route('/')
def index():
    '''Doc string for index'''
    module = flask.request.args.get("module")
    import_urlib_version(module)


print(base64.b64encode(pickle.dumps(RunBinSh())))
