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

with Diagram(f'Arquitetura - {date}', show=False, direction='TB', outformat=formats,
             filename=f'out_pdf/architecture_{date_name}',
             graph_attr={'labelloc': 't', 'fontsize': '20'}):

    with Cluster('internet', graph_attr={'fontsize': '15'}):
        google_drive = Custom('Google drive', '../images/google-drive.png')

        with Cluster('automation', graph_attr={'fontsize': '15'}):
            ha_mobile = Custom('HA Mobile', '../images/home-assistant-mobile.png')

    with Cluster('local-network', graph_attr={'fontsize': '15'}):
        core_dns = Custom("Core DNS", '../images/core.jpeg')
        proxy = Custom("swag", '../images/swag.jpeg')
        cloudflare = Custom("cloudflare tunnel", '../images/cloudflare.png')

        core_dns >> Edge() << proxy >> Edge() << cloudflare

        with Cluster('', graph_attr={'fontsize': '15'}):

            with Cluster('data', graph_attr={'fontsize': '15'}):
                mysql = Mysql('Mysql')
                mysql_cron = Custom('Cron Backup', '../images/cron.png')
                rclone_mysql = Custom('Rclone', '../images/rclone.png')
                volume_mysql = Docker("Volume Docker")
                mysql >> mysql_cron >> volume_mysql
                volume_mysql << rclone_mysql >> google_drive

            with Cluster('health', graph_attr={'fontsize': '15'}):
                service_nutri_track = Quarkus('Nutri Track')
                service_body_track = Spring('Body Track')
                service_exercise = Spring('Exercise Service')

                ha_link = Python('HA Link Service')

                health_rabbit = [
                    service_nutri_track,
                    service_body_track,
                    service_exercise
                ]

                health_mysql = [
                    service_nutri_track,
                    service_body_track,
                    service_exercise
                ]

            with Cluster('orchestration', graph_attr={'fontsize': '15'}):
                event_sync = Csharp('Event Sync')
                mosquitto = Custom('Mosquitto', '../images/mosquitto.png')
                rabbitmq = RabbitMQ('RabbitMQ')
                rabbitmq >> Edge() << event_sync >> Edge() << mosquitto

            with Cluster('view', graph_attr={'fontsize': '15'}):
                grafana = Grafana('Grafana')

            with Cluster('automation', graph_attr={'fontsize': '15'}):
                ha = Custom('Home Assistant', '../images/home-assistant.png')
                # ha_mobile = Custom('HA Mobile', '../images/home-assistant-mobile.png')
                volume_ha = Docker("Volume Docker")
                rclone_ha = Custom('Rclone', '../images/rclone.png')
                ha_mobile >> Edge() << ha
                ha >> volume_ha << rclone_ha >> google_drive

            with Cluster('monitoring', graph_attr={'fontsize': '15'}):
                glances = Docker('Glances')
                Docker('Portainer')

                glances >> ha

    # services x database
    health_mysql >> Edge() << mysql
    grafana << mysql

    # services x rabbitMQ
    health_rabbit >> Edge() << rabbitmq
    ha_link >> rabbitmq

    # Others
    ha >> Edge() << mosquitto
    ha_link << ha
    # ha_mobile >> Edge() << ha
