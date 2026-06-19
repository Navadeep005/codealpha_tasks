import os
import shutil
import re
import requests

def run_automation_suite():
    print("=======================================")
    print("   CodeAlpha Task Automation Suite     ")
    print("=======================================")

    # IDEA 1: Scrape the title of a webpage (Uses: 'requests', 're', File Handling)
   
    print("\n--- Running Task 1: Web Scraping & Extraction ---")
    target_url = "https://www.google.com"
    
    try:
        response = requests.get(target_url, timeout=10)
        # Verify the request was successful
        if response.status_code == 200:
            html_content = response.text
            
            # Using regex (re) to find the text between <title> and </title> tags
            title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
            
            if title_match:
                web_title = title_match.group(1).strip()
                print(f"[*] Successfully scraped title: '{web_title}'")
                
                # Save the scraped title to a text file
                with open("scraped_title.txt", "w", encoding="utf-8") as f:
                    f.write(f"Website URL: {target_url}\n")
                    f.write(f"Extracted Title: {web_title}\n")
                print(" -> Saved title to 'scraped_title.txt'")
            else:
                print("[!] Could not find a <title> tag on the page.")
        else:
            print(f"[-] Failed to fetch webpage. HTTP Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"[-] Network/Request Error: {e}")

    # IDEA 2: Extract email addresses from a file (Uses: 're', File Handling)
   
    print("\n--- Running Task 2: Email Extraction via Regex ---")
    
    # Mock a sample text file with emails to simulate a real file handling task
    sample_text = """
    Hello team, please send the quarterly reports to manager.alpha@codealpha.com.
    For technical support, open a ticket or contact support123@example.org immediately.
    Note: invalid-email@com or contact@hr without an extension won't work.
    """
    source_file = "raw_data.txt"
    output_emails_file = "extracted_emails.txt"
    
    # Writing the sample text to a file first
    with open(source_file, "w") as f:
        f.write(sample_text)
        
    # Reading the file and extracting emails using regular expressions
    try:
        with open(source_file, "r") as f:
            content = f.read()
            
        # Standard robust regex pattern for finding email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        found_emails = re.findall(email_pattern, content)
        
        if found_emails:
            # Keep unique emails only
            unique_emails = list(set(found_emails))
            print(f"[*] Found {len(unique_emails)} unique email(s): {unique_emails}")
            
            # Save extracted emails to a new file
            with open(output_emails_file, "w") as f:
                for email in unique_emails:
                    f.write(email + "\n")
            print(f" -> Extracted emails saved to '{output_emails_file}'")
        else:
            print("[!] No valid email addresses found in the file.")
    except IOError as e:
        print(f"[-] File Handling Error: {e}")

    # IDEA 3: File Organization / Moving .jpg files (Uses: 'os', 'shutil')
    
    print("\n--- Running Task 3: File Organization & Sorting ---")
    
    source_dir = "./source_folder"
    target_dir = "./organized_images"
    
    # Dynamically setup dummy environment folders and sample files for demonstration
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    
    dummy_files = ["photo1.jpg", "document.pdf", "vacation.jpg", "notes.txt"]
    for file_name in dummy_files:
        # Create empty placeholder files in the source directory
        with open(os.path.join(source_dir, file_name), "w") as f:
            f.write("dummy content")
            
    print(f"📁 Created dummy source files inside '{source_dir}' for testing.")

    try:
        # List all items in the directory
        files_in_source = os.listdir(source_dir)
        moved_count = 0
        
        for file in files_in_source:
            # Check if the file ends with the .jpg extension
            if file.lower().endswith('.jpg'):
                current_file_path = os.path.join(source_dir, file)
                destination_file_path = os.path.join(target_dir, file)
                
                # Move the file from source to destination
                shutil.move(current_file_path, destination_file_path)
                print(f"  Moved: {file} -> {target_dir}/")
                moved_count += 1
                
        print(f"[*] File cleanup complete. Total .jpg files moved: {moved_count}")
    except Exception as e:
        print(f"[-] Error during file moving operation: {e}")

    print("\n=======================================")
    print("   All Tasks Executed Successfully!    ")
    print("=======================================")

if __name__ == "__main__":
    run_automation_suite()