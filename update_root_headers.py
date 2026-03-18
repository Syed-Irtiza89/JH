import os

# Navbar HTML for root pages (index.html is already correct, but this ensures others match)
ROOT_NAVBAR = """        <nav class="navbar navbar-expand-lg fixed-top" id="mainNavbar">
            <div class="container">
                <a class="navbar-brand d-flex align-items-center" href="index.html">
                    <img src="images/logo.png" class="navbar-brand-image img-fluid me-2" alt="J & H Painting"
                        style="max-width: 100px; height: auto; width: auto; filter: none !important;">
                </a>
                <div class="d-lg-none ms-auto me-3">
                    <a class="btn custom-btn custom-border-btn btn-ripple" data-bs-toggle="offcanvas"
                        href="#offcanvasExample" role="button" aria-controls="offcanvasExample"
                        style="background-color: white; border-color: white; color: #6d16df; backdrop-filter: blur(5px); font-weight: 600; padding: 8px 20px; border-radius: 50px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">Free
                        Quote</a>
                </div>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"
                    style="background: transparent; border: none; padding: 6px 8px; outline: none; box-shadow: none;">
                    <span style="display: flex; flex-direction: column; gap: 5px; width: 26px;">
                        <span
                            style="display:block; height:2.5px; background: linear-gradient(90deg,#6d16df,#0dbbc9); border-radius:2px; transition: all 0.3s;"></span>
                        <span
                            style="display:block; height:2.5px; background: linear-gradient(90deg,#6d16df,#0dbbc9); border-radius:2px; width:70%; transition: all 0.3s;"></span>
                        <span
                            style="display:block; height:2.5px; background: linear-gradient(90deg,#6d16df,#0dbbc9); border-radius:2px; transition: all 0.3s;"></span>
                    </span>
                </button>

                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-lg-auto">
                        <li class="nav-item"><a class="nav-link click-scroll" href="index.html#section_1">Home</a></li>
                        <li class="nav-item"><a class="nav-link click-scroll" href="index.html#section_2">About</a></li>
                        <li class="nav-item"><a class="nav-link click-scroll" href="index.html#section_3">Services</a></li>
                        <li class="nav-item"><a class="nav-link click-scroll" href="index.html#section_4">Gallery</a></li>
                        <li class="nav-item"><a class="nav-link click-scroll" href="index.html#section_5">Contact Us</a></li>
                    </ul>
                    <div class="d-none d-lg-block ms-lg-3">
                        <a class="btn navbar-get-quote btn-ripple" data-bs-toggle="offcanvas" href="#offcanvasExample"
                            role="button" aria-controls="offcanvasExample">Get Quote</a>
                    </div>
                </div>
            </div>
        </nav>"""

ROOT_DIR = r"c:\Users\hp\OneDrive\Desktop\j-h-main\j-h-main"

def update_navbar(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_search = '<nav'
    end_search = '</nav>'
    
    start_idx = content.find(start_search)
    end_idx = content.find(end_search, start_idx)
    
    if start_idx != -1 and end_idx != -1:
        end_idx += len(end_search)
        new_content = content[:start_idx] + ROOT_NAVBAR + content[end_idx:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated navbar in: {file_path}")
    else:
        print(f"Could not find navbar in: {file_path}")

def main():
    root_files = ['event-listing.html', 'event-detail.html']
    for filename in root_files:
        path = os.path.join(ROOT_DIR, filename)
        if os.path.exists(path):
            update_navbar(path)

if __name__ == "__main__":
    main()
