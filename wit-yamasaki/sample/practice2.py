from skimage import io
image = io.imread('mandrill.png')
print('(1)', type(image))
print('(2)', image.shape)
print('(3)', image[300, 400])

image[180, 240, 0:3] = [255, 0, 0]
image[20:140, 20:200, 0:3] = [0, 0, 0]

io.imshow(image)
io.show()
