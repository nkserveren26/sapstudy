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
以下の３種類がある。  
　ファイルゲートウェイ  
　ボリュームゲートウェイ  
　テープゲートウェイ  

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

## ECR
### クロスリージョンレプリケーション
ECRのプライベートレジストリを別リージョンにレプリケーションできる。  
デフォルトではレジストリ内の全リポジトリを複製するが、対象のリポジトリを絞って複製することも可能。  

## Data LifeCycle Manager
EBSスナップショットの作成、保存、削除を自動化するサービス。  
スナップショットの作成をスケジュール実行できる。  
また、一定期間の保持期間がが過ぎたスナップショットを自動削除できる。  

## VPC
### VPCエンドポイント
#### S3 インターフェースエンドポイント
インターフェース型エンドポイント。  
VPC内に作成され、ENIが割り当てられる。  
また、プライベートIPが割り当てられるので、このIPを使ってS3へアクセスする。  
（ゲートウェイ型はパブリックIPであり、ここが両者の違いの1つである）

## CodeBuild
### EFSをビルド実行環境にマウント可能
CodeBuildのプロジェクト設定でビルド環境にマウントするEFSファイルシステムを設定できる。  
　CodeBuildはファイルシステムと同じVPCとプライベートサブネットに配置する必要がある。

## Amazon PinPoint
ユーザーの動向を分析し、そのユーザーをセグメントに分け、対象のユーザーに向けて個別通知するサービス。  
通知はメール、SNS、SMS等で送信可能。  
また、送信したメールの分析もする（開封率など）。  

## Savings Plan
EC2やLambda、Fargateといったコンピューティングリソースを、一定期間・１時間に何ドル分使うという契約をするサービス。  
料金は一括支払いになるが、その分割引してくれる。  
　Lambdaは17%の割引になる

## Lambda
### 502エラーが返されたとき
API Gateway + Lambdaの構成で、Lambdaから502エラーが返されたとき、以下のケースが考えられる。  
　レスポンスの形式が正しくない。  
　　statusCodeとbodyがレスポンスに含まれているか  
　　body部のJSONが正しい形になっているか  
　コードエラーで強制終了。  