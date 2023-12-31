# AWS Solution Architect Professional 勉強メモ

## 目次

- [AWS Solution Architect Professional 勉強メモ](#aws-solution-architect-professional-勉強メモ)
  - [目次](#目次)
  - [Firewall Manager](#firewall-manager)
  - [RDS](#rds)
    - [Babelfish for Aurora PostgreSQL](#babelfish-for-aurora-postgresql)
    - [IAMデータベース認証](#iamデータベース認証)
    - [RDSリードレプリカの負荷分散方法](#rdsリードレプリカの負荷分散方法)
    - [マルチリージョン構成のRDSのフェイルオーバー戦略](#マルチリージョン構成のrdsのフェイルオーバー戦略)
  - [Aurora](#aurora)
    - [Aurora Serverless Data API](#aurora-serverless-data-api)
    - [Aurora Global Database](#aurora-global-database)
  - [Amazon TimeStream](#amazon-timestream)
  - [AWS Backup](#aws-backup)
  - [S3](#s3)
    - [IgnorePublicAcls](#ignorepublicacls)
    - [bucket-owner-full-control](#bucket-owner-full-control)
    - [S3アクセスポイント](#s3アクセスポイント)
    - [Apache Parquet形式でのデータ保存](#apache-parquet形式でのデータ保存)
    - [クロスリージョンレプリケーションの前提条件](#クロスリージョンレプリケーションの前提条件)
    - [S3 RTC](#s3-rtc)
  - [Amazon Macie](#amazon-macie)
  - [Cloudfront](#cloudfront)
    - [Lambda@Edgeを使った動的オリジン選択](#lambdaedgeを使った動的オリジン選択)
    - [静的コンテンツと動的コンテンツの振り分け](#静的コンテンツと動的コンテンツの振り分け)
  - [Athena](#athena)
    - [パーティション](#パーティション)
  - [Storage Gateway](#storage-gateway)
    - [ファイルゲートウェイ](#ファイルゲートウェイ)
      - [S3 ファイルゲートウェイ](#s3-ファイルゲートウェイ)
      - [FSx ファイルゲートウェイ](#fsx-ファイルゲートウェイ)
    - [ボリュームゲートウェイ](#ボリュームゲートウェイ)
      - [キャッシュ型ボリュームゲートウェイ](#キャッシュ型ボリュームゲートウェイ)
      - [保管型ボリュームゲートウェイ](#保管型ボリュームゲートウェイ)
    - [テープゲートウェイ](#テープゲートウェイ)
  - [AWS DataSync](#aws-datasync)
  - [Migration Evaluator](#migration-evaluator)
  - [Migration Hub](#migration-hub)
  - [AWS Application Discovery Service](#aws-application-discovery-service)
  - [Cloud Endure](#cloud-endure)
  - [System Manager](#system-manager)
    - [Session Managerを使ったWindows EC2へのRDP](#session-managerを使ったwindows-ec2へのrdp)
  - [ECS](#ecs)
    - [deployment circuit breaker](#deployment-circuit-breaker)
  - [ECR](#ecr)
    - [クロスリージョンレプリケーション](#クロスリージョンレプリケーション)
  - [Data LifeCycle Manager](#data-lifecycle-manager)
  - [VPC](#vpc)
    - [VPCエンドポイント](#vpcエンドポイント)
      - [S3 インターフェースエンドポイント](#s3-インターフェースエンドポイント)
    - [VPC PrivateLink](#vpc-privatelink)
    - [サブネットのCIDR変更](#サブネットのcidr変更)
    - [プレフィックスリスト](#プレフィックスリスト)
  - [Direct Connectの暗号化通信](#direct-connectの暗号化通信)
  - [Cost Categories](#cost-categories)
  - [Direct Connect](#direct-connect)
    - [パブリック仮想インターフェイス](#パブリック仮想インターフェイス)
    - [プライベート仮想インターフェイス](#プライベート仮想インターフェイス)
  - [Direct Connectゲートウェイ](#direct-connectゲートウェイ)
    - [トランジット仮想インターフェイス](#トランジット仮想インターフェイス)
  - [Transit Gateway](#transit-gateway)
  - [CodeBuild](#codebuild)
    - [EFSをビルド実行環境にマウント可能](#efsをビルド実行環境にマウント可能)
  - [Amazon PinPoint](#amazon-pinpoint)
  - [Savings Plan](#savings-plan)
  - [Lambda](#lambda)
    - [502エラーが返されたとき](#502エラーが返されたとき)
  - [Step Functions](#step-functions)
    - [同一ステートマシンを複数回同時実行](#同一ステートマシンを複数回同時実行)
  - [AWS Batch](#aws-batch)
  - [EC2](#ec2)
    - [属性ベースのインスタンスタイプ自動選定（Auto Scaling）](#属性ベースのインスタンスタイプ自動選定auto-scaling)
  - [Compute Optimizer](#compute-optimizer)
  - [API Gateway](#api-gateway)
    - [Cloudfrontとの組み合わせ](#cloudfrontとの組み合わせ)
  - [FSx For Windows Server](#fsx-for-windows-server)
    - [HDD→SSDの変更](#hddssdの変更)
  - [IAM](#iam)
    - [IAM Access Analyzer](#iam-access-analyzer)
  - [IoT Greengrass](#iot-greengrass)
  - [Image Builder](#image-builder)
    - [Build Components](#build-components)
    - [Recipes](#recipes)
    - [Image pipelines](#image-pipelines)
  - [Cloudwatch](#cloudwatch)
    - [Cloudwatch Synthetics](#cloudwatch-synthetics)
      - [CloudWatch Synthetics Canary](#cloudwatch-synthetics-canary)
  - [Identity Center](#identity-center)
  - [Control Tower](#control-tower)
    - [必須ガードレール](#必須ガードレール)
  - [AWS Organizations](#aws-organizations)
    - [OrganizationAccountAccessRole](#organizationaccountaccessrole)
  - [タグポリシー](#タグポリシー)
  - [AWS Managed Microsoft AD](#aws-managed-microsoft-ad)
  - [Simple AD](#simple-ad)
  - [AD Connector](#ad-connector)

<br>

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

### RDSリードレプリカの負荷分散方法
複数のリードレプリカに負荷を分散させる方法として、Route53の加重レコードセットを使う方法がある。  
リードレプリカがあるVPC内にRoute53プライベートホストゾーンを作成し、このホストゾーンに加重レコードセットをCNAMEで作成する。  
　サブドメイン名とリードレプリカのエンドポイントURLを紐づける  

アプリケーション側でRoute53に登録したエンドポイントでアクセスするようにすることで、複数のリードレプリカに負荷分散されるようになる。  
レコードセットはリードレプリカの数だけ作成する。  
また、レコードセットはRoute53ヘルスチェックを併用するのがベスト。

### マルチリージョン構成のRDSのフェイルオーバー戦略
最速でフェイルオーバーしたいならば、Aurora Global Databaseを使用する。  
こっちはコンソール上でプライマリのフェイルオーバーができる。  
クロスリージョンリードレプリカ構成のRDSでもフェイルオーバーは出来なくはないが、Aurora Global Databaseよりやることが多い。  
　クロスリージョンリードレプリカの昇格（スタンドアロンRDSになる）  
　昇格したプライマリRDSから障害が起きたリージョンへリードレプリカを展開  
　　昇格した時点でスタンドアロン構成になるので（元のRDSとの同期がされなくなる）、別途リードレプリカを展開する必要がある。  

<br>

## Aurora
### Aurora Serverless Data API
Aurora Serverlessへの接続エンドポイント。  
httpプロトコルでの通信で接続する。  
DBへの接続はエンドポイントを経由するので、Connections数が上限に達する問題を防ぐことができる。  
Data APIでは、DBの認証情報はSecret Managerで保持されてるものを利用してDBに接続する。

### Aurora Global Database
複数リージョンにAuroraクラスターを展開する。  
プライマリリージョン以外のリージョンは読み取り専用クラスターが展開される。  
また、プライマリに障害が発生した時のフェイルオーバーは数クリックで実行できる。  

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
### IgnorePublicAcls
その名の通り、パブリックACLの設定を無視して、バケットポリシーにしたがってリクエストユーザーのアクセス可否を判定する。  
※パブリックACL：特定のオブジェクトやバケットに対して一般のユーザー、つまり一般の公開（パブリック）されたユーザーに対して許可を与えるためのACL

### bucket-owner-full-control
バケットにオブジェクトをアップロードする際、明示的にバケット所有者にオブジェクトのアクセス権を付与するオプション。  
別アカウントからS3バケットにオブジェクトがアップロードされると、そのオブジェクトの所有者はアップロードしたアカウントになる。  
なので、明示的にアクセス権を付与しなければ、バケット所有者はそのオブジェクトにアクセスできない。  
ちなみに、バケット設定でアップロードするオブジェクトの所有者設定をバケット所有者にすることで、そのバケットにアップロードされるオブジェクトの所有者はバケット所有者となる。  
　この設定を使う際、バケットポリシーで bucket-owner-full-control の指定を必須にする必要がある。

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

### クロスリージョンレプリケーションの前提条件
クロスリージョンレプリケーションを行うS3バケットはバージョニングが有効化されている必要がある。

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

### 静的コンテンツと動的コンテンツの振り分け
ビヘイビア機能を使うことで、パスに応じて静的コンテンツがあるオリジンと、動的コンテンツがあるオリジンにリクエストをルーティングできる。  
　jpgファイルのリクエストは、オリジンA  
　動的コンテンツのリクエストは、オリジンB

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

## System Manager
### Session Managerを使ったWindows EC2へのRDP
Session Managerのポートフォワーディングを使うことで、ローカル端末からWindows EC2へリモートデスクトップ接続できる。  
　AWS CLIのSession Managerコマンドを実行して、ローカルポートと対象EC2との接続を確立する。  
　　直接ローカルPCとEC2がつながっているわけではなく、間にSession Managerがおり、これが接続を中継している。  

なお、現在はSystem Manager Fleet Managerがあり、そちらはマネージメントコンソール上でEC2にRDPすることができる。  
　vSphereのWeb Client的なやつ。  
　これも内部的にはSession Managerのポートフォワーディングを使っている。

<br>

## ECS
### deployment circuit breaker
ECSサービスのデプロイで異常が発生した場合に、以前にデプロイが成功していたバージョンに自動でロールバックする機能。  
rolling updateデプロイタイプでサポート。  
もともとrolling updateのデプロイには失敗というステータスが無かったので、デプロイに異常があった場合にECSサービスがタスクの起動を繰り返すという問題があった。  
　CFnでECSを監視している場合、永遠にUPDATE_IN_PROGRESSの状態になり、デプロイが終わらないという最悪の事態になることも。  
circuit breakerでは2つのステージでタスクのデプロイを評価する。  
　ステージ1  
　　Running状態に遷移せずに、タスクの起動回数が閾値を超えたら失敗と判定   
　　閾値の範囲内でRunning状態になれば成功と判定  
　ステージ2
　　ヘルスチェックの失敗によりリプレースされたタスクの数が閾値以上の数になったら失敗と判定  
　　閾値の範囲内でタスクのヘルスチェックが通れば成功と判定

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
Direct Connectで複数のVPCに接続するには、VPC分のVIFが必要だが、こっちは1つのVIFで複数のVPCに紐づけることができる。  
　オンプレ→複数のVPCに接続することができる。

ただし、以下の制約がある。  
　Direct Connect Gatewayを介したVPC(VGW)同士の通信は不可  
　Direct Connect Gatewayを介したVIF同士の通信は不可  
　異なるAWSアカウントのVIFおよびVGWの接続は不可  
　接続するVPCの上限は20個


### トランジット仮想インターフェイス
トランジットゲートウェイとDirect Connectを紐づける。  
このインターフェイスはDirect Connectゲートウェイに紐づける必要がある。
Direct Connectゲートウェイ同様、この構成もオンプレから複数のVPCに接続できるが、Direct Connectゲートウェイでは出来ないVPC間の接続もサポートしている。  
（VPC間の接続はTransit Gatewayの機能である）

<br>

## Transit Gateway
複数のVPC間の通信を確立するサービス。  
中央ハブ的な役割を果たす。  
ユースケースとしては、  
　相互に接続する必要があるVPCの数が多い。  
　　Transit Gatewayを使えば構成はスッキリする。  

Transit Gatewayと他ネットワークリソース（VPC、Direct Connectゲートウェイなど）との非紐づけはTransit Gateway Attachmentで行う。  
各AttachmentにはTransit Gateway Route Tableが紐づいており、このテーブルでルーティングを制御する。  
VPCを関連付けている場合、VPC側のルートテーブルには、接続先IPのCIDRがTransit Gatewayに転送されるルールを追加する。  
（自動的にルールが追加されないっぽい）

<br>


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
　Lambdaの同時実行数の上限に達した  

<br>

## Step Functions
### 同一ステートマシンを複数回同時実行
これができるのはエクスプレスワークフロー。  
スタンダードは、1ステートマシンの同時実行回数は1回。

<br>

## AWS Batch
大規模バッチ処理を実行する環境をフルマネージドで提供するサービス。  
内部では、コンテナイメージから作られたコンテナが動いている。   
コンテナ実行環境：ECS or EKS。  
ジョブ定義  
　使用するコンテナイメージやコンテナが使用するvCPUやメモリ量等、実行に関する設定を定義したもの


<br>

## EC2
### 属性ベースのインスタンスタイプ自動選定（Auto Scaling）
Auto Scalingでは、スポットインスタンスを利用する場合、どのインスタンスタイプを使うかを起動テンプレートで設定する。  
インスタンスタイプの選択は、複数のインスタンスタイプを選ぶのがベストプラクティスである。  
（インスタンスタイプに空きが無くなってインスタンスが起動できなくなるのを防ぐため）  
属性ベースでのインスタンスタイプでは、CPU数やメモリサイズを定義し、それに該当するインスタンスタイプをAWS側で自動選定してくれる。  
→インスタンスタイプの多様化を実現  


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

## Cloudwatch
### Cloudwatch Synthetics
WebアプリケーションやAPIを監視するサービス。  
実際にこれらにアクセスし、サービスが正常に応答できているかどうか等を確認する。  
設定したしきい値に基づいてエラーがあればアラート（Cloudwatchアラーム）を上げる。  
裏ではLambdaが動いており、Lambda上でWebアプリやAPIへのアクセス等を行っている。  
（いわゆるヘッドレスブラウザでWebアプリやAPIへアクセスしている）

#### CloudWatch Synthetics Canary
Cloudwatch Syntheticsを定義するもの。   
ここでアクセス対象のWebアプリやAPIのエンドポイントを設定する。   
　URL  
　HTTPメソッドなど  

また、対象へのアクセス間隔をスケジュール設定可能。  
　5分に1回アクセスなど  

Canaryは以下の方法で定義できる。  
　予め用意されたテンプレートを使う  
　コード書いてカスタムで定義  
　S3にスクリプトを配置して、それをインポート  

Syntheticsで動かすLambdaのランタイム環境は以下。  
　Node.js  
　Python

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

## タグポリシー
AWSリソースに対するタグの使用を管理するためのルールや制約のセット。  
例えば以下のようなルールを定義し、Organization内のアカウントにこのポリシーを適用することができる。  
　特定のプロジェクトに属するリソースには必ず"Project"というキーのタグが含まれるように強制する  
　特定の環境に属するリソースには"Environment"というキーのタグが含まれるようにする  
　"Environment"というキーの値はProd,Stg,Devのみ入力可能

組織全体や各OUごと、個々のアカウントにポリシーを適用できる。  
　各OU固有のポリシーを定義し、それらを各OUに割り当てる、など

<br>

## AWS Managed Microsoft AD
「Microsoft Active Directory」をマネージドサービスとして提供するサービス。  
AWS上のサービスをドメイン参加させることで、これらのサービスにADユーザーとして接続できるようになる。  
　RDS/AuroraやAmazon FSx for Windows FIle Serverなど  

もちろん、マネジメントコンソールへADユーザーでログイン可能。

オンプレのADと信頼関係を確立させることで、オンプレのADと連携ができる。  
　オンプレADユーザーでAWS上のリソースにアクセス  
　マネジメントコンソールへのログインにオンプレADユーザーでログイン

制限事項として、  
　オンプレミスADなど既存のドメインに対して、AWS MS ADを「追加のドメインコントローラー」として追加できない  
　AWS MS ADで構築したドメインに対して、オンプレミスAD等のドメインコントローラーを追加できない

<br>

## Simple AD
Microsoft Active Directoryと互換性のある「Sambda」を使ったマネージドサービス。  
ユーザーやコンピューターの管理、ログイン認証などの基本的な機能はActive Directoryと同様に利用できるが、Active Directoryで利用可能な多様な機能に対してSimple ADで使える機能は限定されている。  
Simple ADは、Active Directoryが持つ機能のうち、以下の機能をサポートしていない。  
　他のドメインとの信頼関係  
　LDAPスキーマ拡張  
　Active Directory「ごみ箱」機能  
　グループ管理サービスアカウント (gMSA)  
　RADIUSサーバーを使った多要素認証 (MFA)  
　以下のツールを使った管理  
　　PowerShell  
　　Windows Server 2008 R2以降で提供されている「Active Directory管理センター」  

以上の機能制限を踏まえると、Simple ADは、オンプレミスADなどと連係しない独立したActive Directoryドメインとして導入する構成が唯一の選択肢となる。  

また、AWS Managed Microsoft ADに比べて連携可能なAWSサービスが少ない。  
AWS Managed Microsoft ADが対応していて、Simple ADが対応していないサービスは以下。  
　Amazon FSx for Windows File Server
　Amazon RDS/Aurora  
　Amazon Chime
　AWS Single Sign-On (SSO)  
　AWS Transfer Family

<br>

## AD Connector
AWS環境からオンプレ環境にあるドメインコントローラーに対する通信を中継するためのプロキシサービス。  
これを使うと以下のことができる。  
　オンプレADの認証情報を使って、WorkSpaces、WorkDocs、WorkMailといったAWSのサービスにサインイン。  
　Amazon EC2 launch wizardまたはEC2 Simple System Manager（SSM） API経由でのプログラムによるActive Directoryドメインへの参加  
　Active DirectoryのアイデンティティとIAMロールとのマッピングによるAWS Management Consoleへのフェデレーションによるサインイン  
　　AD Connector側でIAMロールとユーザーorグループをマッピングする

AD ConnectorはRDS/Auroraに対応していない。  
→このサービスとADを連携させたい場合はAWS Managed Microsoft ADを利用。  

AD Connectorはあくまで中継するだけで、認証情報はAWS側でキャッシュされない。  
AD Connectorは特定のVPC内に作成される。  
　AD Connectorは複数のサブネットに配置される必要がある。  

作成時に、対象のオンプレADに関する情報を入れて、オンプレADとの関連付けをする。  
また、AD Connectorとオンプレ間で通信できるような仕組みを用意する必要がある（Direct Connect、AWS VPNなど）。
　言うまでもないが、インターネット経由でオンプレADと接続するのはセキュリティ面でバッドパターン。  
