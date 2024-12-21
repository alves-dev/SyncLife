from datetime import datetime

from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.container import Docker
from diagrams.onprem.database import Mysql
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.queue import RabbitMQ
from diagrams.programming.framework import Quarkus, Spring
from diagrams.programming.language import Python, Csharp

all_formats = ["jpg", "png", "svg", "pdf", "dot"]
formats = ["pdf"]

date = datetime.now().strftime('%Y/%m')
date_name = datetime.now().strftime('%Y_%m_%d')

with Diagram(f'Sync Life - {date}', show=False, direction='TB', outformat=formats, filename=f'sync_life_{date_name}',
             graph_attr={'labelloc': 't', 'fontsize': '20'}):
    with Cluster('Data', graph_attr={'fontsize': '15'}):
        mysq = Mysql('Mysql')

    with Cluster('Health', graph_attr={'fontsize': '15'}):
        health = [
            Quarkus('Nutri Track'),
            Spring('Exercise Service')
        ]

    with Cluster('Orchestrator', graph_attr={'fontsize': '15'}):
        event_sync = Csharp('Event Sync')
        mosquitto = Custom('Mosquitto', 'images/mosquitto.png')
        rabbitmq = RabbitMQ('RabbitMQ')
        rabbitmq >> Edge() << event_sync >> Edge() << mosquitto

    with Cluster('View', graph_attr={'fontsize': '15'}):
        grafana = Grafana('Grafana')

    with Cluster('Legado/Depreciado', graph_attr={'fontsize': '15'}):
        ha_link = Python('HA Link Service')
        Quarkus('Food Service')

    with Cluster('Automation', graph_attr={'fontsize': '15'}):
        ha = Custom('Home Assistant', 'images/home-assistant.png')
        ha_mobile = Custom('HA Mobile', 'images/home-assistant-mobile.png')
        ha_mobile >> Edge() << ha

    with Cluster('Backup', graph_attr={'fontsize': '15'}):
        mysql_cron = Custom('Cron Backup', 'images/cron.png')
        rclone = Custom('Rclone', 'images/rclone.png')
        google_drive = Custom('Google drive', 'images/google-drive.png')
        volume = Docker("Volume Docker")
        mysql_cron >> volume
        volume << rclone >> google_drive

    with Cluster('Monitoring', graph_attr={'fontsize': '15'}):
        Docker('Glances')

    ha >> Edge() << mosquitto
    health >> Edge() << rabbitmq
    health >> Edge() << mysq
    grafana << mysq
    ha_link << ha
    ha_link >> rabbitmq
    mysql_cron >> mysq
