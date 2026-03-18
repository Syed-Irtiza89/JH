import re

file_path = r'c:\Users\hp\OneDrive\Desktop\j-h-main\j-h-main\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the corruption and the surrounding gallery section
# We'll target the whole gallery block from the start of Row 1 to the end of Row 2
pattern = re.compile(r'<!-- Row 1: Left to Right -->.*?<!-- Row 2: Right to Left -->.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)

new_gallery = """<!-- Row 1: Left to Right -->
                        <div class="gallery-horizontal-row">
                            <div class="gallery-track-h left-to-right">
                                <div class="gallery-h-item"><img src="images/commercial-painting-alt.png" alt="Commercial">
                                    <div class="gallery-h-overlay"><span>Commercial Project</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/restaurant-finish-alt.png" alt="Restaurant">
                                    <div class="gallery-h-overlay"><span>Restaurant Finish</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/retail-finish-alt.png" alt="Retail">
                                    <div class="gallery-h-overlay"><span>Retail Space</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/interior-1.png" alt="Interior">
                                    <div class="gallery-h-overlay"><span>Interior Coating</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/commercial-3.jpeg" alt="Supermarket">
                                    <div class="gallery-h-overlay"><span>Supermarket Finish</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/Commercial-hero.jpg" alt="Build">
                                    <div class="gallery-h-overlay"><span>Commercial Build</span></div>
                                </div>
                                <!-- Duplicate for seamless loop -->
                                <div class="gallery-h-item"><img src="images/commercial-painting-alt.png" alt="Commercial">
                                    <div class="gallery-h-overlay"><span>Commercial Project</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/restaurant-finish-alt.png" alt="Restaurant">
                                    <div class="gallery-h-overlay"><span>Restaurant Finish</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/retail-finish-alt.png" alt="Retail">
                                    <div class="gallery-h-overlay"><span>Retail Space</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/interior-1.png" alt="Interior">
                                    <div class="gallery-h-overlay)<span>Interior Coating</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/commercial-3.jpeg" alt="Supermarket">
                                    <div class="gallery-h-overlay"><span>Supermarket Finish</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/Commercial-hero.jpg" alt="Build">
                                    <div class="gallery-h-overlay"><span>Commercial Build</span></div>
                                </div>
                            </div>
                        </div>

                        <!-- Row 2: Right to Left -->
                        <div class="gallery-horizontal-row">
                            <div class="gallery-track-h right-to-left">
                                <div class="gallery-h-item"><img src="images/nationwide-1.jpeg" alt="Premium">
                                    <div class="gallery-h-overlay"><span>Premium Finish</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/nationwide-2.jpeg" alt="Commercial">
                                    <div class="gallery-h-overlay"><span>Commercial Build</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/wallcovering-scope.png" alt="Wallcovering">
                                    <div class="gallery-h-overlay"><span>Wallcovering</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/ext-1.jpeg" alt="Exterior">
                                    <div class="gallery-h-overlay"><span>Exterior Work</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/interior-3.png" alt="Foyer">
                                    <div class="gallery-h-overlay"><span>Lobby Finish</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/interior-prep-roller.jpg" alt="Paint">
                                    <div class="gallery-h-overlay"><span>Professional Paint</span></div>
                                </div>
                                <!-- Duplicate for seamless loop -->
                                <div class="gallery-h-item"><img src="images/nationwide-1.jpeg" alt="Premium">
                                    <div class="gallery-h-overlay"><span>Premium Finish</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/nationwide-2.jpeg" alt="Commercial">
                                    <div class="gallery-h-overlay"><span>Commercial Build</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/wallcovering-scope.png" alt="Wallcovering">
                                    <div class="gallery-h-overlay"><span>Wallcovering</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/ext-1.jpeg" alt="Exterior">
                                    <div class="gallery-h-overlay"><span>Exterior Work</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/interior-3.png" alt="Foyer">
                                    <div class="gallery-h-overlay"><span>Lobby Finish</span></div>
                                </div>
                                <div class="gallery-h-item"><img src="images/interior-prep-roller.jpg" alt="Paint">
                                    <div class="gallery-h-overlay"><span>Professional Paint</span></div>
                                </div>
                            </div>
                        </div>"""

# Replace the block
fixed_content = pattern.sub(new_gallery, content)

# Also remove any lone strings of 00000000 just in case
fixed_content = re.sub(r'\\s*000000000.*\\(Used in Row 1 too\\)', '', fixed_content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(fixed_content)

print("File fixed successfully.")
