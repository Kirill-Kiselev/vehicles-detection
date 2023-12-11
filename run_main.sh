#!/bin/bash

# Проверяем, переданы ли оба параметра
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <path> <polygon_path>"
    exit 1
fi

# Считываем параметры
video_path=$1
polygon_path=$2
output_path=$3

# Запускаем Python скрипт с переданными параметрами
python -m src.main.py "$video_path" "$polygon_path" "$output_path"
