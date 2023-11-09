# AWS Solution Architect Professional 勉強メモ

## S3
### S3アクセスポイント
S3 Bucketへのアクセス権限を管理するポリシーみたいなもの。  
Bucketへのアクセス権限を管理するものにバケットポリシーがあるが、
バケットポリシーに複数のポリシーを記載すると、バケットポリシーの中身が肥大化していく。  
肥大化すると管理しづらくなり、ポリシーを更新する際に事故が発生するリスクがある。（違うポリシーを更新してしまった、など）  
そこで、1つの接続可否は1つのアクセスポイントで管理することで、バケットポリシーの肥大化を防ぐことができる。  

## Cloudfront
### Lambda@Edgeを使った動的オリジン選択
リクエストの内容に応じて、接続先オリジンをLambda@Edgeでルーティングすることができる。  
　URLがfoo.example.com/hogeだったらオリジンAに接続  
　URLがfoo.example.com/booだったらオリジンBに接続  

## Storage Gateway
オンプレミス環境のデータとAWS上のデータを橋渡しするサービス。

### ファイルゲートウェイ
オンプレミスのファイルをS3、FSx For Windows Serverにファイルを保管。  
S3から取得したファイルはオンプレ内のキャッシュストレージに保持しており、
一度取得したファイルはそこから取得するようになっている。  
そのため低レイテンシーでファイルアクセス可能。  
オンプレ→ファイルゲートウェイの通信はSMB、NFSプロトコルを使用。

#### S3 ファイルゲートウェイ
S3上にファイルを保管。

#### FSx ファイルゲートウェイ
FSx For Windows Server上にファイルを保管。

### ボリュームゲートウェイ
ブロックストレージとしてファイルをS3上に保管。  
（実体はEBSスナップショット）  
オンプレ→ボリュームゲートウェイへの通信はiSCSIプロトコルを使用する。   

キャッシュ型ボリュームゲートウェイと保管型ボリュームゲートウェイの2種類がある。  

#### キャッシュ型ボリュームゲートウェイ
S3がデータ保存先のプライマリーとなる。  
オンプレには頻繁にアクセスされるデータのみがキャッシュとして保持される。  
　キャッシュにファイルアクセスするので低レイテンシー

#### 保管型ボリュームゲートウェイ
オンプレがデータ保存先のプライマリーとなる。  
S3にもデータは保存されるが、保管のみの用途であり、こっちにデータアクセスは発生しない。  

### テープゲートウェイ
オンプレミスで管理している物理テープをS3上に保管する。  
S3に置いたテープデバイスへのアクセスはStorage Gateway APIを使用する。