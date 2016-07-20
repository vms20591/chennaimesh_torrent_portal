import os
from flask.views import MethodView
from flask import render_template,request,url_for,redirect
from werkzeug.utils import secure_filename
from . import auth_blueprint as auth

#Load the index page
class IndexView(MethodView):
    methods=['GET']
    
    def get(self):
        return render_template('auth/index.html')

#Upload torrent file
@auth.route('/upload/',methods=['POST'])
class UploadFileView(MethodView):
    methods=['POST']
    
    def post(self):
        if 'torrent-file' not in request.files:
            return redirect(url_for('auth.auth_view'))

        f=request.files['torrent-file']
        
        if f.filename=='':
            return redirect(url_for('auth.auth_view'))
        
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        return redirect(url_for('auth.auth_view'))
	
auth.add_url_rule('/',view_func=IndexView.as_view('auth_view'))
auth.add_url_rule('/upload/',view_func=UploadFileView.as_view('upload_file_view'))
