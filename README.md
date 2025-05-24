# Pi-Whisper-RSS25-Workshop

This repository contains evaluation data and transcription outputs supporting the work:

### **Performance Evaluation of Whisper-Series Speech Transcription Models on Raspberry Pi**

This work evaluated:

* The original [OpenAI Whisper](https://github.com/openai/whisper) implementation
* The [Faster-Whisper](https://github.com/guillaumekln/faster-whisper) re-implementation

across four different Raspberry Pis:

* Raspberry Pi 4 (4GB)
* Raspberry Pi 5 (4GB, 8GB, 16GB)

---
## 📊 Evaluation Tasks

We evaluate models across two test tests:

| Test Sets          | Description                                             |
| ---------------- | ------------------------------------------------------- |
| **Common Voice** | short single-sentence speech clips from [Common Voice](https://commonvoice.mozilla.org/en/datasets)  (10 clips total)   |
| **AP News**      | 1–2 minutes long AP news clips (5 clips total) |

