from PIL import Image
import os
def image_to_pdf(image_list,output_pdf_name):

    if not image_list:
        print("No images provided")
        return
    
    images_objects=[]

    for img_path in image_list:
        try:
            if os.path.exists(img_path):
                img=Image.open(img_path).convert('RGB')
                images_objects.append(img)
        except Exception as e:
            print(f"Error: {e}")
        else:
            print(f"Warning: Image '{img_path}' not found. Skipping.")

    if not images_objects:
        print("Not valid images found to convert.")
        return

    base_image=images_objects[0]
    other_images=images_objects[1:]
    
    base_image.save(
        output_pdf_name,
        save_all=True,
        append_images=other_images
    )
    
    print(f"Success! created '{output_pdf_name}' with {len(images_objects)} pages.")
    
if __name__=="__main__":
    
    my_images=[
        'new.png',
        'new2.png'
    ]
    
    pdf="First.pdf"
    
    image_to_pdf(my_images,pdf)
    