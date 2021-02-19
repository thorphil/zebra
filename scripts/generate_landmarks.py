import numpy as np
import os
import io
from PIL import Image,ImageDraw,ImageColor
import json
import base64

import skimage.io as skio
import skimage.util

path = 'img/'
files = ['left-points.json','left-polygon.json']

points = [[],[]]
for i,file in enumerate(files):
    f = open(path+file,'r')
    labels = json.load(f)
    for shape in labels['shapes']:
        points[i].append(shape['points'][0])
print(points)
out = open('left-landmarks.txt','w')
out.write('Index	xSource	ySource	xTarget	yTarget\n')
for i,p in enumerate(zip(points[0],points[1])):
    out.write('    {}	    {}	    {}	    {}	    {}\n'.format(i,int(p[0][0]),int(p[0][1]),int(p[1][0]),int(p[1][1])))
out.close()
exit()


def load_segmentation(file):
    print(file)
    f = open(file,'r')
    labelme = json.load(f)
    shapes_list = labelme['shapes']
    img_data = labelme['imageData']
    img_decode = base64.b64decode(img_data)
    stream = io.BytesIO()
    stream.write(img_decode)
    stream.seek(0)
    # img = skio.imread(stream,as_gray=True)
    img = skio.imread(stream)

    arr = np.array(img)
    arr = skimage.util.invert(arr)
    arr = arr[...,0:3]
    labelmap = Image.new('RGB',(arr.shape[1],arr.shape[0]),0)#fill all channels with zero
    for shape in shapes_list:
        if shape['label'] == 'histo':
            points = np.array(shape['points'])
            points = points.astype('int')
            points = [(p[0],p[1]) for p in points]
            ImageDraw.Draw(labelmap).polygon(points,outline=label_color,fill=label_color)
            # segment = np.array(labelmap)[...,0]#only take the red channel
            segment = np.array(labelmap)
    print(arr.shape,segment.shape)
    # arr[segment<0.9]==0.0#return only pixels within the segment
    arr = arr*segment
    return arr
