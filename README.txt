��������������
�޸� SwhyDataAnalytic.SwhyDataAnalytic.settings.py��
STATIC_ROOT = 'D:/Project/Python/SwhyDataAnalytic'Ϊ����·��/usr/local/SwhyDataAnalytic/static/

����޸�static�ļ���λ�ã���Ҫ�޸�vim /etc/nginx/nginx.conf�У�staticλ��

����nginx����
service nginx  start

uwsgi django_socket.ini

�˳�
screen
python manage.py runserver 0.0.0.0:8000
ctrl+a d
����
screen -r

ѹ����һ�汾
tar -zcvf /usr/local/SwhyDataAnalytic.tar.gz /usr/local/SwhyDataAnalytic

Restful�ӿڿ����꣬��������
makemigrations [appname] 
migrate

����migrations
migrate �C-fake XXX
makemigrations XXX


