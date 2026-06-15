import whisper
import os
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

model = whisper.load_model("base")

result = model.transcribe(
    r"audio\Hannah_Bahng_OLeander_Audio_(getmp3.pro).mp3"
)

print("\nTranscription:\n")
print(result["text"])

os.makedirs("transcripts", exist_ok=True)
os.makedirs("summaries", exist_ok=True)

# ---------------------------
# 1. Save timestamped transcript
# ---------------------------
with open("transcripts/output.txt", "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()

        f.write(f"[{start:.2f}s - {end:.2f}s] {text}\n")

print("\nTranscript saved to transcripts/output.txt")

# ---------------------------
# 2. Generate summary (ONLY ONCE)
# ---------------------------
parser = PlaintextParser.from_string(result["text"], Tokenizer("english"))
summarizer = LsaSummarizer()

summary = summarizer(parser.document, 3)

print("\nSummary:\n")

with open("summaries/summary.txt", "w", encoding="utf-8") as f:
    for sentence in summary:
        print(sentence)
        f.write(str(sentence) + "\n")

print("\nSummary saved to summaries/summary.txt")