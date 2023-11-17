# AWS Solution Architect Professional 勉強メモ

## Firewall Manager
多数のアカウントとアプリケーションに対して、中央でAWS WAF ルールを設定、管理するセキュリティ管理サービス。  
Organizationの管理アカウント等でWAFルールを一元管理し、組織に所属するアカウントにWAFを適用できる。

<br>

## RDS
### Babelfish for Aurora PostgreSQL
SQL Server独自のSQL言語（T-SQLなど）を解釈できるAurora PostgreSQL。  
SQL ServerからPostgreSQLに移行する際、アプリケーション側でコード変更が発生する。  
（SQL部分）  
BabelfishはSQL Server独自のSQLをサポートしているので、アプリケーション側のコード変更が不要。

### IAMデータベース認証
データベースにユーザー名とパスワードでログインするのではなく、トークンを使ってログインする。  
DBユーザーに対するrds-db:connect権限を付与したIAMロールを接続元リソースに付与する。  
そして、DBユーザーでログインするためのトークンを作成し、DB接続コマンドでそのトークンを指定する。  
この認証方式はIAMのIDプロバイダーと統合されていないため、SAML認証で使用するIdPユーザーでRDSに接続することはできない。  
※IAM IDプロバイダーは、SAML認証で使うIdPの情報を登録するリソース。

<br>

## Aurora
### Aurora Serverless Data API
Aurora Serverlessへの接続エンドポイント。  
httpプロトコルでの通信で接続する。  
DBへの接続はエンドポイントを経由するので、Connections数が上限に達する問題を防ぐことができる。  
Data APIでは、DBの認証情報はSecret Managerで保持されてるものを利用してDBに接続する。

<br>

## Amazon TimeStream
フルマネージド・サーバーレスの時系列データベースサービス。  
timestampをキーに値を保持する。  
timestampがキーなので、時系列によるデータ検索、分析に向いている。  
一方で、データの更新と削除は対応していないので、一般的なアプリケーションのDBとしての用途には向いていない。  
コンピューティングリソースとストレージを自動で拡張し、使用分に応じて従量課金される。  
TimeStreamでは、データのライフサイクル設定があり、このサイクルを超えるとデータが削除される。  Timestreamのストレージは階層化されており、取り込まれたデータはまず高速なメモリ階層に置かれる。  
一定期間が経過するとやや低速な磁気ディスク階層に移動し、さらに一定期間が経過すると削除される。  
ライフサイクル期間は自由に設定可能で、磁気ディスク階層は最長200年も保持可能。

<br>

## AWS Backup
AWSサービスのバックアップを自動化・一元管理するサービス。  
　完全マネージドサービス  
　スケジュールバックアップ  
　バックアップアクティビティをログとして出力  

サポートしているサービス  
　EBS、EFS、RDS、EC2、FSx、DocumentDBなど

<br>

## S3
### S3アクセスポイント
S3 Bucketへのアクセス権限を管理するポリシーみたいなもの。  
Bucketへのアクセス権限を管理するものにバケットポリシーがあるが、
バケットポリシーに複数のポリシーを記載すると、バケットポリシーの中身が肥大化していく。  
肥大化すると管理しづらくなり、ポリシーを更新する際に事故が発生するリスクがある。（違うポリシーを更新してしまった、など）  
そこで、1つの接続可否は1つのアクセスポイントで管理することで、バケットポリシーの肥大化を防ぐことができる。  

### Apache Parquet形式でのデータ保存
列指向でデータを保存する。  
列指向にすることで、データの分析パフォーマンス（平均、合計だしたりなど）が上がる。  
（対象列のデータを効率よく取得できる）

### S3 RTC
S3 Replication Time Control (S3 RTC)機能を使うことで、S3レプリケーションをほぼ確実に15分以内で実行できる。  
通常のレプリケーションでは大体のS3オブジェクトのレプリケートは15分いないで完了するが、場合によっては数時間かかる場合がある。  
RTCを併用することで、99.99%のオブジェクトを15分以内にレプリケートできる。

<br>

## Amazon Macie
S3バケット上に、個人情報等の機密情報が記載されたファイルが存在しないかを検知するサービス。  
検知は機械学習を用いて行われる。  
対象となるのは、暗号化されていないバケット、パブリックアクセス可能なバケット、AWS Organizations で定義したもの以外の AWS アカウントと共有されているバケット。

<br>

## Cloudfront
### Lambda@Edgeを使った動的オリジン選択
リクエストの内容に応じて、接続先オリジンをLambda@Edgeでルーティングすることができる。  
　URLがfoo.example.com/hogeだったらオリジンAに接続  
　URLがfoo.example.com/booだったらオリジンBに接続  

<br>

## Athena
### パーティション
AthenaではS3バケットを年月でフォルダ分けすると、テーブルがパーティション化される。  
パーティション化することで、検索速度が向上し、データ取得のコストを削減できる。  
　検索対象のパーティションしか見に行かないため

パーティションの分け方にHive形式とHiveじゃない形式がある。
　Hive形式  
　　フォルダ名が以下のようになっているパーティション  
　　s3://log/year=2021/month=01/day=26/  
　Hiveじゃない形式  
　　フォルダ名が以下のようになっているパーティション  
　　s3://log/2021/01/26/

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

<br>

## AWS DataSync
オンプレ→AWS、AWS→オンプレへのデータ移行サービス。  
オンプレにエージェント（実体は仮想マシン）を導入し、エージェント経由でAWSサービスへデータを移行する。  
移行先AWSサービスはS3、EFS、FSxがサポートされている。

<br>

## Migration Evaluator
オンプレ→AWSへ移行する際、オンプレ環境を分析し、移行に掛かるコストを予測するサービス。  
Migration Hubとセットで使う。

<br>

## Migration Hub
オンプレ→AWSへの移行を一元管理するサービス。  
ダッシュボードで移行状況を可視化する。  
オンプレミスサーバーの詳細情報を特定・取得して移行計画を策定、移行中は移行状況を確認できる。

<br>

## AWS Application Discovery Service
オンプレ→AWSへの移行支援サービス。  
オンプレミスのリソース情報を収集し、インフラの検出や依存関係の識別、パフォーマンスの測定を行う。

<br>

## Cloud Endure
AWSのサーバー移行サービスの1つ。  
Server Migration ServiceやVM Importよりも高速にオンプレのサーバーをAWSに移行できる。  
　データを圧縮してAWSに送信

AWS上にレプリケーションインスタンスを構築し、このインスタンスを経由して、オンプレ→ターゲットインスタンスへデータが移行される。  
　オンプレサーバーにはエージェントをインストールする必要がある。

<br>

## ECR
### クロスリージョンレプリケーション
ECRのプライベートレジストリを別リージョンにレプリケーションできる。  
デフォルトではレジストリ内の全リポジトリを複製するが、対象のリポジトリを絞って複製することも可能。  

<br>

## Data LifeCycle Manager
EBSスナップショットの作成、保存、削除を自動化するサービス。  
スナップショットの作成をスケジュール実行できる。  
また、一定期間の保持期間がが過ぎたスナップショットを自動削除できる。  

<br>

## VPC
### VPCエンドポイント
#### S3 インターフェースエンドポイント
インターフェース型エンドポイント。  
VPC内に作成され、ENIが割り当てられる。  
また、プライベートIPが割り当てられるので、このIPを使ってS3へアクセスする。  
（ゲートウェイ型はパブリックIPであり、ここが両者の違いの1つである）

### VPC PrivateLink
AWS上で動くサードパーティサービスと、サービス利用側VPCとの間にセキュアな接続を提供するリソース。  
サービスではなく、以下のコンポーネントで構成される。  
　VPCエンドポイント  
　VPCエンドポイントサービス  
　　サービス提供側はロードバランサーで構成されている必要がある。  
　　（エンドポイントサービス作成時にロードバランサーとの紐づけ設定がされる）

### サブネットのCIDR変更
既存サブネットのCIDRを変更することはできない。  

### プレフィックスリスト
CIDRのリスト。  
プレフィックスリストはセキュリティグループで使うことができる。  
複数のCIDRに特定ポートの接続ルールを作成する際、リストを使わない場合、そのCIDRの数だけルールを作らないといけない。  
が、リストを使えば、作るルールが1つだけで済む。  
（リストに対するポート接続ルールを作るだけでよい）

<br>

## Direct Connectの暗号化通信
Direct Connectの通信は暗号化されていない。
通信を暗号化する手段の1つとして、Site to Site VPNとの併用がある。  
　Site to Site VPNのAWS側エンドポイントはパブリックIPを使用する。  
　→パブリックVIFでVPN接続先VPCのVGWを接続する必要がある。

## Cost Categories
AWSの料金を何らかのカテゴリで分割表示するサービス。  
カテゴリの種類として以下がある。  
　AWSアカウント（管理部門、開発部門など）、タグ、サービス、料金タイプなど

<br>

## Direct Connect
### パブリック仮想インターフェイス
オンプレ側からAWSのパブリックサービス（S3など）にアクセスする際に使用する。  

### プライベート仮想インターフェイス
オンプレ側からVPC内のリソースへのアクセスに使用する。  

## Direct Connectゲートウェイ
1つのVIFに複数のVGWを紐づけるAWSリソース。  
これを使えば、1つのVIFで複数のリージョンにアクセスすることができる。  
ただし、以下の制約がある。  
　Direct Connect Gatewayを介したVPC(VGW)同士の通信は不可  
　Direct Connect Gatewayを介したVIF同士の通信は不可  
　異なるAWSアカウントのVIFおよびVGWの接続は不可


### トランジット仮想インターフェイス
トランジットゲートウェイとDirect Connectを紐づける。  
このインターフェイスはDirect Connectゲートウェイに紐づける必要がある。

## CodeBuild
### EFSをビルド実行環境にマウント可能
CodeBuildのプロジェクト設定でビルド環境にマウントするEFSファイルシステムを設定できる。  
　CodeBuildはファイルシステムと同じVPCとプライベートサブネットに配置する必要がある。

<br>

## Amazon PinPoint
ユーザーの動向を分析し、そのユーザーをセグメントに分け、対象のユーザーに向けて個別通知するサービス。  
通知はメール、SNS、SMS等で送信可能。  
また、送信したメールの分析もする（開封率など）。  

<br>

## Savings Plan
EC2やLambda、Fargateといったコンピューティングリソースを、一定期間・１時間に何ドル分使うという契約をするサービス。  
料金は一括支払いになるが、その分割引してくれる。  
　Lambdaは17%の割引になる

<br>

## Lambda
### 502エラーが返されたとき
API Gateway + Lambdaの構成で、Lambdaから502エラーが返されたとき、以下のケースが考えられる。  
　レスポンスの形式が正しくない。  
　　statusCodeとbodyがレスポンスに含まれているか  
　　body部のJSONが正しい形になっているか  
　コードエラーで強制終了。  

<br>

## AWS Batch
大規模バッチ処理を実行する環境をフルマネージドで提供するサービス。  
内部では、コンテナイメージから作られたコンテナが動いている。   
コンテナ実行環境：ECS or EKS。  
ジョブ定義  
　使用するコンテナイメージやコンテナが使用するvCPUやメモリ量等、実行に関する設定を定義したもの


<br>


## Compute Optimizer
ユーザー環境を機械学習を使って分析し、最適なコンピューティングリソースを提案するサービス。  
リソースの提案は最大3つまで提示してくれる。  
また、メモリ等の使用率も予測してくれる。  
対象サービスはEC2、EC2 Auto Scaling、EBS、Lambda。

## API Gateway
### Cloudfrontとの組み合わせ
API Gatewayには内部的にCloudfrontを使っている機能がある。  
（エッジ最適化エンドポイント、キャッシュ）  

キャッシュをより細かく制御したいケースで、API Gatewayの機能で実現できない場合、
APIの前段にCloudfrontを置く必要がある。  

<br>

## FSx For Windows Server
### HDD→SSDの変更
既存のFSx For Windows Serverのストレージタイプは変更できない。  
既存のサーバーをHDD→SSDに変更するには、新規にFSx For Windows ServerをSSDで作成し、そっちにデータをレプリケートする必要がある。

<br>

## IAM
### IAM Access Analyzer
リソースアクセス制限をするポリシーを分析し、外部からのアクセス設定がされていないかを検出するサービス。  
アクセス可能なエンティティ（AWSアカウント、Organizationに所属するアカウントなど）を信頼ゾーンとして定義し、その信頼ゾーン外からのアクセスを外部とみなす。

<br>

## IoT Greengrass
AWS の「IoT プラットフォーム」(AWS IoT) の機能をエッジ(現場)内の環境に提供するサービス。  
AWS上で実行するAWS IoTを現場のネットワーク内で実行できる。    
何らかの事情でクラウドにIoTデバイスのデータをアップロードできない問題を解決できる。

<br>

## Image Builder
AMIの作成を自動化するサービス。  
予めAMIを用意しておいて、それを複製させることでインスタンスを効率よくデプロイできる。  
（このイメージをゴールデンイメージと呼ぶ）  

が、ソフトウェアのアップデート等の理由で、そのたびにイメージを作り直す必要がある。    
Image Builderは、パイプラインを使ってAMIを自動ビルドするサービスである。  
　作成元ソースを指定し、そいつにソフトウェア等をインストールし、イメージをビルドする。  

また、Image BuilderはAMIの作成をスケジュールすることもできる。  
Image Builderは以下のリソースで構成される。  

### Build Components
ソフトウェアパッケージをダウンロード、インストール、および構成するための一連の手順を定義するオーケストレーションドキュメント。  
ドキュメントはyaml形式。  

### Recipes
ソースイメージと、ソースイメージに適用して出力イメージに必要な構成を生成するBuild Componentsを定義するドキュメント。

### Image pipelines
Recipeから実際にAMIを取得するパイプラインを定義したもの。  
　ビルドインスタンスの指定もここで行う。

<br>

## Identity Center
AWS Single Sign-onの後継サービスであり、AWS Organizationsで複数アカウントを運用している環境で各ユーザを集約管理し、各アカウントへのシングルサインオンを提供。  
管理アカウントで各アカウントへ接続する際に使用するIAMロールとIAMユーザーを紐づけることで、利用者は1つのIAMユーザーで各AWSアカウント環境にログインできる。

<br>

## Control Tower
### 必須ガードレール
Control Towerにデフォルトで有効化されている。  
（CloudTrailやAWS COnfigが有効化されているか、など）

EBSの暗号化は必須ガードレールでは検証対象外であり、こっちは強く推奨ガードレールが検証対象としている。  
→これもチェックしたい場合、このガードレールも有効化する。

<br>

## AWS Organizations
### OrganizationAccountAccessRole
AWS Organizationsでアカウントを作成すると、そのアカウント内にOrganizationAccountAccessRoleという名前のロールが作成される。  
このロールはAdministrator権限が付与されており、大体何でもできる。  
用途としては、マスターアカウント内のIAMユーザーにこのロールを引き受ける権限を付与しておき、このIAMユーザーで対象アカウントにスイッチロールしてログインし、何らかの操作をする（IAMユーザーの作成など）、など。  
　ID、パスワードを入力せずにアカウント切り替えできるのがメリットか。