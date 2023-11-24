import re

def main():
    # Markdownファイルから内容を読み込む（ファイルのパスを適切に設定）
    file_path = './README.md'
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    pattern = re.compile(r'^#{1,3}\s+(.*?)\s*\n', re.MULTILINE)
    matches = pattern.finditer(markdown_content)
    
    for match in matches:
        heading = match.group()
        print(heading)


if __name__ == "__main__":
    main()
