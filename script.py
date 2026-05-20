
import sys
import argparse
import asyncio
from telegram import Bot

# Configuration
BOT_TOKEN = "8959590252:AAG_Ge7lSG1Tkhi9-sAYS-evr48i5_GIyjM"
CHAT_ID = "1120478717"

async def send_file_cli(file_path, caption=None):
    # Initialize the Telegram Bot
        bot = Bot(token=BOT_TOKEN)
            
                print(f"Uploading {file_path} to Telegram...")
                    try:
                            with open(file_path, 'rb') as file_to_send:
                                        await bot.send_document(
                                                        chat_id=CHAT_ID, 
                                                                        document=file_to_send, 
                                                                                        caption=caption
                                                                                                    )
                                                                                                            print("✅ File sent successfully!")
                                                                                                                except FileNotFoundError:
                                                                                                                        print(f"❌ Error: The file '{file_path}' was not found.", file=sys.stderr)
                                                                                                                            except Exception as e:
                                                                                                                                    print(f"❌ Telegram API Error: {e}", file=sys.stderr)

                                                                                                                                    def main():
                                                                                                                                        parser = argparse.ArgumentParser(description="Send files to Telegram directly from your CLI.")
                                                                                                                                            parser.add_argument("file", help="Path to the file you want to send.")
                                                                                                                                                parser.add_argument("-c", "--caption", help="Optional text caption for the file.")
                                                                                                                                                    
                                                                                                                                                        args = parser.parse_args()
                                                                                                                                                            
                                                                                                                                                                # Run the asynchronous function inside the main CLI thread
                                                                                                                                                                    asyncio.run(send_file_cli(args.file, args.caption))

                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                        main()
