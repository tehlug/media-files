import os
import subprocess

def convert_jpeg_to_webp(input_dir, output_dir, quality=80):
    os.makedirs(output_dir, exist_ok=True)

    jpeg_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg'))]
    
    if not jpeg_files:
        print(f"No JPEG files were found in the directory {input_dir}")
        return

    for jpeg_file in jpeg_files:
        input_path = os.path.join(input_dir, jpeg_file)
        output_file = os.path.splitext(jpeg_file)[0] + '.webp'
        output_path = os.path.join(output_dir, output_file)

        try:
            subprocess.run(
                ['cwebp', '-q', str(quality), input_path, '-o', output_path],
                check=True,
                capture_output=True,
                text=True
            )
            print(f"Converted: {input_path} -> {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert {input_path}: {e.stderr}")
        except FileNotFoundError:
            print("The 'cwebp' tool could not be found. Please install it first. (https://storage.googleapis.com/downloads.webmproject.org/releases/webp/index.html)")
            return

if __name__ == "__main__":
    input_directory = "279"
    output_directory = "279-c"
    convert_jpeg_to_webp(input_directory, output_directory, quality=80)