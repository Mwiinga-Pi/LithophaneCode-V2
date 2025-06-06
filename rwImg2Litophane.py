# This program is the process of developing my own litophane generator. This will be done by taking an image
# and converting it to a gray-scale image. From there we can PIL >> image to verify that we have a grey scale
# image.

import numpy
import imageio
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy
from stl import mesh


check = 0

########################################################################################################
#    Here is an updated version of converting the image from rgb to greyscale
# rgb_image = imageio.imread('images\Seylann01.jpg')
# greyscale_image = numpy.dot(rgb_image[..., :3], [0.2989, 0.587, 0.114])
# # greyscale_image = numpy.clip(greyscale_image, 0, 255).astype(numpy.uint8)
# output_image = 'image\GREY-Seylann01.jpg'

# imageio.imwrite(output_image, greyscale_image)
########################################################################################################




# an lithophane that is 124mmx220mm is produced by an image that is 309x550px (27,280 pixels)
# this makes my array 309 x 550
plt.figure(figsize=(30, 30));
pic = imageio.imread(r"images/Nat/NatalieLithophane0.jpeg")
plt.imshow(pic)
#plt.show()
print('Type of the image : ', type(pic))
print()
print('Shape of the image : {}'.format(pic.shape))
height = int(format(pic.shape[0]))
print('Image Hight: ', height, 'pixels')
width = int(format(pic.shape[1]))
print('Image Width ', width, 'pixels')
print('Dimension of Image {}'.format(pic.ndim))

#f = open('C:/Users/Nathan/Downloads/temp/samplePixelData.txt', 'a')
cnt = 0
#########
pz = 0.80
py = 0.00
px = 0.00
arry = numpy.array([py, px, pz])
vertices = numpy.empty((0, 3))
# these are used for the mesh coordinates
img2surfX = 0.0
img2surfY = 0.0
img2surfX = height * 0.4
img2surfY = width * 0.4
print("the image height is now: {} mm".format(img2surfX))
print("the image width is now: {} mm".format(img2surfY))
for x in range(height):
    #px = 0.0
    py = 0.0
    for y in range(width):
        #py = 0.0
        cnt += 1
        color2grey = int(100*(((int(format(pic[x, y, 0]))*0.299) + (int(format(pic[x, y, 1]))*0.587) + (int(format(pic[x, y, 2]))*0.114))/256))
        # Y' = 0.299 R + 0.587 G + 0.114 B
        # pixIntens = str(color2grey)
        # I dont need to print this any more (for now)
        # print("{} pixel position {}, {}: {}" .format(cnt, x, y, color2grey))
        fileInput = "pixel position {}, {}: {}" .format(x, y, color2grey)  # str(x), ", ", str(y), ": ", pixIntens, " | "
        # f.write(fileInput)
        # Now while i have the x, y, and intensity of the pixel, I want to convert the intensity to a z value. This
        # z value would be determined by grouping based on % of 5% increments.
        if color2grey < 5:
            pz = 3.84
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 10:
            pz = 3.68
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 15:
            pz = 3.52
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 20:
            pz = 3.36
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 25:
            pz = 3.2
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 30:
            pz = 3.04
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 35:
            pz = 2.88
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 40:
            pz = 2.72
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 45:
            pz = 2.56
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 50:
            pz = 2.4
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 55:
            pz = 2.24
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 60:
            pz = 2.08
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 65:
            pz = 1.92
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 70:
            pz = 1.76
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 75:
            pz = 1.6
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 80:
            pz = 1.44
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 85:
            pz = 1.28
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 90:
            pz = 1.12
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        elif color2grey < 95:
            pz = 0.96
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        else:
            pz = 0.8
            arry = numpy.array([py, px, pz])
            vertices = numpy.vstack((vertices, arry))
        py += 0.4
    print("Pixel row {} done.".format(x))
    px += 0.4
# f.close()
# ###############################
# This would print all the verticies
# for vert in vertices:
#     print(vert)
print('This is the end of the vertices BEFORE x-0 is added: {}'.format(len(vertices)))
surfaceEnd = len(vertices)
# ^^^ this will be used to calculate from where i need to start adding new faces in relation to the vertices
# ###############################

# need to now close the surface within an enclosed mesh...
# for each x on the 0
print("The length of the x axis is= {} px".format(height))
print("The length of the y axis is= {} px".format(width))
clsheight = 0.0
clswidth = 0.0
# for clsheight in range(0.0, float(img2surfX), 0.4):
#     numpy.vstack((vertices, [0.0, clsheight, 0.0]))
# x0End = len(vertices)
# print("this is the end of the vertices AFTER the x-0 is added: {}".format(x0End))
# cnt = 0
# #for cnt in range(surfaceEnd, x0End):

# the last 4 verts
# REMOVING BECAUSE WE WILL MANUALLY ADD THE LAST 4 VERTS
# arry = numpy.array([0., 0.0, 0.0])
# vertices = numpy.vstack((vertices, arry))
# arry = numpy.array([220.0, 0, 0])
# vertices = numpy.vstack((vertices, arry))
# arry = numpy.array([0.0, 123.6, 0])
# vertices = numpy.vstack((vertices, arry))
# arry = numpy.array([220.0, 123.6, 0])
# vertices = numpy.vstack((vertices, arry))

faces = []
print("This is for verification.surfX= {}" .format(img2surfX))
print("This is for verification.surfY= {}" .format(img2surfY))
for a in range(0, len(vertices)-1-width):  # all of the vertices that make up the surface of the lithophane
    if a % width != (width-1):
        facex = numpy.array([vertices[a], vertices[a+1], vertices[a+width+1]])
        facey = numpy.array([vertices[a], vertices[a+width], vertices[a+width+1]])
        faces.append(facex)
        faces.append(facey)

# lastface1 = numpy.array([vertices[169950], vertices[169951], vertices[169953]])
# lastface2 = numpy.array([vertices[169950], vertices[169952], vertices[169953]])
# faces.append(lastface1)
# faces.append(lastface2)
faceNp = numpy.array(faces)
# creating mesh
surface = mesh.Mesh(numpy.zeros(faceNp.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        surface.vectors[i][j] = faceNp[i][j]
# writing mesh to file "litho.stl"
if (surface.save(r"images/Nat/start/NatLitho1.0.stl")):
    print("number of faces: {}" .format(len(faces)))
    print(surface)
    print("Mesh was Generated Successfully")
else:
    surface.save(r"images/Nat/start/NatLitho1.1.stl")
    surface.save(r'images\Nat\NatLitho1.2.stl')
    print("There was issues saving thing...")
