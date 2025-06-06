from content_generator.crypto_reels_generator import generate_crypto_reel

if __name__ == "__main__":
    reel = generate_crypto_reel()
    print("\n🎬 REEL SCRIPT")
    print(f"🎯 Title: {reel['title']}")
    print(f"📜 Script:\n{reel['script']}")
    print(f"📌 Hashtags: {', '.join(reel['hashtags'])}")
    print(f"🔁 CTA: {reel['cta']}")
