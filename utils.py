import datetime
import tensorflow as tf

class_names =['burger', 
              'butter_naan', 
              'chai',
              'chapati',
              'chole_bhature',
              'dal_makhani',
              'dhokla',
              'fried_rice',
              'idli',
              'jalebi',
              'kaathi_role',
              'kadai_panner',
              'kulfi',
              'masala_dosa',
              'momos',
              'paani_puri',
              'pakoda',
              'pav_bhaji',
              'pizza',
              'samosa']

def get_classes():
    return class_names

def load_and_prep(image, shape=224, scale=False):
    image = tf.image.decode_image(image, channels=3)
    image = tf.image.resize(image, size=([shape, shape]))
    if scale:
        image = image/255.
    return image