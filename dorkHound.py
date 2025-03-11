from googlesearch import search 
import time

# Categorized Google Dorks
DORK_CATEGORIES = {
    "1": ("People Search", {
        "1": ('Find Public Facebook Profiles', 'site:facebook.com "{query}"'),
        "2": ('Find Public Facebook Posts', 'site:facebook.com/posts "{query}"'),
        "3": ('Find LinkedIn Profiles', 'site:linkedin.com/in "{query}"'),
    }),
    "2": ("Files & Documents", {
        "1": ('Find Exposed PDFs', 'filetype:pdf "{query}"'),
        "2": ('Find Exposed Excel Files', 'filetype:xls OR filetype:xlsx "{query}"'),
        "3": ('Find Open Google Drive Docs', 'site:docs.google.com "{query}"'),
    }),
    "3": ("Website Security", {
        "1": ('Find Open Directories', 'intitle:"index of" "{query}"'),
        "2": ('Find SQL Injection Vulnerable Sites', 'inurl:index.php?id= "{query}"'),
        "3": ('Find Exposed Admin Panels', 'inurl:admin/login "{query}"'),
    }),
    "4": ("Custom Dork Search", None)  # User-defined dork
}

def perform_search(dork, query):
    """ Perform a Google search and return results. """
    full_query = dork.format(query=query)
    print(f"\n[+] Searching: {full_query}\n")
    
    try:
        results = [url for url in search(full_query, num=10, stop=10, pause=2)]
        for idx, url in enumerate(results, start=1):
            print(f"{idx}. {url}")
        return results
    except Exception as e:
        print(f"[-] Error: {e}")
        return []

def save_results(results):
    """ Save results to a file """
    if results:
        filename = f"google_dork_results_{int(time.time())}.txt"
        with open(filename, "w") as f:
            f.write("\n".join(results))
        print(f"[+] Results saved to {filename}")

def main():
    while True:
        # Display Categories
        print("\n====== Google Dorking OSINT Tool ======")
        for key, (category, _) in DORK_CATEGORIES.items():
            print(f"{key}. {category}")
        print("0. Exit")

        cat_choice = input("\n[?] Choose a category: ").strip()
        
        if cat_choice == "0":
            print("[+] Exiting.")
            break
        elif cat_choice in DORK_CATEGORIES:
            category_name, dork_options = DORK_CATEGORIES[cat_choice]

            # Handle Custom Dork Input
            if cat_choice == "4":
                dork = input("[?] Enter your custom Google Dork query: ")
                query = input("[?] Enter a search term (if needed): ")
            else:
                # Display Dorks in the Selected Category
                print(f"\n====== {category_name} ======")
                for key, (desc, _) in dork_options.items():
                    print(f"{key}. {desc}")
                print("0. Back")

                dork_choice = input("\n[?] Choose a dork: ").strip()
                
                if dork_choice == "0":
                    continue  # Go back to main menu
                elif dork_choice in dork_options:
                    desc, dork = dork_options[dork_choice]
                    print(f"\n[+] Selected: {desc}")
                    query = input("[?] Enter search term (e.g., a name or keyword): ")
                else:
                    print("[-] Invalid choice. Try again.")
                    continue
            
            results = perform_search(dork, query)
            save_option = input("[?] Save results? (y/n): ").strip().lower()
            if save_option == "y":
                save_results(results)

        else:
            print("[-] Invalid choice. Try again.")

if __name__ == "__main__":
    main()