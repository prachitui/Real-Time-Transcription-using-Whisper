import time
from jiwer import wer, cer
import whisper

# List of audio files to evaluate
audio_files = ["audio1.wav", "audio2.wav"]

model = whisper.load_model("base")
# Reference transcripts for each audio file
reference_transcripts = [
    "This is the reference transcript for audio1",
    "This is the reference transcript for audio2"
]

# Evaluation results
latency_times = []
wer_scores = []
cer_scores = []

for i, audio_file in enumerate(audio_files):
    # Measure latency
    start_time = time.time()

    # Transcribe using Whisper
    result = model.transcribe(audio_file, language="en")

    end_time = time.time()
    latency = end_time - start_time
    latency_times.append(latency)

    # Calculate WER and CER
    transcription = result['text']
    wer_score = wer(reference_transcripts[i], transcription)
    cer_score = cer(reference_transcripts[i], transcription)

    wer_scores.append(wer_score)
    cer_scores.append(cer_score)

# Output results
for i, audio_file in enumerate(audio_files):
    print(f"Audio File: {audio_file}")
    print(f"Latency: {latency_times[i]:.2f} seconds")
    print(f"WER: {wer_scores[i]:.2%}")
    print(f"CER: {cer_scores[i]:.2%}")
    print()

# Average results
avg_latency = sum(latency_times) / len(latency_times)
avg_wer = sum(wer_scores) / len(wer_scores)
avg_cer = sum(cer_scores) / len(cer_scores)

print(f"Average Latency: {avg_latency:.2f} seconds")
print(f"Average WER: {avg_wer:.2%}")
print(f"Average CER: {avg_cer:.2%}")
