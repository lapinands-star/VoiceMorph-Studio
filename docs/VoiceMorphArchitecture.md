# Architecture — intended reuse, not implementation
Input mic (WASAPI) → current vc-rs ring buffers → optional RNNoise/GTCRN (bounded delay) → ContentVec + RMVPE + RVC ONNX via TensorRT → chunk join/OLA/SOLA → playback endpoint → external VB-CABLE → OBS/Discord.
Keep real-time callback independent of model inference. Track p50/p95 mic-output and underruns, not inference-only timing.
Only scope a minimal profile-switching/offline patch after current GUI behavior is proven insufficient.
No new inference backends or custom kernel driver in MVP.
