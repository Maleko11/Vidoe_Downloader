from flask import Blueprint, render_template, request
from download import Download

auth = Blueprint('auth', __name__)


@auth.route("/")
def home():
	return render_template("home.html", error=None, style="error")


@auth.route("/download", methods=['GET', 'POST'])
def download():
	if request.method == 'POST':
		video_link = request.form['link']
		if str(video_link).startswith("https://www.youtube.com"):
			srz_download = Download(video_link)
			downloaded_video = srz_download.download_youtube_video()
			if downloaded_video:
				mp3_file = srz_download.convert_video_to_mp3(downloaded_video)
				srz_download.delete_file(downloaded_video)
				return render_template("home.html", error=f"{srz_download.name} is downloaded", style="success")
			else:
				return render_template("home.html", error="Video download failed.", style="error")
		else:
			return render_template("home.html", error="Invalid Youtube link", style="error")
	else:
		return render_template("home.html", error=None, style="success")
