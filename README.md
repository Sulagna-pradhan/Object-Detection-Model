
---

# Object-Detection-Model

This repository contains an object detection model built using Python. The model uses a pre-trained DETR (Detection Transformer) from Hugging Face to detect and classify objects by images.

## Getting Started

### Prerequisites

Make sure you have Python installed. You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Installation

1. **Fork the repository**: Click on the 'Fork' button at the top right corner of this page to fork this repository.

2. **Clone the repository**: Clone your forked repository to your local machine using:

    ```bash
    git clone https://github.com/Sulagna-pradhan/Object-Detection-Model.git
    cd Object-Detection-Model
    ```

3. **Install dependencies**: Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Add images**: Place the images you want to test in the `img` folder.

2. **Set the path**: Update the image paths in the code (`ai.py`).

3. **Run the script**: Execute the script to run the object detection model:

    ```bash
    python ai.py
    ```

### Folder Structure

```
Object-Detection-Model/
│
├── img/               # Folder to store input images
├── ai.py              # Main script to run the object detection model
├── requirements.txt   # List of dependencies
├── .gitignore         # Git ignore file
└── README.md          # This README file
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or run into any issues. Happy coding!

---
