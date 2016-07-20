from . import main_blueprint as main
from .. import get_db,allowed_file
from flask.views import MethodView
from flask import render_template,current_app,url_for,request
from flask import json,send_from_directory
from bson import json_util

#Load the main page
class IndexView(MethodView):
    methods=['GET']

    def get(self):
        return render_template('main/index.html')

#Retrieve list of torrents
class TorrentListView(MethodView):
    methods=['GET']

    def get(self):
        response_body={}

        if request.args.get('q') and request.args.get('q').strip()!='':
            q=request.args.get('q')
            q={
                "name":{
                    '$regex':q
                }
            }

            torrents=get_db().torrents.find(q)
        else:
            torrents=get_db().torrents.find()

        for torrent in torrents:
            if torrent['type']=='torrent':
                torrent['url']=url_for('main.uploaded_file_view',filename=torrent['url'],_external=True)
            response_body.setdefault("torrents",[]).append(torrent)

        response_headers=[('Content-Type','application/json'),('Content-Length',len(response_body))]

        status_code=200

        response_body=json.dumps(response_body,default=json_util.default)

        response=(response_body,status_code,response_headers)

        return response

#Return the torrent file
class ReturnUploadedFileView(MethodView):
    methods=['GET']

    def get(self,filename):
        return send_from_directory(current_app.config['UPLOAD_FOLDER'],filename)

main.add_url_rule('/',view_func=IndexView.as_view('index_view'))
main.add_url_rule('/torrents/',view_func=TorrentListView.as_view('torrent_list_view'))
main.add_url_rule('/uploads/<filename>',view_func=ReturnUploadedFileView.as_view('uploaded_file_view'))
