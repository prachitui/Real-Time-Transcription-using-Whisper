# Real-Time Transcription System Using Whisper

## Table of Contents
 - [Overview](#overview)
 - [Features](features)
 - [Setup and Requirements](#setup-and-requirements)
 - [Usage](#usage)
 - [Issues](#issues)
 - [Evaluation Results](#evaluation-results)
 

   
## Overview
This repository contains an implementation of a real-time speech-to-text transcription system using OpenAI's Whisper model. The system processes live audio input in 
real-time, transcribing it with minimal delay and high accuracy. In addition to real-time transcription, the system includes an evaluation component that measures key
performance metrics such as:
- **Latency**: The time delay between speaking and the transcription being displayed.
- **Word Error Rate (WER)**: The percentage of incorrect words in the transcription.
- **Character Error Rate (CER)**: The percentage of incorrect characters in the transcription.

The evaluation is performed using pre-recorded audio files, providing insights into the system's accuracy and efficiency under different conditions.

## Features

- **Real-Time Transcription**: Transcribes speech from a live audio stream with minimal delay.
- **Whisper Model Integration**: Utilizes OpenAI's Whisper model for accurate transcription.
- **Low Latency**: Transcriptions are processed in real-time, making it suitable for live applications.
- **Customizable**: Supports multiple Whisper model sizes (`tiny`, `base`, `small`, `medium`, `large`) for different performance and accuracy requirements.
- **Evaluated**: Provides performance evaluation for transcription accuracy and latency.


## Setup and Requirements

To get started, ensure you have the following installed:
- Python>=3.7
- ```bash
     pip install sounddevice numpy scipy jiwer
     pip install openai-whisper

  ```

## Usage
### Clone the Repository

```bash
   git clone https://github.com/prachitui/Real-Time-Transcription-System-Using-Whisper.git
   cd Real-Time-Transcription-System-Using-Whisper
```
### Running the Real-Time Transcription System
``` bash
    python real_time_transcription.py
```
### Evaluation
``` bash
    python evaluate_transcription.py
```
## Issues

Noise Sensitivity: The transcription accuracy may degrade in noisy environments. 

## Evaluation Results

The system was evaluated on pre-recorded audio files to measure transcription latency and accuracy. Below are the results from two audio files:

### Audio File: `audio1.wav`
- **Latency**: 1.52 seconds
- **Word Error Rate (WER)**: 4.12%
- **Character Error Rate (CER)**: 2.38%

### Audio File: `audio2.wav`
- **Latency**: 1.48 seconds
- **Word Error Rate (WER)**: 5.89%
- **Character Error Rate (CER)**: 3.05%

### Averages
- **Average Latency**: 1.50 seconds
- **Average WER**: 5.01%
- **Average CER**: 2.72%
