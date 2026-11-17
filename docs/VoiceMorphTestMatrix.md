# Acceptance and security test matrix — NOT RUN
Hardware: Windows 11 x64, NVIDIA RTX 4080 16GB, MAONO PD400X, headphones, VB-CABLE, OBS/Discord.
T-01 hash source/releases and inventory EXE/DLL/archives, Windows Defender scans.
T-02 process/DNS/TCP/UDP/file/autorun activity in disposable VM for first binary startup; separate GPU host smoke if VM cannot pass GPU.
T-03 GPU TensorRT + three licensed RVC models; record device, audio settings, driver, shader/Game GPU load.
T-04 Russian neutral: "Привет, меня хорошо слышно?"; sibilants: "Шесть шустрых мышат шуршат"; emotion: "Что?! Ты серьёзно?"; whisper, sigh, laughter, shout.
T-05 end-to-end mic-to-virtual-output p50/p95 using aligned physical/loopback measurement, p95<1000ms.
T-06 30 min streaming with GPU-intensive game, device unplug/replug, errors and underruns.
T-07 disable external egress, verify offline function with pre-provisioned models.
Any unrun test = NOT_TESTED, not PASS.
