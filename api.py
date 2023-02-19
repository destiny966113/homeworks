"""
[程式能力] 請用 Python-flask 實作一 API Server 
根據 輸入的寬高數值，給予對應大小的 png
圖片顏色不限，可使用各種 pip 套件。回傳時間需小於0.7秒

[GET] /image
    query_data: width: int, height: int

1. Create empty png image
2. Send this binary content to frontend
3. Record basic information with Google Cloud Logging

TODO: return image with BytesIO or temp file content.
"""
import datetime
import os
import time
from io import BytesIO

import cv2
import dotenv
import eventlet
import httplib2
import numpy as np
import pandas as pd
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    MetricType,
    OrderBy,
    RunReportRequest,
)
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from PIL import Image

eventlet.monkey_patch()
import json
import os

from flask import Flask, make_response, request, send_file, send_from_directory
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
from google.cloud import logging

# Load config values directly
config_values = dotenv.dotenv_values()

# Load GCP credential data and initialize google cloud logging
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cred.json"
logging_client = logging.Client()
log_name = "homework-logger"
google_cloud_logger = logging_client.logger(log_name)

# Setup google analytics
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "cred.json", ["https://www.googleapis.com/auth/analytics.readonly"]
)
http = credentials.authorize(httplib2.Http())
service = build(
    "analytics",
    "v4",
    http=http,
    discoveryServiceUrl=("https://analyticsreporting.googleapis.com/$discovery/rest"),
)
client = BetaAnalyticsDataClient()

# region win_handler
def install_handler():
    import sys

    def handler(a, b=None):
        sys.exit(1)

    if sys.platform == "win32":
        print("install handler!!")
        import win32api  # (pywin32)

        win32api.SetConsoleCtrlHandler(handler, True)


install_handler()
# endregion win_handler

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app, supports_credentials=True)

socketio = SocketIO(app, cors_allowed_origins="*", logger=False, engineio_logger=False)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, "PNG", quality=80)
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png", download_name="test.png")


@app.route("/")
def index():
    resp = make_response(json.dumps({"data": "ok"}), 200)
    resp.set_cookie("flask", f"flask{time.time()}")
    return resp


@app.route("/image")
def generate_image():
    width = int(request.args.get("width", 200))
    height = int(request.args.get("height", 200))
    image_array = np.zeros((height, width, 3), np.uint8)
    img = Image.fromarray(image_array)
    img.save("test.png")
    google_cloud_logger.log_text(
        json.dumps(
            {"width": width, "height": height, "created_at": str(datetime.datetime.utcnow())}
        )
    )
    return send_from_directory(".", "test.png", as_attachment=True)


@socketio.on("connect")
def connect():
    print(f"{request.sid} on connect")


@socketio.on("disconnect")
def disconnect():
    print(f"{request.sid} on disconnect")


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=config_values.get("SYSTEM_PORT", 5000), debug=False)
