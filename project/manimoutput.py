# manim -pql scene.py SquareToCircle
# what happens when we run this?

# -p tells manim to play scene once rendered and -ql tells manim to play in low quality

# Sections

def construct(self):
    # play the first animations...
    # you don't need a section in the very beginning as it gets created automatically
    self.next_section()
    # play more animations...
    self.next_section("this is an optional name that doesn't have to be unique")
    # play even more animations...
    self.next_section("this is a section without any animations, it will be removed")
    
def construct1(self):
    self.next_section()
    # this section doesn't have any animations and will be removed
    # but no error will be thrown
    # feel free to tend your flock of empty sections if you so desire
    self.add(Circle())
    self.next_section()

def construct(self):
    self.next_section()
    self.add(Circle())
    # now we wait 1sec and have an animation to satisfy the section
    self.wait()
    self.next_section()

# for videos to be created for each section 
# manim --save_sections scene.py

# JSON files can be used by third party applications

def construct(self):
    self.next_section(skip_animations=True)
    # play some animations that shall be skipped...
    self.next_section()
    # play some animations that won't get skipped...
    
"""
Flags

-a: render all
-q(l,m,h,k): rendering in different qualities
-p: play once rendered
-f: for opening file browser at location of animation instead of playing it
-i: outputing gifs instead of mp4 files, they will be in the same place as the mp4 files but with a different extension


"""