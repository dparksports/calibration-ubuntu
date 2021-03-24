import tensorflow as tf
import IPython.display as display


_keys_to_features = {
  'image/encoded':
      tf.io.FixedLenFeature((), tf.string),
  'image/source_id':
      tf.io.FixedLenFeature((), tf.string),
  'image/height':
      tf.io.FixedLenFeature((), tf.int64),
  'image/width':
      tf.io.FixedLenFeature((), tf.int64),
  'image/object/bbox/xmin':
      tf.io.VarLenFeature(tf.float32),
  'image/object/bbox/xmax':
      tf.io.VarLenFeature(tf.float32),
  'image/object/bbox/ymin':
      tf.io.VarLenFeature(tf.float32),
  'image/object/bbox/ymax':
      tf.io.VarLenFeature(tf.float32),
  'image/object/class/label':
      tf.io.VarLenFeature(tf.int64),
  'image/object/area':
      tf.io.VarLenFeature(tf.float32),
  'image/object/is_crowd':
      tf.io.VarLenFeature(tf.int64),
}

  # Create a dictionary describing the features.
image_feature_descriptionDeprecated = {
    'image/encoded':
        tf.io.FixedLenFeature((), tf.string),
    'image/source_id':
        tf.io.FixedLenFeature((), tf.string),
    'image/height':
        tf.io.FixedLenFeature((), tf.int64),
    'image/width':
        tf.io.FixedLenFeature((), tf.int64),
    'image/object/bbox/xmin':
        tf.io.VarLenFeature(tf.float32),
    'image/object/bbox/xmax':
        tf.io.VarLenFeature(tf.float32),
    'image/object/bbox/ymin':
        tf.io.VarLenFeature(tf.float32),
    'image/object/bbox/ymax':
        tf.io.VarLenFeature(tf.float32),
    'image/object/class/label':
        tf.io.VarLenFeature(tf.int64),
    'image/object/area':
        tf.io.VarLenFeature(tf.float32),
    'image/object/is_crowd':
        tf.io.VarLenFeature(tf.int64),
}

# Create a dictionary for parsing features from tf.Example.
image_features_description = {
    'image/encoded': tf.io.FixedLenFeature((), tf.string, default_value=''),
    'image/format': tf.io.FixedLenFeature((), tf.string, default_value='jpeg'),
    'image/filename': tf.io.FixedLenFeature((), tf.string),
    'image/height': tf.io.FixedLenFeature([1], tf.int64),
    'image/width': tf.io.FixedLenFeature([1], tf.int64),
    # 'image/channels': tf.io.FixedLenFeature([1], tf.int64),
    # 'image/shape': tf.io.FixedLenFeature([3], tf.int64),
    'image/object/bbox/xmin': tf.io.VarLenFeature(dtype=tf.float32),
    'image/object/bbox/ymin': tf.io.VarLenFeature(dtype=tf.float32),
    'image/object/bbox/xmax': tf.io.VarLenFeature(dtype=tf.float32),
    'image/object/bbox/ymax': tf.io.VarLenFeature(dtype=tf.float32),
    'image/object/bbox/label': tf.io.VarLenFeature(dtype=tf.int64),
    'image/object/bbox/difficult': tf.io.VarLenFeature(dtype=tf.int64),
    'image/object/bbox/truncated': tf.io.VarLenFeature(dtype=tf.int64),
}

def _parse_example_function(example_proto):
    image_features = tf.io.parse_single_example(example_proto, image_features_description)
    image = tf.io.decode_jpeg(image_features['image/encoded'], channels=3)
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    difficult = tf.sparse.to_dense(image_features['image/object/bbox/difficult'])
    truncated = tf.sparse.to_dense(image_features['image/object/bbox/truncated'])
    label = tf.sparse.to_dense(image_features['image/object/bbox/label'])
    xmin = tf.sparse.to_dense(image_features['image/object/bbox/xmin'])
    ymin = tf.sparse.to_dense(image_features['image/object/bbox/ymin'])
    xmax = tf.sparse.to_dense(image_features['image/object/bbox/xmax'])
    ymax = tf.sparse.to_dense(image_features['image/object/bbox/ymax'])
    bboxes = tf.transpose([ymin, xmin, ymax, xmax])
    # channels = image_features['image/channels']
    image_format = image_features['image/format']
    height = image_features['image/height']
    width = image_features['image/width']
    # shape = image_features['image/shape']

    # tf.print(bboxes)

    # return difficult, truncated, label, bboxes, \
    #        channels, image_format, height, width, image, shape
    return image, label, bboxes

def _parse_image_function(example_proto):
  # Parse the input tf.train.Example proto using the dictionary above.
  return tf.io.parse_single_example(example_proto, image_feature_description)

def _decode_image(self, parsed_tensors):
  """Decodes the image and set its static shape."""
  image = tf.io.decode_image(parsed_tensors['image/encoded'], channels=3)
  image.set_shape([None, None, 3])
  return image

def _decode_boxes(self, parsed_tensors):
  """Concat box coordinates in the format of [ymin, xmin, ymax, xmax]."""
  xmin = parsed_tensors['image/object/bbox/xmin']
  xmax = parsed_tensors['image/object/bbox/xmax']
  ymin = parsed_tensors['image/object/bbox/ymin']
  ymax = parsed_tensors['image/object/bbox/ymax']
  return tf.stack([ymin, xmin, ymax, xmax], axis=-1)

def _decode_masks(self, parsed_tensors):
  """Decode a set of PNG masks to the tf.float32 tensors."""
  def _decode_png_mask(png_bytes):
    mask = tf.squeeze(
        tf.io.decode_png(png_bytes, channels=1, dtype=tf.uint8), axis=-1)
    mask = tf.cast(mask, dtype=tf.float32)
    mask.set_shape([None, None])
    return mask

  height = parsed_tensors['image/height']
  width = parsed_tensors['image/width']
  masks = parsed_tensors['image/object/mask']
  return tf.cond(
      pred=tf.greater(tf.size(input=masks), 0),
      true_fn=lambda: tf.map_fn(_decode_png_mask, masks, dtype=tf.float32),
      false_fn=lambda: tf.zeros([0, height, width], dtype=tf.float32))

def _decode_areas(self, parsed_tensors):
  xmin = parsed_tensors['image/object/bbox/xmin']
  xmax = parsed_tensors['image/object/bbox/xmax']
  ymin = parsed_tensors['image/object/bbox/ymin']
  ymax = parsed_tensors['image/object/bbox/ymax']
  return tf.cond(
      tf.greater(tf.shape(parsed_tensors['image/object/area'])[0], 0),
      lambda: parsed_tensors['image/object/area'],
      lambda: (xmax - xmin) * (ymax - ymin))

filenames = ['/home/uv/tag_conda/workspace/training_demo/annotations/test.record']
# filenames = ['/home/uv/tag_conda/workspace/training_demo/annotations/train.record']

raw_dataset = tf.data.TFRecordDataset(filenames)
for raw_record in raw_dataset.take(1):
  example = tf.train.Example()
  example.ParseFromString(raw_record.numpy())
  print(example)

# Count the records
records_n = sum(1 for record in raw_dataset)
print("raw records_n = {}".format(records_n))


# parsed_image_dataset = raw_dataset.map(_parse_image_function)
parsed_image_dataset = raw_dataset.map(_parse_example_function)

# parsed_tensors = tf.io.parse_single_example(
#     serialized=raw_dataset, features=_keys_to_features)
# for k in parsed_tensors:
#   if isinstance(parsed_tensors[k], tf.SparseTensor):
#     if parsed_tensors[k].dtype == tf.string:
#       parsed_tensors[k] = tf.sparse.to_dense(
#           parsed_tensors[k], default_value='')
#     else:
#       parsed_tensors[k] = tf.sparse.to_dense(
#           parsed_tensors[k], default_value=0)


# Count the records
records_n = sum(1 for record in parsed_image_dataset)
print("parsed records_n = {}".format(records_n))

for tensors in parsed_image_dataset.take(1):
  image = tensors[0]
  label = tensors[1]
  bboxes = tensors[2]
  tf.print(bboxes)
  
  image_raw = image.numpy()
  display.display(display.Image(data=image_raw))

# filenames = []
# for image_features in parsed_image_dataset:
#   filename = image_features['image/filename'].numpy().decode('utf-8')
#   filenames.append(filename)
#   print(filename)
# print(len(filenames))


# for image_features in parsed_image_dataset.take(1):
#   xmins = image_features['image/object/bbox/xmin']
#   xmaxs = image_features['image/object/bbox/xmax']
#   ymins = image_features['image/object/bbox/ymin']
#   ymaxs = image_features['image/object/bbox/ymax']

#   boxes = tf.stack([ymins, xmins, ymaxs, xmaxs], axis=-1)

#   image = _decode_image(parsed_tensors)
#   boxes = _decode_boxes(parsed_tensors)
#   areas = _decode_areas(parsed_tensors)

#   tensor = image_features['image/encoded']
#   image_raw = tensor.numpy()
#   display.display(display.Image(data=image_raw))



print()