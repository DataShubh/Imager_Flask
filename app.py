from flask import Flask,  render_template, request, send_file
import numpy
import io
from PIL import Image
from io import BytesIO
app = Flask(__name__)


@app.route('/')
def index():

    return (render_template("index.html"))



@app.route('/', methods= ['GET', 'POST'])
def create_image( ):
        
        if request.method =="POST" :
            height = int(request.form['height'])
            
            width = int(request.form['width'])
            
            color = request.form['color']
            
            img_format = request.form['img_format']
            
        
        if not isinstance(height, int) or height <= 0:
                return "400 Bad Request. Enter a valid value for height", 400
        if not isinstance(width, int) or width <= 0:
                return "400 Bad Request. Enter a valid value for width", 400
        
        # Generate image array
        if color == 'red':
            rgb = (255, 0, 0)
        elif color == 'green':
            rgb = (0, 255, 0)
        elif color == 'blue':
            rgb = (0, 0, 255)
        
        image = Image.new('RGB', (height, width), rgb)
        image_io = io.BytesIO()
        # Convert the image to an array in the specified format
        if img_format == 'jpeg':
            image.save(image_io, format="JPEG")
            image_io.seek(0)
            return (
            send_file(image_io,
            mimetype='image/jpeg')) 

        elif img_format == 'png':
            image.save(image_io, format="PNG")
            image_io.seek(0)
            return (
            send_file(image_io,
            mimetype='image/png'))
            
        elif img_format == 'gif':
            image.save(image_io, format="PNG")
            image_io.seek(0)
            return (
            send_file(image_io,
            mimetype='image/gif'))
        
       
if __name__ =="__main__":
    app.run(debug= True, port = 5000)