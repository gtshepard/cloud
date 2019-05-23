import os
import time
import time
#import datetime
from flask import Flask, request, jsonify, render_template
app = Flask(__name__, template_folder='templates')
from flask import request

current_time = 10
@app.route("/home", methods=['GET', 'POST'])
def home():
        global current_time
        print(request.remote_addr)
        try:
            if request.method == 'POST':
                try:
                    print("What", request.form)
                    if request.form.get('getTime'):
                        print("getTime test")
                    print("Post test")
                except:
                    print("form failed")
                data = {}
                try:
                    data['time'] = request.json['time']
                except:
                    print("Failed to request data")
        except:
            print("rip")
        return render_template('main_page.html', timestamp = current_time)# app.send_static_file("/templates/main_page.html")


if __name__ == '__main__':
    app.run(debug=True)
