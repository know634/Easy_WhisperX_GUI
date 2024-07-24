# -- coding: utf-8 --
import whisperx
import pysrt

whisper_arch = r"C:\Users\XGR\Desktop\SoftwareDev\001字幕小工具03（字幕识别）\model\WhisperX_Model\medium"
vad_model_fp = r"C:\Users\XGR\Desktop\SoftwareDev\001字幕小工具03（字幕识别）\model\Vad_Model\whisperx-vad-segmentation.bin"

device = "cuda"

audio_file = r"C:\Users\XGR\Desktop\SoftwareDev\001字幕小工具03（字幕识别）\test\test.mp3"

batch_size = 8  # reduce if low on GPU mem

# 小型GPU（例如，具有2-4GB内存的GPU）：
# batch_size可能需要设置为4或8。
# 中型GPU（例如，具有6-8GB内存的GPU）：
# batch_size可以设置为16、32或64。
# 大型GPU（例如，具有12-16GB内存的GPU）：
# batch_size可以设置为64、128甚至更高。
# 非常大型GPU（例如，具有32GB或更多内存的GPU）：
# batch_size可以设置为256、512或更高。

# 如果内存不足，减小batch_size。
# 如果训练速度较慢，增加batch_size，直到达到内存限制为止。
# 有时使用小批量（mini-batch）可以提供更好的泛化能力。


compute_type = "float16"  # change to "int8" if low on GPU mem (may reduce accuracy)

# 1. Transcribe with original whisper (batched)
model = whisperx.load_model(whisper_arch=whisper_arch, vad_model_fp=vad_model_fp, device=device, compute_type=compute_type, language="zh")

# int8: 速度快，显存使用少，但精度有限。
# int16（cpu）/float16（gpu）: 速度较快，显存使用较少，精度较高。
# float32: 精度最高，但速度较慢，显存使用较多。
# https://opennmt.net/CTranslate2/quantization.html

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size, chunk_size=5, print_progress=True)
output = []
for idx, item in enumerate(result.get("segments")):
    output.append(f"{idx + 1}\n"
                  f"{pysrt.SubRipTime.from_ordinal(1000 * float(item.get('start')))} --> {pysrt.SubRipTime.from_ordinal(1000 * float(item.get('end')))}\n"
                  f"{item.get('text')}\n")
out = "\n".join(output)
with open(r"C:\Users\XGR\Desktop\SoftwareDev\001字幕小工具03（字幕识别）\test\test.srt", "w", encoding="utf-8") as f:
    f.write(out)
