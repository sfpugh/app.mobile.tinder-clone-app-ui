# barrier_grid_illusion.py
# Flask server that accepts GET requests and returns
# the requestor-supplied image with a barrier grid 
# illusion on top of it.

import sys
import numpy as np
import os
from flask import Flask, request
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from moviepy.editor import *

NUM_BARS    = 16
PHOTO_COVER = 0.5
OPACITY     = 0.8
TEMP_MP4    = 'temp.mp4'
SPEEDUP     = 200

app = Flask(__name__)

@app.route('/secure_image', methods=['GET'])
def secure_image():
    # Get the image specified by the requestor
    img_filepath = str(request.args['img_path'])
    path_no_format, img_format = img_filepath.rsplit('.', 1)

    img = plt.imread(img_filepath, format=img_format)
    (M,N,_) = img.shape

    # Initialize plot
    fig, ax = plt.subplots()
    plt.axis('off')
    ax.imshow(img)     # set image as background
    
    lw = ((PHOTO_COVER * M) / NUM_BARS) / 2
    avg_color = img.mean(axis=0).mean(axis=0)

    lines = []
    for i in range(NUM_BARS):
        lines.append( ax.plot([], [], lw=lw, color=avg_color, alpha=OPACITY)[0] )

    # Specify the animation
    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    xs = np.tile(np.linspace(0, N, N), (2,1)).T
    y  = np.linspace(0, N, 2)

    def animate(i):
        for j in range(NUM_BARS):
            lines[j].set_data(xs[(j * int(M/NUM_BARS) + i) % 600], y)
        return lines

    anim = FuncAnimation(fig, animate, init_func=init, frames=M, interval=10, blit=True)
    anim.save(TEMP_MP4, fps=60, extra_args=['-vcodec', 'libx264'])

    # Speed it up and save as a GIF
    clip = VideoFileClip(TEMP_MP4)
    final = clip.fx(vfx.speedx, SPEEDUP)

    out_filepath = path_no_format + '_secure.gif'
    final.write_gif(out_filepath)

    # Delete temporary mp4 file
    os.remove(TEMP_MP4)

    return out_filepath

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)