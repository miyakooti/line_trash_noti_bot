# init
cd functions
if [ -d upload ];then\
    rm -rf upload;\
fi

# prtimes
python gen_env.py prtimes
mkdir upload
rsync -ahv --progress prtimes/ upload/ --exclude '__pycache__'
cp ./config.py ./upload/
cp ./etl.py ./upload/
cp ./slack_notification.py ./upload/
cd upload &&\
gcloud functions deploy prtimes --gen2 --runtime=python310 --source=. --entry-point=prtimes --region=asia-northeast1 --trigger-topic=raw-datalake --env-vars-file .env.yaml --memory 1024;\
rm -rf ./upload/
cd ..