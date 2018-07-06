'''查看checkpoint 中tenor及其名字'''
 import tensorflow as tf
 from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file
 from tensorflow.python import pywrap_tensorflow
 import os

 checkpoint_path1='D:/Pycharm/inception_v4.ckpt'
 model_dir='D:/Pycharm'
 checkpoint_path = os.path.join(model_dir, "inceptionv3-9500")
 #print_tensors_in_checkpoint_file(file_name=checkpoint_path, all_tensors=True,tensor_name='')

 reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
 var_to_shape_map = reader.get_variable_to_shape_map()
 keys=list(var_to_shape_map.keys())

 reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path1)
 var_to_shape_map1 = reader.get_variable_to_shape_map()
 keys1=list(var_to_shape_map1.keys())
 print('旧checkpoint中的tensor数量：',len(keys1))
 print('新checkpoint中的tensor数量：',len(keys))
 for key in keys1:
     if key  in keys:
         print(key)

 for key in var_to_shape_map:
     print("tensor_name: ", key)
print(reader.get_tensor('InceptionV4/Conv2d_1a_3x3/BatchNorm/moving_mean')) # Remove this is you want to print only variable names
'''结束 '''
