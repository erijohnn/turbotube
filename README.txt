# TURBOTUBE - DEPLOY NO RENDER

## PASSO A PASSO PARA COLOCAR ONLINE

1. Crie uma conta gratuita em https://render.com
2. Crie uma conta no GitHub (https://github.com)
3. Crie um novo repositório chamado "turbotube"
4. Faça upload de todos os arquivos deste ZIP no GitHub
5. Vá até o site da Render.com e clique em "New Web Service"
6. Conecte sua conta GitHub e selecione o repositório "turbotube"
7. Configure:
   - Build Command: pip install -r requirements.txt
   - Start Command: python app.py
   - Environment: Python 3
8. Clique em "Create Web Service"

Em 1 a 2 minutos, seu site estará online com um link como:
https://turbotube.onrender.com

Cole um link do YouTube e clique em "Baixar em Alta Qualidade" para testar.
