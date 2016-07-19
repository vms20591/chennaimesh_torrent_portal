import os
from bson import json_util
from flask import Flask
from flask import request,render_template,redirect,url_for
from flask_pymongo import PyMongo
from flask import json
from flask import send_from_directory
from werkzeug.utils import secure_filename

#Some global config vars
ALLOWED_EXTENSIONS = set(['torrent'])
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR,'uploads')

#Create app object
app=Flask(__name__)

#Set app config vars
app.config['MONGO_DBNAME']="torrentstash"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['BASE_DIR']=BASE_DIR

#Create Mongo object
mongo=PyMongo(app)

#Helper to check if a file is in allowed list
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#Load the main page
@app.route('/')
def index_view():
    return render_template('index.html')

#Retrieve list of torrents
@app.route('/torrents/')
def torrent_list_view():
    response_body={}
        
    for torrent in mongo.db.torrents.find():
        if torrent['type']=='torrent':
            torrent['url']=url_for('uploaded_file',filename=torrent['url'],_extername=True)
        response_body.setdefault("torrents",[]).append(torrent)
                                                                
    response_headers=[('Content-Type','application/json'),('Content-Length',len(response_body))]
                                                                    
    status_code=200

    response_body=json.dumps(response_body,default=json_util.default)
                                                                                                    
    response=(response_body,status_code,response_headers)

    return response

#Return the torrent file
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print filename
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

#Upload torrent file
@app.route('/upload/',methods=['POST'])
def uploads():
    if 'torrent-file' not in request.files:
        return redirect(url_for('index_view'))

    f=request.files['torrent-file']
    
    if f.filename=='':
        return redirect(url_for('index_view'))
    
    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return redirect(url_for('index'))

#Run the app if its a main module
if __name__=='__main__':
    app.run(debug=True)
