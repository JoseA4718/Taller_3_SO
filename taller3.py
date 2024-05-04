from PIL import Image, ImageFilter
import threading
import time

class ImageFilteringModule:
    def __init__(self, img_name):
        self.img_name = img_name
        self.image = Image.open(img_name)

    def apply_filter(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)

def run_filters(img_filtering_modules):
    for image_filter in img_filtering_modules:
        image_filter.apply_filter()

if __name__ == "__main__":
    start_time = time.time()  # Record start time
    filtered_pics = []
    threads = []
    for i in range(0, 10000):
        filtered_pics.append(ImageFilteringModule("image.png"))
    for i in range(0, 10):
        lower_limit = int(i * len(filtered_pics)/10)
        upper_limit = int(i * len(filtered_pics)/10 + len(filtered_pics)/10 - 1)
        threads.append(threading.Thread(target=run_filters, 
        args=([filtered_pics[lower_limit:upper_limit]])))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()  # Record end time
    print("Execution time:", end_time - start_time, "seconds")
