import matplotlib.pyplot as plt


def plot_image(image, label):
    image_to_display = -1 * image + 255
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image_to_display, cmap='gray')
    ax.set_title(f"label = {label}")
    fig.show()
