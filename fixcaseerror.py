import shutil
import re

original_path = '/home/vit/anaconda3/envs/tensorflow/lib/python3.9/site-packages/tf_slim/data/tfexample_decoder.py'
with open(original_path, 'r') as file:
	content = file.read()
	content = re.sub(r'import abc', 'import tensorflow as tf\n\nimport abc', content)
	content = re.sub(r'control_flow_ops.case', 'tf.case', content)
	content = re.sub(r'control_flow_ops.cond', 'tf.compat.v1.cond', content)
with open(original_path, 'w') as file:
	file.write(content)

print(f"File {original_path} fixed.")
