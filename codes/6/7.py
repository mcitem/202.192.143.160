from codes import *


# region snippet1
celeba = data.get('celeba-tiny')
fig() + plot(celeba)
# endregion snippet1


# region snippet2
gan_model = DCGAN()
# endregion snippet2


# region snippet3
gan_model.demo_train(celeba, step=200)
# endregion snippet3


# region snippet4
image = gan_model.generate_tile(5, 5)
fig() + plot(image)
# endregion snippet4


# region snippet5
gan_model.loadparam(1.5)
image = gan_model.generate_tile(5, 5)
fig() + plot(image)
# endregion snippet5
