import cv2
import numpy as np

def adjust_colors(img, lower_bound, upper_bound):
    # Convert image to HSV (Hue, Saturation, Value) color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Create a mask for the NFL logos/end zones with specific color range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    # Invert mask to change everything but the logos/end zones
    mask_inv = cv2.bitwise_not(mask)
    
    # Use the mask to remove logos/end zones
    img[mask == 255] = [0, 255, 0] 
    img[:, :, 1] = cv2.add(img[:, :, 1], 50, mask=mask_inv)  # Adjust green channel
    
    return img

def main():
    img = cv2.imread('AFC39.jpg')  
    
    # This is HARD, since the logos can vary game by game
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    
    # Filter out these colors and enhance green
    img = adjust_colors(img, lower_blue, upper_blue)
    img = adjust_colors(img, lower_red, upper_red)
    
    cv2.imwrite('processed_nfl_game.jpg', img)
    cv2.imshow('Processed Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()