import streamlit as st

from parser import parse_srt, build_srt
from translator import translate_batch

st.set_page_config(
page_title="Subtitle Translator",
page_icon="🎬"
)

st.title("🎬 مترجم زیرنویس")

api_key = st.text_input(
"Gemini API Key",
type="password"
)

uploaded_file = st.file_uploader(
"فایل SRT را انتخاب کنید",
type=["srt"]
)

if uploaded_file is not None:

```
st.success("فایل بارگذاری شد")

if st.button("شروع ترجمه"):

    if not api_key:
        st.error("API Key را وارد کنید")

    else:

        content = uploaded_file.read().decode(
            "utf-8",
            errors="ignore"
        )

        subtitles = parse_srt(content)

        progress = st.progress(0)

        batch_size = 10
        total = len(subtitles)

        for start in range(0, total, batch_size):

            end = start + batch_size

            batch = subtitles[start:end]

            texts = [
                item["text"]
                for item in batch
            ]

            translated = translate_batch(
                texts,
                api_key
            )

            for i, text in enumerate(translated):
                batch[i]["text"] = text

            progress.progress(
                min(end / total, 1.0)
            )

        final_srt = build_srt(subtitles)

        st.success("ترجمه کامل شد")

        st.download_button(
            label="دانلود زیرنویس",
            data=final_srt,
            file_name="translated.srt",
            mime="text/plain"
        )
```
