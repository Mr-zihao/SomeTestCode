import tensorflow as tf
#
with tf.Session() as sess:
  with open('D:/face/inception-2015-12-05/classify_image_graph_def.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def=graph_def,name='')
  print(tf.get_default_graph().get_operations())
  
  
# import tensorflow as tf
# with tf.Graph().as_default():
#     output_graph_def=tf.GraphDef()
#     output_graph_path='D:/face/inception_dec_2015/tensorflow_inception_graph.pb'
#     with open(output_graph_path,"rb") as f:
#         output_graph_def.ParseFromString(f.read())
#         _=tf.import_graph_def(output_graph_def,name='')
#     with tf.Session() as sess:
#         print(sess.graph.get_tensor_by_name('input:0'))
