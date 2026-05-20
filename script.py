#!/usr/bin/env python3
import sys
import os
import argparse
import asyncio
import zipfile
from telegram import Bot

BOT_TOKEN = "8959590252:AAG_Ge7lSG1Tkhi9-sAYS-evr48i5_GIyjM"
CHAT_ID = "1120478717"

async def send_file_cli(file_path, caption=None):
    bot = Bot(token=BOT_TOKEN)
    try:
        print(f"Uploading {file_path} to Telegram...")
        with open(file_path, 'rb') as file_to_send:
            await bot.send_document(
                chat_id=CHAT_ID, 
                document=file_to_send, 
                caption=caption
            )
        print("✅ File sent successfully!")
    except Exception as e:
        print(f"❌ Telegram API Error: {e}", file=sys.stderr)

# Helper function to zip a directory
def zip_folder(folder_path):
    zip_path = f"{folder_path.rstrip('/')}.zip"
    print(f"📦 Compressing folder into {zip_path}...")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                # Keep relative structure inside the zip
                rel_path = os.path.relpath(full_path, os.path.dirname(folder_path))
                zipf.write(full_path, rel_path)
    return zip_path

def main():
    parser = argparse.ArgumentParser(description="Send files or folders to Telegram.")
    parser.add_argument("target", help="Path to the file or folder you want to send.")
    parser.add_argument("-c", "--caption", help="Optional text caption.")
    parser.add_argument(
        "--mode", 
        choices=["zip", "files"], 
        default="zip", 
        help="For folders: 'zip' sends one compressed archive, 'files' sends each item separately."
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.target):
        print(f"❌ Error: The path '{args.target}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # If target is a folder
    if os.path.isdir(args.target):
        if args.mode == "zip":
            # Method A: Zip and send
            zipped_file = zip_folder(args.target)
            asyncio.run(send_file_cli(zipped_file, args.caption))
            # Optional: Delete zip archive locally after uploading
            # os.remove(zipped_file)
        else:
            # Method B: Loop through all files individually
            print(f"📂 Scanning folder: {args.target}")
            for root, dirs, files in os.walk(args.target):
                for file in files:
                    file_path = os.path.join(root, file)
                    asyncio.run(send_file_cli(file_path, f"{args.caption or ''} ({file})".strip()))
    else:
        # If target is just a standard file
        asyncio.run(send_file_cli(args.target, args.caption))

if __name__ == "__main__":
    main()
    
