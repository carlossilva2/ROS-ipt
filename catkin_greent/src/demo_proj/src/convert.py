import Image
 
 
 
def processimage():
        im = Image.open('frame.jpg') # open the Image
        rgb_im = im.convert('RGB') #convert the image to RGB type
        width, height = rgb_im.size # get height and width of image
        pix=im.load()  # load all pixels of image in an list called "pix"
        #print width, height
        r,g,b=pix[0,0]  # get the rbg value of starting pixel        
        initialcolor=r+g+b # get color value of starting pixel
                 
        linedeteced=0  #variable used to detect a line
        linestartxvalue=0 # varaible used to store the x value of line
        lineendxvalue=0   # variable used to store the ending x value of line
                
        y=int (height/8)  # get the top y value of image, we don't to start from the very start of image
        # A for loop that goes through one itteration of x value at height y        
         
        for x in range (0,width):
             r,g,b= pix[x,y] # rbg value of pixel
             currentcolor=r+g+b # get color value of pixel
 
             # this the logic for detecting a change in color to indicate a line
             if (currentcolor > initialcolor +10 ) or (currentcolor < initialcolor -10):
                     linedetected=1
                     linestartxvalue=x
                     #print x , y   
                     break
        y=height - int(height/8)
         # A for loop that goes through one itteration of x value at height y 
        for x in range (0,width):
             r,g,b= pix[x,y]
             currentcolor=r+g+b
             # this the logic for detecting a change in color to indicate a line   
             if (currentcolor > initialcolor +10 ) or (currentcolor <initialcolor -10):
                     linedetected=1
                     lineendxvalue=x
                     #print x , y   
                     break
       # logic to see if line is turning left 
        if ( linestartxvalue > lineendxvalue +20):
               return "right"
       #logic to see if line is turning right 
        if ( linestartxvalue < lineendxvalue -20):
               return "left"
       #logic to see if line straight        
        if ( lineendxvalue + 9 > linestartxvalue > lineendxvalue - 10 ):
                return "straight"
