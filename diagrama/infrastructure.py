from datetime import datetime

from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.generic.network import Router

all_formats = ["jpg", "png", "svg", "pdf", "dot"]
formats = ["pdf"]

date = datetime.now().strftime('%Y-%m-%d')
date_name = datetime.now().strftime('%Y_%m_%d')

with Diagram(f'Infraestrutura fisica - {date}', show=False, direction='LR', outformat=formats,
             filename=f'out_pdf/infrastructure_{date_name}',
             graph_attr={'labelloc': 't', 'fontsize': '20'}):
    internet = Custom('Internet', '../images/web.png')

    with Cluster('Home', graph_attr={'fontsize': '15'}):
        provider = Router('Roteador bridge: Arris')
        tp_link = Custom('Roteador', '../images/tp-link.png')

        with Cluster('Rack', graph_attr={'fontsize': '15'}):
            raspberry = Custom('Raspberry pi 4', '../images/raspberry-pi.png')
            think_centre = Custom('ThinkCentre', '../images/lenovo.png')

        provider >> Edge(label='cabo') << tp_link >> Edge(label='cabo') << raspberry
        tp_link >> Edge(label='cabo') << think_centre

    internet >> Edge(label='Fibra') << provider
