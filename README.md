# 🖼️ Lambda Image Thumbnail Generator

This AWS Lambda function automatically creates thumbnails when an image is uploaded to an S3 bucket.

---

## ✅ What It Does

- Triggered when an image is uploaded to the `source_image/` folder in S3.
- Renames the file by adding a random suffix.
- Creates a folder under `processed_image/` using the new name.
- Generates resized thumbnails: 200px, 300px, 500px, and 1000px wide.
- Maintains the image format (JPG or PNG).
- Keeps aspect ratio (height auto-adjusts).
- Returns the paths of all generated files as a JSON response.

---

## 📁 Example Folder Structure

If you upload `source_image/photo.jpg`, it creates:

- processed_image/photo_xxxxxxxx/
  - 200_photo_xxxxxxxx.jpg
  - 300_photo_xxxxxxxx.jpg
  - 500_photo_xxxxxxxx.jpg
  - 1000_photo_xxxxxxxx.jpg

---

## 🐳 Setting Up Pillow Layer Using Docker

Since Pillow requires native dependencies, a Lambda-compatible layer must be built using Docker.

### Steps:

1. Create a Dockerfile that installs Pillow and packages it into a zip.
2. Build the Docker image.
3. Run the image to generate `pillow-layer.zip`.
4. Upload the zip file to AWS Lambda as a layer.
5. Attach the layer to your Lambda function.

---

## 🔧 Lambda Setup

1. Set the Lambda **runtime to Python 3.9**.
2. Set the timeout to at least **30 seconds**.
3. Add an **S3 trigger** for the prefix: `source_image/`.
4. Attach the generated **Pillow layer**.
5. Give the Lambda **S3 read/write permissions**.

---

## ✅ Done

Once deployed, uploading any JPG or PNG to `source_image/` will automatically trigger thumbnail generation.
