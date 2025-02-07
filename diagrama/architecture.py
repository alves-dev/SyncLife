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

date = datetime.now().strftime('%Y-%m-%d')
date_name = datetime.now().strftime('%Y_%m_%d')

with Diagram(f'Arquitetura - {date}', show=False, direction='TB', outformat=formats, filename=f'out_pdf/architecture_{date_name}',
             graph_attr={'labelloc': 't', 'fontsize': '20'}):

    with Cluster('Data', graph_attr={'fontsize': '15'}):
        # db_nutri_track = Mysql('Nutri DB')
        # db_body_track = Mysql('Body DB')
        # db_exercise = Mysql('Exercise DB')
        mysql = Mysql('Mysql')

    with Cluster('Health', graph_attr={'fontsize': '15'}):
        service_nutri_track = Quarkus('Nutri Track')
        service_body_track = Spring('Body Track')
        service_health = [
            service_nutri_track,
            service_body_track
        ]

    with Cluster('Orchestrator', graph_attr={'fontsize': '15'}):
        event_sync = Csharp('Event Sync')
        mosquitto = Custom('Mosquitto', '../images/mosquitto.png')
        rabbitmq = RabbitMQ('RabbitMQ')
        rabbitmq >> Edge() << event_sync >> Edge() << mosquitto

    with Cluster('View', graph_attr={'fontsize': '15'}):
        grafana = Grafana('Grafana')

    with Cluster('Legado/Depreciado', graph_attr={'fontsize': '15'}):
        ha_link = Python('HA Link Service')
        service_exercise = Spring('Exercise Service')

    with Cluster('Automation', graph_attr={'fontsize': '15'}):
        ha = Custom('Home Assistant', '../images/home-assistant.png')
        ha_mobile = Custom('HA Mobile', '../images/home-assistant-mobile.png')
        ha_mobile >> Edge() << ha

    with Cluster('Backup', graph_attr={'fontsize': '15'}):
        mysql_cron = Custom('Cron Backup', '../images/cron.png')
        rclone = Custom('Rclone', '../images/rclone.png')
        google_drive = Custom('Google drive', '../images/google-drive.png')
        volume = Docker("Volume Docker")
        mysql_cron >> volume
        volume << rclone >> google_drive

    with Cluster('Monitoring', graph_attr={'fontsize': '15'}):
        Docker('Glances')

    # services x database
    service_nutri_track >> Edge() << mysql
    service_body_track >> Edge() << mysql
    service_exercise >> Edge() << mysql
    grafana << mysql

    # services x rabbitMQ
    service_health >> Edge() << rabbitmq
    ha_link >> rabbitmq
    service_exercise << rabbitmq

    # Others
    ha >> Edge() << mosquitto
    ha_link << ha
    mysql_cron >> mysql
