#!/usr/bin/env bash
set -e

cd dut_green_tracker_fixed

echo "==> Running flutter pub get..."
flutter pub get

echo "==> Building Flutter web app..."
flutter build web --release

echo "==> Build complete. Output in dut_green_tracker_fixed/build/web"
