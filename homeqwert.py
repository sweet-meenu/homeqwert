import cv2
import pytesseract
import google.generativeai as genai
import sys
import absl.logging

absl.logging.set_verbosity(absl.logging.ERROR)
genai.configure(api_key="AIzaSyCX2CUcDMd5CetpPzRCK9NPan88HvkjBgM")

def preprocess_image(img):
    image = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    image = cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return image

def extract_math_expression(img):
    return pytesseract.image_to_string(img, config="--psm 6")

def solve_with_gemini(expr):
    prompt = f"Solve this expression: {expr}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run hello.py <image_path>")
        sys.exit(1)
    img = sys.argv[1]
    preprocessed_image = preprocess_image(img)
    math_Expr = extract_math_expression(preprocessed_image)

    if math_Expr.strip():
        print(f"[+] Extracted Expression:  {math_Expr}")
        solution = solve_with_gemini(math_Expr)
        print(f"Solution: {solution}")
    else:
        print("[-] No valid expression detected. Try again!")


if __name__ == "__main__":
    main()
