from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

# Cria a pasta de downloads se não existir
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Rota principal, carrega o formulário
@app.route('/')
def home():
    return render_template('index.html')

# Rota que trata o download via POST
@app.route('/baixar', methods=['POST'])
def baixar():
    url = request.form['url']
    nome_arquivo = f"{uuid.uuid4()}.mp4"
    caminho = os.path.join(DOWNLOAD_FOLDER, nome_arquivo)

    ydl_opts = {
        'outtmpl': caminho,
        'format': 'bestaudio+best',
        'merge_output_format': 'mp4'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return send_file(caminho, as_attachment=True)
    except Exception as e:
        return f"Erro ao baixar o vídeo: {str(e)}"

# Executa o servidor
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

