import re

def generateLinkList(readme_content: str) -> str:
    # 見出しを抽出する正規表現
    pattern = re.compile(r'^(#{1,4})\s+(.*?)\s*\n', re.MULTILINE)

    # マッチングした見出しを取得
    matches = pattern.finditer(readme_content)
    
    #取得した見出しをループしてリンクリストを生成
    link_list = []
    for match in matches:
        level = len(match.group(1)) #見出しの階層
        heading = match.group(2) #見出しのタイトル
        if heading not in ["AWS Solution Architect Professional 勉強メモ", "目次"]:
            # リンクを生成
            link = f'{"  " * (level - 2)}- [{heading}](#{heading.lower().replace(" ", "-")})'
            # リンクをリストに追加
            link_list.append(link)
    
    #リンク一覧を生成
    result = '\n'.join(link_list)  # \nは改行を表現するエスケープシーケンス
    return result


def rewriteReadme(readme_path: str, readme_content: str, link_list: str):
    # 正規表現パターンを使用して目次の開始位置と終了位置を検索
    toc_start_match = re.search(r'^##\s*目次', readme_content, re.MULTILINE)
    toc_end_match = re.search(r'^##\s*', readme_content[toc_start_match.end():], re.MULTILINE)
    toc_start_index = toc_start_match.start()  #目次の開始位置
    toc_end_index = toc_start_match.end() + toc_end_match.start()  #目次の終了位置

    # 既存の目次部分を除いた新しいREADMEファイルの内容を作成
    new_readme_content = (
        readme_content[:toc_start_index]
        + '## 目次\n\n'
        + link_list
        + '\n\n<br>\n\n'
        + readme_content[toc_end_index:]
    )

    # 書き込んだ内容でREADMEファイルを上書き
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(new_readme_content)


def main():
    # Markdownファイルから内容を読み込む（ファイルのパスを適切に設定）
    file_path = './README.md'
    with open(file_path, 'r', encoding='utf-8') as file:
        readme_content = file.read()

    #リンク一覧を生成
    link_result = generateLinkList(readme_content)

    #READMEファイルを上書き
    rewriteReadme(file_path, readme_content, link_result)
    

if __name__ == "__main__":
    main()
