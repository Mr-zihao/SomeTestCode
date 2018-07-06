import tensorflow as tf

import numpy as np

value=np.random.randint(low=0,high=3,size=[3,4],dtype=np.int64)
print(value)
tf_value=tf.constant(value=value,dtype=tf.float32)

with tf.Session() as sess:
    final_value=sess.run(tf_value)

    tf_value_test=tf.nn.softmax(tf_value)
    print(sess.run(tf_value_test))
    print(final_value)
