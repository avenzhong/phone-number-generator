import os
import re

# ==========================================
# CONFIGURATION
# ==========================================
DIRECTORY = "/Users/zhongwenjian/Documents/website/phone-number-generator"
ANALYTICS_TAG = '<script src="/assets/analytics.js"></script>'
# ==========================================

def inject_tag(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid duplicate injection
    if 'analytics.js' in content:
        print(f"[-] Skipping {os.path.basename(filepath)}: Tag already present.")
        return

    # Inject immediately after <head>
    # Works for both <head> and <head ...>
    new_content = re.sub(r'(<head.*?>)', r'\1\n    ' + ANALYTICS_TAG, content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[+] Success: {os.path.basename(filepath)}")
    else:
        print(f"[!] Error: <head> tag missing in {os.path.basename(filepath)}")

def main():
    print("🚀 Antigravity Analytics Injection Engine Starting...")
    html_files = [f for f in os.listdir(DIRECTORY) if f.endswith(".html")]
    
    for filename in html_files:
        inject_tag(os.path.join(DIRECTORY, filename))

    print("\n✅ Done! All pages are now linked to /assets/analytics.js")
    print("👉 Now, just edit /assets/analytics.js to set your Measurement ID.")

if __name__ == "__main__":
    main()
