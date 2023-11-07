# # init
# cd functions
# if [ -d upload ];then\
#     rm -rf upload;\
# fi

# # prtimes
# python gen_env.py prtimes
# mkdir upload
# rsync -ahv --progress prtimes/ upload/ --exclude '__pycache__'
# cp ./config.py ./upload/
# cp ./etl.py ./upload/
# cp ./slack_notification.py ./upload/
# cd upload &&\
# gcloud functions deploy prtimes --gen2 --runtime=python310 --source=. --entry-point=prtimes --region=asia-northeast1 --trigger-topic=raw-datalake --env-vars-file .env.yaml --memory 1024;\
# rm -rf ./upload/
# cd ..

# 引数を受け取る
a=$1
b=$2

# 第３引数がある場合
if [[ -n "$3" ]]; then
  # 第３引数を処理する
  echo "第３引数 = $3"
else
  # 第３引数がない場合は、何もしない
fi