# Pornograghy-Check | تشخیص محتوای نامناسب تصاویر

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face](https://img.shields.io/badge/🤗%20Model-NSFW%20Detector-orange)](https://huggingface.co/AdamCodd/vit-base-nsfw-detector)

ابزاری سبک، سریع و مبتنی بر **Vision Transformer (ViT)** برای شناسایی خودکار تصاویر مستهجن (NSFW) و نامناسب. مناسب برای فیلترینگ محتوای کاربران در پلتفرم‌های آنلاین، ربات‌های تلگرام، و سیستم‌های مدیریت محتوا.

## ✨ ویژگی‌ها

- تشخیص با دقت بالا با استفاده از مدل `AdamCodd/vit-base-nsfw-detector`
- قابلیت اجرا روی **CPU** (نیاز به GPU ندارد)
- تنظیم آستانه حساسیت (`threshold`) متناسب با نیاز شما
- استفاده آسان با یک تابع `is_porn()`
- خروجی شامل وضعیت، درصد احتمال و برچسب نهایی

## 📋 پیش‌نیازها

- Python 3.8 یا بالاتر
- کتابخانه‌های ذکر شده در بخش [نصب](#-نصب)

## 🚀 نصب

مخزن را clone کرده و وابستگی‌ها را نصب کنید:

```bash
git clone https://github.com/Reza-Khodayie867/Pornograghy-Check.git
cd Pornograghy-Check
pip install transformers torch pillow
