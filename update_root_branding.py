import os

# New Offcanvas HTML from index.html
NEW_OFFCANVAS = """        <!-- Offcanvas -->
        <div class="offcanvas offcanvas-end" data-bs-scroll="true" tabindex="-1" id="offcanvasExample"
            aria-labelledby="offcanvasExampleLabel">
            <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvasExampleLabel" style="color: #322e2f;">Get a Free Quote</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body d-flex flex-column">
                <form class="custom-form member-login-form" action="#" method="post" role="form">
                    <div class="member-login-form-body">
                        <div class="mb-4">
                            <label class="form-label mb-2" for="full-name-oc" style="color: #322e2f;">Full Name</label>
                            <input type="text" name="full-name" id="full-name-oc" class="form-control"
                                placeholder="Your Name" required>
                        </div>
                        <div class="mb-4">
                            <label class="form-label mb-2" for="email-oc" style="color: #322e2f;">Email</label>
                            <input type="email" name="email" id="email-oc" pattern="[^ @]*@[^ @]*" class="form-control"
                                placeholder="Your Email" required="">
                        </div>
                        <div class="mb-4">
                            <label class="form-label mb-2" for="phone-oc" style="color: #322e2f;">Phone</label>
                            <input type="tel" name="phone" id="phone-oc" class="form-control"
                                placeholder="Your Phone Number">
                        </div>
                        <div class="col-lg-8 col-md-8 col-10 mx-auto">
                            <button type="submit" class="form-control btn-ripple"
                                style="background-color: #6d16df; border-color: #6d16df; color: white;">Submit</button>
                        </div>
                    </div>
                </form>
                <div class="mt-auto mb-5">
                    <p><strong class="me-3" style="color: #322e2f;">Any Questions?</strong><a href="tel:+15619063823"
                            class="contact-link" style="color: #6d16df;">+1 (561) 906-3823</a></p>
                </div>
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
                <path fill="#dcb78a" fill-opacity="1"
                    d="M0,224L34.3,192C68.6,160,137,96,206,90.7C274.3,85,343,139,411,144C480,149,549,107,617,122.7C685.7,139,754,213,823,240C891.4,267,960,245,1029,224C1097.1,203,1166,181,1234,160C1302.9,139,1371,117,1406,106.7L1440,96L1440,320L1405.7,320C1371.4,320,1303,320,1234,320C1165.7,320,1097,320,1029,320C960,320,891,320,823,320C754.3,320,686,320,617,320C548.6,320,480,320,411,320C342.9,320,274,320,206,320C137.1,320,69,320,34,320L0,320Z">
                </path>
            </svg>
        </div>"""

ROOT_DIR = r"c:\Users\hp\OneDrive\Desktop\j-h-main\j-h-main"

def update_offcanvas(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_search = '<div class="offcanvas offcanvas-end"'
    end_search = '<!--' # Search for the comment after offcanvas if possible, or just the end div
    
    # Actually, let's find the main offcanvas block and replace it.
    start_idx = content.find(start_search)
    if start_idx == -1: return
    
    # Find the closing </div> of the offcanvas. 
    # It has a unique SVG at the end.
    svg_end = '</svg>'
    svg_idx = content.find(svg_end, start_idx)
    if svg_idx == -1: return
    
    # The div ends right after the next </div> after the SVG.
    div_end = content.find('</div>', svg_idx) + len('</div>')
    
    new_content = content[:start_idx] + NEW_OFFCANVAS + content[div_end:]
    
    # Also update title
    new_content = new_content.replace('Tiya Golf Club - Event Listing', 'J&H Painting - Event Listing')
    new_content.replace('Tiya Golf Club - Event Detail', 'J&H Painting - Event Detail')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated offcanvas and branding in: {file_path}")

def main():
    root_files = ['event-listing.html', 'event-detail.html']
    for filename in root_files:
        path = os.path.join(ROOT_DIR, filename)
        if os.path.exists(path):
            update_offcanvas(path)

if __name__ == "__main__":
    main()
