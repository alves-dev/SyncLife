from datetime import datetime

from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.container import Docker
from diagrams.onprem.database import Mysql
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import RabbitMQ
from diagrams.onprem.vcs import Github
from diagrams.programming.language import Csharp, Java, Go

all_formats = ["jpg", "png", "svg", "pdf", "dot"]
formats = ["pdf"]

date = datetime.now().strftime('%Y-%m-%d')
date_name = datetime.now().strftime('%Y_%m_%d')

with Diagram(f'Arquitetura - {date}', show=False, direction='TB', outformat=formats,
             filename=f'out_pdf/architecture_{date_name}',
             graph_attr={'labelloc': 't', 'fontsize': '20'}):

    with Cluster('internet', graph_attr={'fontsize': '15'}):
        google_drive = Custom('Google drive', '../images/google-drive.png')
        git_hub = Github('Action schedule')

        with Cluster('automation', graph_attr={'fontsize': '15'}):
            ha_mobile = Custom('HA Mobile', '../images/home-assistant-mobile.png')

    with Cluster('local-network', graph_attr={'fontsize': '15'}):
        core_dns = Custom("", '../images/dns.png')
        proxy = Custom("swag", '../images/swag.png')
        cloudflare = Custom("Tunnel", '../images/tunnel.png')

        core_dns >> Edge() << proxy >> Edge() << cloudflare

        with Cluster('', graph_attr={'fontsize': '15'}):

            with Cluster('data', graph_attr={'fontsize': '15'}):
                mysql = Mysql('')
                redis = Redis('Redis')
                mysql_cron = Custom('Cron Backup', '../images/cron.png')
                rclone_mysql = Custom('', '../images/rclone.png')
                volume_mysql = Docker("Volume")
                mysql >> mysql_cron >> volume_mysql
                volume_mysql << rclone_mysql >> google_drive

            with Cluster('health', graph_attr={'fontsize': '15'}):
                service_nutri_track = Java('Nutri Track')
                service_body_track = Custom('Body Track', '../images/kotlin.png')
                service_exercise = Custom('Exercise Service', '../images/kotlin.png')

                ha_link = Custom('HA Link Service', '../images/python.png')

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
                mosquitto = Custom('', '../images/mosquitto.png')
                rabbitmq = RabbitMQ('RabbitMQ')
                subscription = Go('Subscription')
                rabbitmq >> Edge() << event_sync >> Edge() << mosquitto
                subscription >> Edge() << rabbitmq

            with Cluster('view', graph_attr={'fontsize': '15'}):
                grafana = Custom('', '../images/grafana.png')

            with Cluster('automation', graph_attr={'fontsize': '15'}):
                ha = Custom('Home Assistant', '../images/home-assistant.png')
                volume_ha = Docker("Volume")
                rclone_ha = Custom('', '../images/rclone.png')
                ha_mobile >> Edge() << ha
                ha >> volume_ha << rclone_ha >> google_drive

            with Cluster('infrastructure', graph_attr={'fontsize': '15'}):
                glances = Custom('', '../images/glances.png')
                Custom('', '../images/portainer.png')
                inspector = Custom('Task - repo-inspector', '../images/python.png')

                glances >> ha
                inspector >> redis
                git_hub >> inspector

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
