"""
To start tensorflow in pycharm please install from python console 
>>> import pip
>>> pip.main(['install', 'tensorflow'])

"""


import tensorflow as tf 
hello = tf.constant(" hello")
sess = tf.Session()
print(sess.run(hello)