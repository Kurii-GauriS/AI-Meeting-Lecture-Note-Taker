<h1>🎙️ AI Meeting Note Taker (Whisper)</h1>
<h4>❤️
An AI-powered application that converts audio recordings into transcripts with timestamps and generates automatic summaries using Natural Language Processing.<h4>
I used my fav song beacuse i like it...
its amazing song by <h1>❤️⭐Hanna bahng⭐❤️<h1>
Song name: OLeander ⭐<br>⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚⋆˚☆˖°⋆｡° ✮˖ ࣪ ⊹⋆.˚</h1>
<br>
<h3>
So for Emojis i used <br>
https://emojidb.org/thunder-emojis
<br><br><br>
✨ Features<br>
🎧 Converts MP3 audio to text using OpenAI Whisper<br>
⏱️ Generates timestamped transcripts<br>
🧠 Automatically summarizes content using NLP (Sumy)<br>
📁 Saves transcripts and summaries into separate folders<br>
💻 Works completely offline (no API required)<br>
🐍 Built with Python<br><br>
<br>
🛠️ Tech Stack<br>
Python<br>
Whisper (OpenAI)<br>
FFmpeg<br>
Sumy (NLP summarization)<br>
NLTK<br>
<br>
📋pip list<br>
<br>Package            Version<br>
------------------ ---------<br>
breadability       0.1.20<br>
certifi            2026.5.20<br>
chardet            7.4.3<br>
charset-normalizer 3.4.7<br>
click              8.4.1<br>
colorama           0.4.6<br>
docopt             0.6.2<br>
docopt-ng          0.9.0<br>
filelock           3.29.4<br>
fsspec             2026.4.0<br>
idna               3.18<br>
Jinja2             3.1.6<br>
joblib             1.5.3<br>
llvmlite           0.47.0<br>
lxml               6.1.1<br>
lxml_html_clean    0.4.5<br>
MarkupSafe         3.0.3<br>
more-itertools     11.1.0<br>
mpmath             1.3.0<br>
networkx           3.6.1<br>
nltk               3.9.4<br>
numba              0.65.1<br>
numpy              2.4.6<br>
openai-whisper     20250625<br>
pip                24.0<br>
pycountry          26.2.16<br>
regex              2026.5.9<br>
requests           2.34.2<br>
setuptools         81.0.0<br>
sumy               0.12.0<br>
sympy              1.14.0<br>
tiktoken           0.13.0<br>
torch              2.12.0<br>
tqdm               4.68.2<br>
typing_extensions  4.15.0<br>
urllib3            2.7.0<br><br>
📂 Project Structure<br>
AI meeting note tracker/<br>
│<br>
├── app.py          <br>        # Main Python script<br>
├── audio/                  <br># Input audio files (MP3)<br>
├── transcripts/           <br> # Generated transcripts<br>
│   └── output.txt<br>
├── summaries/             <br># Generated summaries<br>
│   └── summary.txt<br>
├── requirements.txtv<br>
├── venv/                <br>  # Virtual environment (ignored in GitHub)<br>
└── README.mdv<br><br><br><h3>
🚀 How It Works<br>
User places an audio file in the audio/ folder<br>
Whisper converts speech → text<br>
Script generates timestamped transcript<br>
NLP model summarizes the transcript<br>
Output saved in transcripts/ and summaries/<br><br></h3>
<h1>⚙️ Installation & Setup</h1><br>
<h2>1. Clone the repository <br>
git clone <br>https://github.com/your-username/ai-meeting-note-taker.git<br>
cd ai-meeting-note-taker<br>
2. Create virtual environment<br>
python -m venv venv<br>
venv\Scripts\activate<br>   # Windows<br>
3. Install dependencies<br>
pip install -r requirements.txt<br>
<br><br>
If installing manually:<br>
<br>
pip install openai-whisper<br>
pip install torch<br>
pip install sumy nltk<br>
4. Install FFmpeg<br>
Download FFmpeg<br>
Add bin folder to system PATH<br>
Verify:<br>
ffmpeg -version<br>
5. Run the project<br>
python app.py<br><br></h2>
<h1>📊 Output Example</h1><br><h2>
📝 Transcript<br>
[0.00s - 4.50s] Hello everyone, today's meeting starts now.<br>
[4.50s - 10.20s] We will discuss project deadlines.<br></h2>
<h1>🧠 Summary</h1>
<h2>Today's meeting focuses on project deadlines and planning.<br>
💡 Use Cases<br>
🎓 Lecture note generation<br>
🏢 Meeting transcription<br>
🎤 Interview analysis<br>
📚 Study material creation<br>
📌 Future Improvements<br>
🌐 Web UI using Streamlit<br>
🤖 AI-powered advanced summarization (GPT-style)<br>
📄 Export to PDF / Word<br>
👥 Speaker diarization (who spoke when)<br>
🔊 Real-time transcription<br><br></h2>
<h1>👩‍💻 Author<br>
<i>Gauri Sangare</i>
</h1>
