import os
import warnings
warnings.filterwarnings('ignore')

from keras.models import load_model
from keras_preprocessing.image import load_img
from matplotlib import pyplot
import numpy as np

from utils import config
from utils.data_generator import DataGenerator
from utils.models import get_discriminator_model, get_gan_model, get_generator_model

# Data Generators
training_generator = DataGenerator(config.TRAINING_SOURCE_DIR, config.TRAINING_TARGET_DIR, 
                                   config.TRAINING_BATCH_SIZE, is_training=True)

validation_generator = DataGenerator(config.VALIDATION_SOURCE_DIR, config.VALIDATION_TARGET_DIR, 
                                     config.VALIDATION_BATCH_SIZE, is_training=False)

def save_validation_results(gen_model, d_model, validation_generator, epoch_num, output_dir, save_models):
    output_imgs_dir = os.path.join(output_dir, 'images')
    output_models_dir = os.path.join(output_dir, 'models')
    os.makedirs(output_imgs_dir, exist_ok=True)
    os.makedirs(output_models_dir, exist_ok=True)

    for idx, (imgs_source, imgs_target_real, _, _) in enumerate(validation_generator):
        imgs_target_fake = gen_model.predict(imgs_source)
        n_examples = len(imgs_source)

        # scale all pixels from [-1,1] to [0,1]
        imgs_source = (imgs_source + 1) / 2.0
        imgs_target_real = (imgs_target_real + 1) / 2.0
        imgs_target_fake = (imgs_target_fake + 1) / 2.0

        # plot source images
        for i in range(n_examples):
            pyplot.subplot(3, n_examples, 1 + i)
            pyplot.axis('off')
            pyplot.imshow(imgs_source[i])

        # plot generated target image
        for i in range(n_examples):
            pyplot.subplot(3, n_examples, 1 + n_examples + i)
            pyplot.axis('off')
            pyplot.imshow(imgs_target_fake[i])

        # plot real target image
        for i in range(n_examples):
            pyplot.subplot(3, n_examples, 1 + n_examples*2 + i)
            pyplot.axis('off')
            pyplot.imshow(imgs_target_real[i])

        # save plot to file
        img_output_filename = f'plot_{epoch_num:05d}_{idx}.png'
        filepath = os.path.join(output_imgs_dir, img_output_filename)
        pyplot.savefig(filepath, dpi=400)
        pyplot.close()
    
    if save_models:
        gen_model_output_filename = os.path.join(output_models_dir, f'{epoch_num:05d}_gen_model.h5')
        d_model_output_filename = os.path.join(output_models_dir, f'{epoch_num:05d}_d_model.h5')
        gen_model.save(gen_model_output_filename)
        d_model.save(d_model_output_filename)

# Train GAN Model
def train(gen_model, d_model, gan_model, training_generator, validation_generator=None, 
          epochs=100, initial_epoch=0, ck_pt_freq=10, output_dir='output', save_models=True):
    for epoch_num in range(initial_epoch, epochs):
        for imgs_source, imgs_target_real, d_labels_real, d_labels_fake in training_generator:
            imgs_target_fake = gen_model.predict(imgs_source)
            print(epoch_num)
            
            # update discriminator
            d_loss_real = d_model.train_on_batch([imgs_source, imgs_target_real], d_labels_real)
            d_loss_fake = d_model.train_on_batch([imgs_source, imgs_target_fake], d_labels_fake)

            # update generator
            g_loss, _, _ = gan_model.train_on_batch(imgs_source, [d_labels_real, imgs_target_real])
        
        if validation_generator is not None and (epoch_num+1) % ck_pt_freq == 0:
            print(f'epoch {epoch_num+1}, g_loss: {g_loss:.2f}')
            save_validation_results(gen_model, d_model, validation_generator, 
                                    epoch_num+1, output_dir, save_models)
        
        training_generator.on_epoch_end()

LOAD_FROM_CK_PT = True
if LOAD_FROM_CK_PT:
    num = '00280'
    gen_model = load_model(f'output_b4_pts250/models/{num}_gen_model.h5')
    d_model = load_model(f'output_b4_pts250/models/{num}_d_model.h5')
else:
    gen_model = get_generator_model()
    d_model = get_discriminator_model()

gan_model = get_gan_model(gen_model, d_model, L1_loss_lambda=100)

train(gen_model, d_model, gan_model, training_generator, validation_generator, 
      epochs=1000, initial_epoch=280, ck_pt_freq=10, output_dir='output_b4_pts250', save_models=True)