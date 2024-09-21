import tkinter as tk
from tkinter import filedialog, font
from PIL import Image, ImageTk
import numpy as np
import os
import traceback

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

try:
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing.image import img_to_array
except ImportError as e:
    print(f"Error importing TensorFlow: {e}")
    input("Press Enter to exit...")
    exit(1)

class BoneFractureGUI:
    def __init__(self, master):
        self.master = master
        master.title("Bone Fracture Detector")
        master.geometry("500x600")
        master.configure(bg='#2E2E2E')
        
        try:
            self.model = load_model('v1_bone_fracture_model.keras')
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
        
        self.class_names = [
            'Avulsion fracture', 'Comminuted fracture', 'Fracture Dislocation',
            'Greenstick fracture', 'Hairline Fracture', 'Impacted fracture',
            'Longitudinal fracture', 'Oblique fracture', 'Pathological fracture',
            'Spiral Fracture'
        ]
        
        # Create GUI elements
        self.title_label = tk.Label(master, text="Bone Fracture Detector", font=('Arial', 24, 'bold'), bg='#2E2E2E', fg='#FFFFFF')
        self.title_label.pack(pady=20)
        
        self.upload_button = tk.Button(master, text="Upload Image", command=self.upload_image, bg='#6082B6', fg='white', font=('Arial', 12))
        self.upload_button.pack(pady=10)
        
        self.image_label = tk.Label(master, bg='#2E2E2E')
        self.image_label.pack(pady=20)
        
        self.result_label = tk.Label(master, text="", font=('Arial', 14), bg='#2E2E2E', fg='#FFFFFF', wraplength=400)
        self.result_label.pack(pady=20)
    
    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if file_path:
            self.process_image(file_path)
    
    def process_image(self, file_path):
        try:
            image = Image.open(file_path)
            image = image.resize((256, 256))  # Resize to match model input size
            photo = ImageTk.PhotoImage(image)
            
            self.image_label.config(image=photo)
            self.image_label.image = photo
            
            # Prepare image for prediction
            img_array = img_to_array(image)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0  # Normalize pixel values
            
            # Make prediction
            prediction = self.model.predict(img_array)
            predicted_class = np.argmax(prediction)
            confidence = np.max(prediction)
            
            result_text = f"{self.class_names[predicted_class]}\nConfidence: {confidence:.2%}"
            self.result_label.config(text=result_text)
            
            # Change color based on confidence
            if confidence > 0.8:
                color = '#28a745'  # Green for high confidence
            elif confidence > 0.5:
                color = '#ffc107'  # Yellow for medium confidence
            else:
                color = '#dc3545'  # Red for low confidence

            self.result_label.config(fg=color)
        except Exception as e:
            print(f"Error processing image: {e}")
            self.result_label.config(text=f"Error: {str(e)}", fg='#dc3545')

def main():
    try:
        root = tk.Tk()
        gui = BoneFractureGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Traceback:")
        traceback.print_exc()
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()