

def main():
    # Markdownファイルから内容を読み込む（ファイルのパスを適切に設定）
    file_path = './README.md'
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    print(markdown_content)


if __name__ == "__main__":
    main()
