import os
import shutil
import random

def split_dataset(original_dir, output_dir, split_ratio=0.8):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for category in os.listdir(original_dir):
        category_path = os.path.join(original_dir, category)
        if not os.path.isdir(category_path):
            continue

        images = os.listdir(category_path)
        random.shuffle(images)

        split_point = int(len(images) * split_ratio)
        train_images = images[:split_point]
        val_images = images[split_point:]

        train_dir = os.path.join(output_dir, "train", category)
        val_dir = os.path.join(output_dir, "val", category)

        os.makedirs(train_dir, exist_ok=True)
        os.makedirs(val_dir, exist_ok=True)

        for img in train_images:
            shutil.copy(os.path.join(category_path, img), os.path.join(train_dir, img))

        for img in val_images:
            shutil.copy(os.path.join(category_path, img), os.path.join(val_dir, img))

        print(f"✅ Done splitting for {category}: {len(train_images)} train, {len(val_images)} val")

# 👉 Replace these paths with your actual folder locations
original_dataset_dir = 'original_dataset'
output_dataset_dir = 'dataset'

split_dataset(original_dataset_dir, output_dataset_dir)
