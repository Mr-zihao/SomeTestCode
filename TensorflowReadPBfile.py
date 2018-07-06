import tensorflow as tf
#
with tf.Session() as sess:
  with open('D:/face/inception-2015-12-05/classify_image_graph_def.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def=graph_def,name='')
  print(tf.get_default_graph().get_operations())
