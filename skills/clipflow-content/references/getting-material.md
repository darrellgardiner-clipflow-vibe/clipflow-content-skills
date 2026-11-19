# Getting the material in

The best posts come from things the owner has already said out loud: a video,
a livestream, a sales call, a client Q&A, a voice note. Your job here is to turn
whatever they have into clean text with timestamps, so later steps can quote
them and point at the exact minute to clip.

You can't watch video. You work from what was said. If a post depends on what
is on screen (a before and after, a product shot), ask them what's there or
mark it as something they need to check.

## Video and audio files

Check for a local transcriber before anything else:

```sh
command -v whisper-cli whisper mlx_whisper ffmpeg
```

**whisper.cpp (`whisper-cli`).** It needs a model file, usually named
`ggml-base.en.bin` or `ggml-small.en.bin`. Look in `~/.cache/whisper-cpp`,
`~/.cache/whisper`, `~/models` and the Homebrew share folder. Convert to 16 kHz
mono WAV first, then transcribe to SRT:

```sh
mkdir -p content/sources
ffmpeg -i "input.mp4" -ar 16000 -ac 1 -c:a pcm_s16le content/sources/name.wav
whisper-cli -m /path/to/ggml-base.en.bin -f content/sources/name.wav -osrt -of content/sources/name
rm content/sources/name.wav
```

**openai-whisper (`whisper`).**

```sh
whisper "input.mp4" --model small --output_format srt --output_dir content/sources
```

For any other local tool, check its `--help` for an SRT or VTT output option.
Use English-only models (`.en`) for English speakers and a multilingual model
otherwise. Transcribe one file first and tell them roughly how long it took,
before starting a folder of long recordings.

**If there's no transcriber,** don't install anything or upload their files
without asking. Offer these, easiest first:

1. **Use the captions they already have.** YouTube Studio lets them download
   subtitles for their own videos, and for a public YouTube video with
   `yt-dlp` installed:
   `yt-dlp --write-auto-subs --sub-langs en --sub-format vtt --skip-download "URL"`.
   Zoom, Teams, Google Meet, Riverside, Descript, Otter and most podcast hosts
   can export a transcript.
2. **Install a free local transcriber** (with their OK). On a Mac with Homebrew:
   `brew install whisper-cpp ffmpeg`, then download a model:
   `curl -L -o ggml-base.en.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.en.bin`.
3. **Paste a transcript** from any tool they already use.

Instagram and TikTok don't export captions. For those, the owner can share the
original video file from their phone or camera roll.

## Cleaning a transcript

Auto-captions repeat lines and carry timing tags (`<00:00:01.040><c> word</c>`).
Collapse them into readable paragraphs of roughly 20 to 40 seconds, each
starting with its time as `[mm:ss]` (or `[h:mm:ss]` past an hour). Keep the
words as spoken. Fix obvious mis-hearings of names and terms only when you are
sure, and note any you're unsure of. Label speakers when there's more than one.

Save the clean version as `content/sources/<short-name>.md` with a line at the
top saying what it is, the date if known, and who's speaking. Keep the raw file
next to it. Add it to `content/sources.md` (see [files](files.md)).

## Past posts and other writing

Posts, captions, emails, website pages, sales pages and reviews they've been
sent are all useful. Screenshots are fine. If they know which posts did well
or brought enquiries, write that down; it matters more than any view count.

## No material: the interview

When they have nothing recorded or written, send these questions in one
message. Tell them rough, long answers are better than polished short ones, and
that a voice memo works: they can record their answers and give you the file.

1. What do you sell, and roughly what does a customer pay?
2. Who is your best kind of customer? Describe the last one you had.
3. What do people ask you before they buy? The questions you answer every week.
4. What do customers get wrong before they come to you?
5. What's something common in your industry that you disagree with?
6. Tell me about a job that went really well, and one that went wrong. What changed after?
7. What happens in a normal week that customers never see?
8. What would you tell a friend who was about to buy this from someone else?
9. What should someone do after seeing a post: call, book, message you, visit?
10. How much time can you give content each week, and what do you hate doing on camera?

Their answers become a source like any other. Tag them `[Interview Q3]`.
If they answer by voice memo, transcribe it as above. Spoken answers usually
give you better hooks and a truer voice than typed ones.
