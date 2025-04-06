from keras.models import load_model

model=load_model('cnn8grps_rad1_model.h5')
print(model.summary())