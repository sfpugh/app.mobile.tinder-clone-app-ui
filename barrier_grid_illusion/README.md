# Barrier Grid Illusion
Barrier Grid Illusion is an animation of lateraly moving lines on top of a static image. When the lines move very quickly, the human eye is able to see the (mostly unobscured) image underneath. However, if a snapshot of the animation is taken, the image is obscured by the lines. D-fence technology patented this idea in 2014. I have re-implemented it here in Python using the Matplotlib and Moviepy modules.

<p align="middle">
  <img src="example/bgi_original.jpg" width="32%" />
  <img src="example/bgi_original_secure.gif" width="32%" /> 
  <img src="example/bgi_screenshot.jpg" width="32%" />
</p>

## Usage
Create a virtual environment using Python3 virtualenv.
```
cd barrier_grid_illusion

python3 -m venv bgi_env
source bgi_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

While the environment is active, run the python script which starts a Flask server.
```
python barrier_grid_illusion.py
```

While the server is running, issue a GET request of the following form to render a GIF of an image with a barrier grid illusion added.
```
GET http://127.0.0.1/5000/secure_image?img_path=[path-to-image]
```

The GIF will be in the same location as the original image. Use `Ctrl-C` to terminate the server and command `deactivate` to close the virtual enviroment.