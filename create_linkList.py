import re

def main():
    # Markdownファイルから内容を読み込む（ファイルのパスを適切に設定）
    file_path = './README.md'
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # 見出しを抽出する正規表現
    pattern = re.compile(r'^(#{1,3})\s+(.*?)\s*\n', re.MULTILINE)

    # マッチングした見出しを取得
    matches = pattern.finditer(markdown_content)
    
    #取得した見出しをループしてリンクリストを生成
    for match in matches:
        level = len(match.group(1)) #見出しの階層
        heading = match.group(1) #見出しのタイトル
        if heading not in ["AWS Solution Architect Professional 勉強メモ", "目次"]:
            link = '- [' + heading + '](#' + heading.lower().replace(' ', '-') + ')'
            print(link)


if __name__ == "__main__":
    main()
