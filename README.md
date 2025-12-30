# Face Detection Test System

This repository contains a simple face detection testing workflow built using:

- FastAPI (Backend API)
- MediaPipe (Face Detection)
- HTML/CSS/JS (Website UI)

## System Flow

Website / Mobile App  
→ Backend API (`/detect-face`)  
→ MediaPipe Face Detection  
→ Normalized coordinates returned  

## Features

- Stateless REST API
- Normalized face coordinates (0–1)
- Bounding box & landmark support
- Canvas-based visualization on website
- Same API used by website and mobile app

