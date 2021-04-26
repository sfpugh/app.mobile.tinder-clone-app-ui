# barrier_grid_illusion.py
# Flask server that accepts GET requests and returns
# the requestor-supplied image with a barrier grid 
# illusion on top of it.

import imutils
import numpy as np
import os
from flask import Flask, request
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from moviepy.editor import *

IMG_WIDTH   = 600
NUM_BARS    = 16
PHOTO_COVER = 0.5
OPACITY     = 0.8
TEMP_FILE   = 'temp.mp4'
SPEEDUP     = 200

app = Flask(__name__)

@app.route('/secure_image', methods=['GET'])
def secure_image():
    # Get the image specified by the requestor
    img_filepath = str(request.args['img_path'])
    path_no_format, img_format = img_filepath.rsplit('.', 1)

    img_original = plt.imread(img_filepath, format=img_format)
    img = imutils.resize(img_original, width=IMG_WIDTH)     # resize the img width to 600 px
    (M, N, _) = img.shape

    # Initialize plot
    px = 1/plt.rcParams['figure.dpi']       # pixel in inches
    fig, ax = plt.subplots(figsize=(N*px, M*px))
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)     # remove all margins
    plt.axis('off')

    ax.imshow(img)     # set image as background
    
    lw = ((PHOTO_COVER * N) / NUM_BARS) * (72 / fig.dpi)
    color = 'w'     # TODO: change this to be more of a blur of the original image

    lines = []
    for i in range(NUM_BARS):
        lines.append( ax.plot([], [], lw=lw, color=color, alpha=OPACITY)[0] )

    # Specify the animation
    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    xs = np.tile(np.linspace(0, N, N), (2, 1)).T
    y  = np.linspace(0, M, 2)

    def animate(i):
        for j in range(NUM_BARS):
            lines[j].set_data(xs[(j * int(N / NUM_BARS) + i) % N], y)
        return lines

    anim = FuncAnimation(fig, animate, init_func=init, frames=N, interval=10, blit=True)
    anim.save(TEMP_FILE, fps=60, extra_args=['-vcodec', 'libx264'], savefig_kwargs={'transparent': True})

    # Speed it up and save as a GIF
    clip = VideoFileClip(TEMP_FILE)

    out_filepath = path_no_format + '_secure.gif'
    final = clip.fx(vfx.speedx, SPEEDUP)
    final.write_gif(out_filepath)

    # Delete temporary mp4 file
    os.remove(TEMP_FILE)

    return out_filepath

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)