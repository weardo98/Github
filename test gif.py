from PIL import Image

im = Image.open('test2.gif')
transparency = im.info['transparency'] 
im.save('test1.png', transparency=transparency)

im.seek(im.tell()+1)
transparency = im.info['transparency'] 
im.save('test2.png', transparency=transparency)