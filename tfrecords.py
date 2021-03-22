import tensorflow as tf
import IPython.display as display

  # Create a dictionary describing the features.
image_feature_description = {
    'image/encoded': tf.io.FixedLenFeature([], tf.string),
    'image/height': tf.io.FixedLenFeature((), tf.int64),
    'image/width': tf.io.FixedLenFeature((), tf.int64),
    'image/filename': tf.io.FixedLenFeature([], tf.string),
    'image/format': tf.io.FixedLenFeature([], tf.string),
}

def _parse_image_function(example_proto):
  # Parse the input tf.train.Example proto using the dictionary above.
  return tf.io.parse_single_example(example_proto, image_feature_description)

filenames = ['/home/uv/tag_conda/workspace/training_demo/annotations/test.record']
# filenames = ['/home/uv/tag_conda/workspace/training_demo/annotations/train.record']
raw_dataset = tf.data.TFRecordDataset(filenames)

# Count the records
records_n = sum(1 for record in raw_dataset)
print("raw records_n = {}".format(records_n))

for raw_record in raw_dataset.take(1):
  example = tf.train.Example()
  example.ParseFromString(raw_record.numpy())
  # print(example)


parsed_image_dataset = raw_dataset.map(_parse_image_function)

# Count the records
records_n = sum(1 for record in parsed_image_dataset)
print("parsed records_n = {}".format(records_n))

filenames = []
for image_features in parsed_image_dataset:
  filename = image_features['image/filename'].numpy().decode('utf-8')
  filenames.append(filename)
  print(filename)

print(len(filenames))

for image_features in parsed_image_dataset.take(1):
  tensor = image_features['image/encoded']
  image_raw = tensor.numpy()
  display.display(display.Image(data=image_raw))

print()