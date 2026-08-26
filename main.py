import sys
import yt_dlp

def get_direct_url(youtube_url):
    ydl_opts = {
        'format': 'best',
        'quiet': False, # এটি False করে দিলাম যাতে ডিটেইলস দেখা যায়
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Fetching info for: {youtube_url}")
            info_dict = ydl.extract_info(youtube_url, download=False)
            video_url = info_dict.get('url', None)
            return video_url
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <youtube_video_url>")
        sys.exit(1)
        
    url = sys.argv[1]
    stream_url = get_direct_url(url)
    
    if stream_url:
        print("\n--- Direct Stream URL Found ---")
        print(stream_url)
    else:
        print("\n[!] Failed to fetch stream URL.")
